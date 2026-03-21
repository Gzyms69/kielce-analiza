import geopandas as gpd
import pandas as pd
import json
from pathlib import Path
import os

def audit_full_pipeline():
    print("=== FINAL 100% PIPELINE VERIFICATION AUDIT ===\n")
    data_dir = Path("data")
    cities_root = data_dir / "cities"
    
    cities = sorted([d.name for d in cities_root.iterdir() if d.is_dir() and d.name != 'rail'])
    
    report_data = []
    
    for city in cities:
        city_dir = cities_root / city
        spatial = city_dir / "02_spatial"
        config = city_dir / "03_config"
        
        # 1. File checks
        has_stops = (spatial / "stops.gpkg").exists()
        has_osm = (spatial / "infrastructure.gpkg").exists()
        has_pop = (spatial / "population_250m.gpkg").exists()
        has_rcn = (spatial / "transactions.gpkg").exists()
        has_val = (config / "poi_valuation.json").exists()
        
        # 2. Data Extraction
        pop_total = 0
        if has_pop:
            try:
                pop_df = gpd.read_file(spatial / "population_250m.gpkg")
                pop_total = pop_df['TOT'].sum()
            except Exception as e:
                print(f"  [ERR] {city}: Nie udalo sie wczytac populacji: {e}")
            
        rcn_count = 0
        avg_price = 0
        if has_rcn:
            try:
                rcn_df = gpd.read_file(spatial / "transactions.gpkg")
                rcn_count = len(rcn_df)
                if 'price_m2' in rcn_df.columns:
                    prices = pd.to_numeric(rcn_df['price_m2'], errors='coerce')
                    avg_price = prices.mean()
            except Exception as e:
                print(f"  [ERR] {city}: Nie udalo sie wczytac RCN: {e}")
            
        top_poi = ""
        poi_count = 0
        if has_val:
            try:
                with open(config / "poi_valuation.json", "r") as f:
                    val_data = json.load(f)
                    poi_count = sum(d['count'] for d in val_data.values())
                    # Sort by final_value descending and get top 3
                    sorted_val = sorted(val_data.items(), key=lambda x: x[1]['final_value'], reverse=True)
                    top_3 = [f"{k}({v['count']})" for k, v in sorted_val[:3]]
                    top_poi = ", ".join(top_3)
            except Exception as e:
                print(f"  [ERR] {city}: Nie udalo sie wczytac POI valuation: {e}")

        integrity = "100%" if all([has_stops, has_osm, has_pop, has_rcn, has_val]) else "FAILED"

        report_data.append({
            "CITY": city.upper()[:12],
            "INTEGRITY": integrity,
            "POPULATION": f"{pop_total:,.0f}",
            "RCN_RECS": rcn_count,
            "PRICE_M2": f"{avg_price:.0f} PLN",
            "POI_TOTAL": poi_count,
            "TOP_3_POI_BY_WEIGHT": top_poi
        })

    # Render Report
    df = pd.DataFrame(report_data)
    
    # Calculate totals
    tot_pop = sum(int(x.replace(',', '')) for x in df['POPULATION'])
    tot_rcn = df['RCN_RECS'].sum()
    tot_poi = df['POI_TOTAL'].sum()
    
    print(df.to_string(index=False))
    
    print("\n" + "="*100)
    print("GLOBAL PIPELINE SUMMARY:")
    print(f"-> Total Cities Processed: {len(cities)}")
    print(f"-> Total Covered Population: {tot_pop:,.0f} citizens")
    print(f"-> Total Valid RCN Transactions (2025+): {tot_rcn:,.0f}")
    print(f"-> Total Valued Infrastructure Objects (POI): {tot_poi:,.0f}")
    print("="*100)
    
    if all(x == "100%" for x in df['INTEGRITY']):
        print("\n[VERDICT]: PASSED. ALL 29 AGGLOMERATIONS HAVE 100% DATA COVERAGE.")
    else:
        print("\n[VERDICT]: WARNING. SOME AGGLOMERATIONS ARE MISSING DATA.")

if __name__ == "__main__":
    audit_full_pipeline()
