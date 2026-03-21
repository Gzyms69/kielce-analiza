import geopandas as gpd
import pandas as pd
import json
import math
from pathlib import Path
import warnings
import os
import re
import argparse

warnings.filterwarnings("ignore")

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

# --- URBAN GRAVITY ENGINE 7.9: TRANSPORT-CENTRIC TAXONOMY ---
TIER_VALUES = {
    "T0_MEGA_HUB":        20000000.0, # Airport, Port, Rail Hub
    "T1_NATIONAL_MAGNET": 10000000.0, # Hospital, University, Stadium
    "T2_STRATEGIC_HUB":   1000000.0,  # Mall, Office, Industrial, Commercial, Gov
    "T3_LOCAL_CORE":      100000.0,   # High School, Culture, Marketplace, Sport
    "T4_DAILY_SERVICE":   10000.0,    # Pharmacy, Bank, Post, Convenience, Kindergarten (SPADEK)
    "T5_SPEC_GASTRO":     1000.0,     # Restaurant, Local Airfield (SPADEK)
    "T6_MICRO_INFRA":     10.0        # ATM, Locker
}

TAG_WHITELIST = {
    # T0 - MEGA HUBS
    "aerodrome": ("international_airport", "T0_MEGA_HUB"),
    "terminal":  ("airport_terminal", "T0_MEGA_HUB"),
    "port":      ("major_seaport", "T0_MEGA_HUB"),
    "station":   ("rail_hub", "T0_MEGA_HUB"),
    
    # T1 - NATIONAL MAGNETS
    "university": ("university_campus", "T1_NATIONAL_MAGNET"),
    "college":    ("university_campus", "T1_NATIONAL_MAGNET"),
    "faculty":    ("university_campus", "T1_NATIONAL_MAGNET"),
    "stadium":    ("national_stadium", "T1_NATIONAL_MAGNET"),
    "arena":      ("national_stadium", "T1_NATIONAL_MAGNET"),
    "exhibition_centre": ("exhibition_centre", "T1_NATIONAL_MAGNET"),
    "hospital":              ("hospital_clinical", "T1_NATIONAL_MAGNET"),

    # T2 - STRATEGIC HUBS
    "mall":                  ("shopping_mall", "T2_STRATEGIC_HUB"),
    "shopping_centre":       ("shopping_mall", "T2_STRATEGIC_HUB"),
    "department_store":      ("shopping_mall", "T2_STRATEGIC_HUB"),
    "office":                ("business_office", "T2_STRATEGIC_HUB"),
    "company":               ("business_office", "T2_STRATEGIC_HUB"),
    "industrial":            ("industrial_zone", "T2_STRATEGIC_HUB"),
    "commercial":            ("commercial_zone", "T2_STRATEGIC_HUB"),
    "warehouse":             ("logistics_hub", "T2_STRATEGIC_HUB"),
    "courthouse":            ("government_central", "T2_STRATEGIC_HUB"),
    "court_house":           ("government_central", "T2_STRATEGIC_HUB"),
    "townhall":              ("government_central", "T2_STRATEGIC_HUB"),
    "government":            ("government_central", "T2_STRATEGIC_HUB"),
    "supermarket":           ("supermarket", "T2_STRATEGIC_HUB"),
    "student_accommodation": ("student_dormitory", "T2_STRATEGIC_HUB"),
    "dormitory":             ("student_dormitory", "T2_STRATEGIC_HUB"),

    # T3 - LOCAL CORES
    "school":                ("education_high_school", "T3_LOCAL_CORE"),
    "marketplace":           ("marketplace", "T3_LOCAL_CORE"),
    "social_facility": ("social_support_mops", "T3_LOCAL_CORE"),
    "clinic":          ("health_clinic", "T3_LOCAL_CORE"),
    "doctors":         ("health_clinic", "T3_LOCAL_CORE"),
    "dentist":         ("health_clinic", "T3_LOCAL_CORE"),
    "theatre":         ("culture_theatre", "T3_LOCAL_CORE"),
    "cinema":          ("culture_theatre", "T3_LOCAL_CORE"),
    "museum":          ("culture_theatre", "T3_LOCAL_CORE"),
    "library":         ("culture_theatre", "T3_LOCAL_CORE"),
    "sports_hall":     ("sports_centre", "T3_LOCAL_CORE"),
    "sports_centre":   ("sports_centre", "T3_LOCAL_CORE"),
    "swimming_pool":   ("sports_centre", "T3_LOCAL_CORE"),

    # T4 - DAILY SERVICES
    "kindergarten":    ("education_preschool", "T4_DAILY_SERVICE"),
    "pharmacy":         ("pharmacy", "T4_DAILY_SERVICE"),
    "bank":             ("bank", "T4_DAILY_SERVICE"),
    "post_office":      ("post_office", "T4_DAILY_SERVICE"),
    "police":           ("police_station", "T4_DAILY_SERVICE"),
    "convenience":      ("convenience_store", "T4_DAILY_SERVICE"),
    "place_of_worship": ("place_of_worship", "T4_DAILY_SERVICE"),
    "park":             ("park_recreation", "T4_DAILY_SERVICE"),
    "garden":           ("park_recreation", "T4_DAILY_SERVICE"),
    "hotel":            ("hotel_accommodation", "T4_DAILY_SERVICE"),
    "hostel":           ("hotel_accommodation", "T4_DAILY_SERVICE"),
    "clothes":          ("specialized_retail", "T4_DAILY_SERVICE"),
    "furniture":        ("specialized_retail", "T4_DAILY_SERVICE"),
    "electronics":      ("specialized_retail", "T4_DAILY_SERVICE"),
    "fuel":             ("car_services", "T4_DAILY_SERVICE"),
    "car_repair":       ("car_services", "T4_DAILY_SERVICE"),

    # T5 - SPECIALIZED / LOW IMPACT
    "restaurant": ("gastronomy", "T5_SPEC_GASTRO"),
    "cafe":       ("gastronomy", "T5_SPEC_GASTRO"),
    "fast_food":  ("gastronomy", "T5_SPEC_GASTRO"),
    "beauty":     ("personal_services", "T5_SPEC_GASTRO"),
    "hairdresser":("personal_services", "T5_SPEC_GASTRO"),
    "chemist":    ("personal_services", "T5_SPEC_GASTRO"),
    "airfield":   ("local_airfield", "T5_SPEC_GASTRO"),

    # T6 - MICRO
    "parcel_locker": ("micro_parcel_locker", "T6_MICRO_INFRA"),
    "atm":           ("micro_atm", "T6_MICRO_INFRA"),
    "playground":    ("micro_playground", "T6_MICRO_INFRA")
}

def parse_hstore(hstore_str):
    if not hstore_str or pd.isna(hstore_str): return {}
    pattern = r'"?([^"=>]+)"?=>"?([^",]+)"?'
    return dict(re.findall(pattern, hstore_str))

def identify_v7_9_tag(row, city_name):
    tags = parse_hstore(row.get('all_tags', ''))
    for col in ['amenity', 'shop', 'office', 'leisure', 'aeroway', 'railway', 'landuse', 'industrial']:
        if col in row and pd.notna(row[col]): tags[col] = row[col]
    
    nm = (tags.get('name') or tags.get('official_name') or "").lower()

    # Specyficzna logika dla Lotnisk (T0 vs T5)
    if tags.get("aeroway") == "aerodrome":
        if "iata" in tags or any(x in nm for x in ["chopin", "modlin", "balice", "pyrzowice", "jasionka", "ławica", "rebiechowo"]):
            return ("international_airport", "T0_MEGA_HUB")
        return ("local_airfield", "T5_SPEC_GASTRO")
        
    if tags.get("railway") == "station":
        if "uic_ref" in tags or any(x in nm for x in ["główn", "glown", "central", "fabrycz", "kalisk"]):
            return ("national_rail_hub", "T0_MEGA_HUB")
        return ("regional_rail_hub", "T1_NATIONAL_MAGNET")

    for k in ['amenity', 'shop', 'office', 'landuse', 'leisure', 'industrial']:
        val = tags.get(k)
        if val in TAG_WHITELIST: return TAG_WHITELIST[val]
            
    return None, None

def process_city(city_name, data_dir):
    city_dir = data_dir / "cities" / city_name
    spatial_dir = city_dir / "02_spatial"
    pop_path = spatial_dir / "population_250m.gpkg"
    infra_path = spatial_dir / "infrastructure.gpkg"
    
    if not pop_path.exists() or not infra_path.exists():
        return False
        
    try:
        pop = gpd.read_file(pop_path)
        h_grav = math.log10(pop["TOT"].sum()) if not pop.empty and pop["TOT"].sum() > 0 else 1.0
        
        objs = []
        for layer in ["points", "multipolygons"]:
            gdf = gpd.read_file(infra_path, layer=layer)
            gdf['area_m2'] = gdf.to_crs("EPSG:2180").area if layer == "multipolygons" else 0
            for _, row in gdf.iterrows():
                cat_name, tier = identify_v7_9_tag(row, city_name)
                if cat_name:
                    base_val = TIER_VALUES[tier]
                    d_mult = 1.0
                    if "rail" in cat_name or "airport" in cat_name: d_mult = 15.0
                    
                    area_factor = 1.0 + math.log10((row['area_m2'] / 100.0) + 1) if row['area_m2'] > 0 else 1.0
                    objs.append({"cat": cat_name, "tier": tier, "val": base_val * h_grav * area_factor * d_mult})
        
        if not objs: return False
            
        df = pd.DataFrame(objs)
        val = {}
        for cat in df['cat'].unique():
            c_df = df[df['cat'] == cat]
            scarcity = 1.0 + (math.log2((len(df)/len(c_df))+1) / 50.0)
            val[cat] = {"count": len(c_df), "tier": c_df.iloc[0]['tier'], "final_value": round(c_df['val'].mean() * scarcity, 2)}
            
        with open(city_dir / "03_config" / "poi_valuation.json", "w", encoding="utf-8") as f:
            json.dump(val, f, indent=4, ensure_ascii=False)
            
        print(f"__PIPELINE_METRICS__={json.dumps({'city': city_name, 'poi': len(df), 'grav': round(h_grav, 2)})}")
        return True
    except Exception as e:
        print(f"[ERR] {city_name}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", required=True)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    process_city(args.city, get_data_dir())

if __name__ == "__main__":
    main()
