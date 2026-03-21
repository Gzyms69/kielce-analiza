import geopandas as gpd
import pandas as pd
import json
import os
import gc
import warnings
import concurrent.futures
import re
import numpy as np
from pathlib import Path
from datetime import datetime

warnings.filterwarnings('ignore')

CITY_BASELINES = {
    "warszawa": 1800000, "krakow": 800000, "lodz": 670000, "wroclaw": 640000,
    "poznan": 530000, "szczecin": 400000, "bydgoszcz": 340000, "lublin": 330000,
    "bialystok": 290000, "katowice": 290000, "gzm": 2300000,
    "rzeszow": 190000, "kielce": 190000, "olsztyn": 170000, "radom": 200000,
    "torun": 190000, "czestochowa": 210000, "legnica": 90000,
    "elblag": 110000, "opole": 120000, "gorzow": 120000, "suwalki": 70000,
    "elk": 60000, "lomza": 60000, "przemysl": 60000, "gizycko": 30000, "swinoujscie": 40000
}

TAG_WHITELIST = {
    "aerodrome": "international_airport", "terminal": "airport_terminal", "port": "major_seaport", "station": "rail_hub",
    "university": "university_campus", "college": "university_campus", "faculty": "university_campus",
    "stadium": "national_stadium", "arena": "national_stadium", "exhibition_centre": "exhibition_centre", "hospital": "hospital_clinical",
    "mall": "shopping_mall", "shopping_centre": "shopping_mall", "department_store": "shopping_mall", "office": "business_office",
    "company": "business_office", "industrial": "industrial_zone", "commercial": "commercial_zone", "warehouse": "logistics_hub",
    "courthouse": "government_central", "court_house": "government_central", "townhall": "government_central", "government": "government_central",
    "supermarket": "supermarket", "student_accommodation": "student_dormitory", "dormitory": "student_dormitory",
    "school": "education_high_school", "marketplace": "marketplace", "social_facility": "social_support_mops", "clinic": "health_clinic",
    "doctors": "health_clinic", "dentist": "health_clinic", "theatre": "culture_theatre", "cinema": "culture_theatre",
    "museum": "culture_theatre", "library": "culture_theatre", "sports_hall": "sports_centre", "sports_centre": "sports_centre",
    "swimming_pool": "sports_centre", "kindergarten": "education_preschool", "pharmacy": "pharmacy", "bank": "bank",
    "post_office": "post_office", "police": "police_station", "convenience": "convenience_store", "place_of_worship": "place_of_worship",
    "park": "park_recreation", "garden": "park_recreation", "hotel": "hotel_accommodation", "hostel": "hotel_accommodation",
    "clothes": "specialized_retail", "furniture": "specialized_retail", "electronics": "specialized_retail", "fuel": "car_services",
    "car_repair": "car_services", "restaurant": "gastronomy", "cafe": "gastronomy", "fast_food": "gastronomy",
    "beauty": "personal_services", "hairdresser": "personal_services", "chemist": "personal_services", "airfield": "local_airfield",
    "parcel_locker": "micro_parcel_locker", "atm": "micro_atm", "playground": "micro_playground"
}

def parse_hstore(hstore_str):
    if not hstore_str or pd.isna(hstore_str): return {}
    pattern = r'"?([^"=>]+)"?=>"?([^",]+)"?'
    return dict(re.findall(pattern, hstore_str))

def identify_category(row):
    tags = parse_hstore(row.get('all_tags', ''))
    for col in ['amenity', 'shop', 'office', 'leisure', 'aeroway', 'railway', 'landuse', 'industrial']:
        if col in row and pd.notna(row[col]): tags[col] = row[col]
    nm = (tags.get('name') or tags.get('official_name') or "").lower()
    if tags.get("aeroway") == "aerodrome":
        if "iata" in tags or any(x in nm for x in ["chopin", "modlin", "balice", "pyrzowice", "jasionka", "ławica", "rebiechowo"]):
            return "international_airport"
        return "local_airfield"
    if tags.get("railway") == "station":
        if "uic_ref" in tags or any(x in nm for x in ["główn", "glown", "central", "fabrycz", "kalisk"]):
            return "national_rail_hub"
        return "regional_rail_hub"
    for k in ['amenity', 'shop', 'office', 'landuse', 'leisure', 'industrial']:
        val = tags.get(k)
        if val in TAG_WHITELIST: return TAG_WHITELIST[val]
    return None

def audit_single_city(city, data_dir, cities_root):
    city_dir = cities_root / city
    results_dir = city_dir / "04_results"
    spatial_dir = city_dir / "02_spatial"
    config_dir = city_dir / "03_config"
    
    dna_path = results_dir / "stop_dna.gpkg"
    if not dna_path.exists(): return None, None, False

    print(f"[{city}] Audyt...")
    
    city_stats = {'stops': 0, 'pop': 0, 'rcn': 0, 'osm_pts': 0, 'osm_ply': 0}
    macro_stats, poi_md, dump_md = [], [], []
    
    try:
        dna = gpd.read_file(dna_path)
        city_stats['stops'] = len(dna)
        
        # FAZA 0
        pop_path = spatial_dir / "population_250m.gpkg"
        if pop_path.exists():
            pop_df = gpd.read_file(pop_path)
            city_stats['pop'] = pop_df['TOT'].sum()
            macro_stats.append(f"- **Populacja:** {city_stats['pop']:,.0f}")
            del pop_df
            
        rcn_path = spatial_dir / "transactions.gpkg"
        if rcn_path.exists():
            rcn_full = gpd.read_file(rcn_path, ignore_geometry=True)
            city_stats['rcn'] = len(rcn_full)
            macro_stats.append(f"- **Transakcje RCN:** {len(rcn_full):,.0f}")
            del rcn_full

        # FAZA III
        val_file = config_dir / "poi_valuation.json"
        if val_file.exists():
            with open(val_file, 'r') as f:
                val_data = json.load(f)
            sorted_poi = sorted(val_data.items(), key=lambda x: x[1]['final_value'], reverse=True)
            poi_md.append("\n| Kategoria | Tier | Ilość | Wartość |\n|---|---|---|---|")
            for cat, d in sorted_poi[:20]:
                poi_md.append(f"| `{cat}` | {d['tier']} | {d['count']} | {d['final_value']:,.0f} |")

        # INFRASTRUKTURA DLA FAZY IV
        infra_path = spatial_dir / "infrastructure.gpkg"
        tagged_infra = None
        if infra_path.exists():
            all_layers = []
            for layer in ['points', 'multipolygons']:
                gdf = gpd.read_file(infra_path, layer=layer)
                if layer == 'points': city_stats['osm_pts'] += len(gdf)
                else: city_stats['osm_ply'] += len(gdf)
                if not gdf.empty:
                    if gdf.crs.to_string() != "EPSG:2180": gdf = gdf.to_crs("EPSG:2180")
                    if layer == 'multipolygons': gdf['geometry'] = gdf.geometry.centroid
                    gdf['cat'] = gdf.apply(identify_category, axis=1)
                    all_layers.append(gdf[gdf['cat'].notna()])
            if all_layers: tagged_infra = pd.concat(all_layers, ignore_index=True)

        # FAZA IV
        if 'local_percentile' in dna.columns:
            dna_s = dna.sort_values('local_percentile', ascending=False)
            
            def render(df, title):
                r_md = [f"\n#### {title}"]
                for _, row in df.iterrows():
                    nm, h3 = row.get('stop_name', 'N/A'), row.get('h3_index', 'N/A')
                    r_md.append(f"<details><summary><b>{nm} ({h3})</b></summary>\n\n```text")
                    
                    groups = {
                        "[IDENTYFIKACJA]": ['stop_name', 'stop_id', 'h3_index'],
                        "[OCENA DNA]": ['grade', 'local_percentile', 'local_score_raw'],
                        "[FILAR 1: INFRA]": ['infra_score', 'raw_gravity', 'domain_count'],
                        "[FILAR 2: TRANSIT]": ['transit_freq', 'hourly_freq'],
                        "[FILAR 3: RCN]": ['market_val', 'liquidity'],
                        "[FILAR 4: POP]": ['pop_val']
                    }
                    
                    for gn, cs in groups.items():
                        r_md.append(f"\n{gn}")
                        for c in cs:
                            if c in dna.columns:
                                v = row[c]
                                if pd.isna(v) or str(v).lower() == 'nan': continue
                                r_md.append(f"  {c.ljust(18)}: {v:.4f}" if isinstance(v, (float, np.float64)) else f"  {c.ljust(18)}: {v}")
                    
                    if tagged_infra is not None:
                        nearby = tagged_infra[tagged_infra.geometry.distance(row.geometry) <= 500]
                        if not nearby.empty:
                            r_md.append("\n[POI W POBLIŻU 500M]")
                            p_counts = nearby['cat'].value_counts()
                            for cat, count in p_counts.items():
                                r_md.append(f"  {cat.ljust(25)}: {count}")
                    r_md.append("```\n</details>")
                return r_md

            dump_md.extend(render(dna_s.head(5), "NAJLEPSZE PRZYSTANKI"))
            dump_md.extend(render(dna_s.tail(5), "NAJSŁABSZE PRZYSTANKI"))

        res_md = [f"## {city.upper()}", "\n### Faza 0: Statystyki ogólne"]; res_md.extend(macro_stats)
        res_md.append("\n### Faza III: Top 20 POI (Miasto)"); res_md.extend(poi_md)
        res_md.append("\n### Faza IV: Próbki przystanków"); res_md.extend(dump_md)
        res_md.append("\n---\n")
        
        del dna, tagged_infra; gc.collect()
        return "\n".join(res_md), city_stats, False
    except Exception as e:
        return f"### {city.upper()}\n**BŁĄD:** {e}\n---", city_stats, True

def run_100_percent_validation():
    data_dir, cities_root = Path("data"), Path("data/cities")
    reports_dir = Path("reports/audits")
    reports_dir.mkdir(parents=True, exist_ok=True)
    report_path = reports_dir / f"GOLDEN_DNA_AUDIT_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    cities = sorted([d.name for d in cities_root.iterdir() if d.is_dir() and d.name != 'rail'])
    
    global_agg = {'stops': 0, 'fails': 0, 'cities': 0, 'pop': 0, 'rcn': 0, 'osm_pts': 0, 'osm_ply': 0}
    city_reports_dict = {}
    
    print(f"=== AUDYT RÓWNOLEGŁY (4 WORKERS) ===")
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(audit_single_city, city, data_dir, cities_root): city for city in cities}
        for future in concurrent.futures.as_completed(futures):
            city_name = futures[future]
            res_md, res_stats, failed = future.result()
            if res_md:
                city_reports_dict[city_name] = res_md
                global_agg['cities'] += 1
                if failed: global_agg['fails'] += 1
                for k in ['stops', 'pop', 'rcn', 'osm_pts', 'osm_ply']: global_agg[k] += res_stats.get(k, 0)

    full_report = [
        f"# RAPORT WALIDACJI DNA - {datetime.now().strftime('%Y-%m-%d')}\n",
        "---",
        "## PODSUMOWANIE POLSKI",
        f"- Miasta: {global_agg['cities']}",
        f"- Populacja: {global_agg['pop']:,.0f}",
        f"- Transakcje RCN: {global_agg['rcn']:,.0f}",
        f"- Obiekty OSM: {global_agg['osm_pts'] + global_agg['osm_ply']:,.0f}",
        "---\n"
    ]
    full_report.extend([city_reports_dict[c] for c in sorted(city_reports_dict.keys())])
    with open(report_path, "w", encoding="utf-8") as f: f.write("\n".join(full_report))
    print(f"\nGotowe: {report_path}")

if __name__ == "__main__":
    run_100_percent_validation()
