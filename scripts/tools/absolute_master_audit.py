import geopandas as gpd
import pandas as pd
from pathlib import Path
import json
import warnings
import sys

warnings.filterwarnings('ignore')

def audit_city_data(city, city_dir):
    spatial_dir = city_dir / "02_spatial"
    
    city_report = {
        "CITY": city.upper(),
        "STOPS_COUNT": 0, "STOPS_NULL_NAME": 0,
        "OSM_POINTS": 0, "OSM_POLYGONS": 0, "OSM_NULL_CAT": 0,
        "POPULATION_TOTAL": 0,
        "RCN_COUNT": 0, "RCN_MIN_DATE": "N/A", "RCN_MAX_DATE": "N/A",
        "RCN_NULL_PRICE": 0, "RCN_AVG_M2": 0,
        "ERRORS": []
    }
    
    # 1. STOPS
    stops_path = spatial_dir / "stops.gpkg"
    if stops_path.exists():
        try:
            df = gpd.read_file(stops_path)
            city_report["STOPS_COUNT"] = len(df)
            if 'stop_name' in df.columns:
                city_report["STOPS_NULL_NAME"] = df['stop_name'].isna().sum()
        except Exception as e:
            city_report["ERRORS"].append(f"STOPS: {str(e)[:30]}")
    else:
        city_report["ERRORS"].append("MISSING: stops.gpkg")

    # 2. OSM
    osm_path = spatial_dir / "infrastructure.gpkg"
    if osm_path.exists():
        try:
            pts = gpd.read_file(osm_path, layer="points")
            polys = gpd.read_file(osm_path, layer="multipolygons")
            city_report["OSM_POINTS"] = len(pts)
            city_report["OSM_POLYGONS"] = len(polys)
            
            # Category completeness (checking amenity, shop, etc.)
            cat_cols = ['amenity', 'shop', 'leisure', 'office', 'landuse']
            missing_cats = 0
            for df in [pts, polys]:
                if not df.empty:
                    available = [c for c in cat_cols if c in df.columns]
                    if available:
                        mask = df[available].isna().all(axis=1)
                        missing_cats += mask.sum()
            city_report["OSM_NULL_CAT"] = missing_cats
        except Exception as e:
            city_report["ERRORS"].append(f"OSM: {str(e)[:30]}")
    else:
        city_report["ERRORS"].append("MISSING: infrastructure.gpkg")

    # 3. POPULATION
    pop_path = spatial_dir / "population_250m.gpkg"
    if pop_path.exists():
        try:
            df = gpd.read_file(pop_path)
            if 'TOT' in df.columns:
                city_report["POPULATION_TOTAL"] = int(df['TOT'].sum())
        except Exception as e:
            city_report["ERRORS"].append(f"POP: {str(e)[:30]}")
    else:
        city_report["ERRORS"].append("MISSING: population.gpkg")

    # 4. RCN
    rcn_path = spatial_dir / "transactions.gpkg"
    if rcn_path.exists():
        try:
            df = gpd.read_file(rcn_path)
            city_report["RCN_COUNT"] = len(df)
            
            if not df.empty:
                if 'dok_data' in df.columns:
                    df['dok_data'] = pd.to_datetime(df['dok_data'], errors='coerce', utc=True)
                    city_report["RCN_MIN_DATE"] = df['dok_data'].min().strftime('%Y-%m-%d') if not df['dok_data'].isna().all() else "N/A"
                    city_report["RCN_MAX_DATE"] = df['dok_data'].max().strftime('%Y-%m-%d') if not df['dok_data'].isna().all() else "N/A"
                
                # Standaryzacja kolumn RCN (często nazwy różnią się z powodu GML/JSON)
                cena_col = 'tran_cena_brutto' if 'tran_cena_brutto' in df.columns else ('price' if 'price' in df.columns else None)
                pow_col = 'lok_pow_uzyt' if 'lok_pow_uzyt' in df.columns else ('area' if 'area' in df.columns else None)
                
                if cena_col:
                    if df[cena_col].dtype == 'object':
                        df[cena_col] = df[cena_col].str.replace(' ', '').str.replace(',', '.')
                    df[cena_col] = pd.to_numeric(df[cena_col], errors='coerce')
                    city_report["RCN_NULL_PRICE"] = int(df[cena_col].isna().sum())
                
                if cena_col and pow_col:
                    if df[pow_col].dtype == 'object':
                        df[pow_col] = df[pow_col].str.replace(' ', '').str.replace(',', '.')
                    df[pow_col] = pd.to_numeric(df[pow_col], errors='coerce')
                    
                    df['m2'] = df[cena_col] / df[pow_col]
                    valid = df[(df['m2'] > 500) & (df['m2'] < 50000)]['m2']
                    if not valid.empty:
                        city_report["RCN_AVG_M2"] = int(valid.mean())
                        
        except Exception as e:
            city_report["ERRORS"].append(f"RCN: {str(e)[:30]}")
    else:
        city_report["ERRORS"].append("MISSING: transactions.gpkg")

    return city_report

def main():
    print("=========================================================================================")
    print("                       ABSOLUTE MASTER AUDIT OF URBAN GRAVITY DATA")
    print("=========================================================================================")
    
    data_dir = Path("data/cities")
    cities = sorted([d for d in data_dir.iterdir() if d.is_dir() and d.name != 'rail'])
    
    reports = []
    for city_dir in cities:
        reports.append(audit_city_data(city_dir.name, city_dir))
        
    df = pd.DataFrame(reports)
    
    # Format and Display
    print("\n--- 1. SPATIAL & DEMOGRAPHIC HEALTH ---")
    df_spatial = df[['CITY', 'STOPS_COUNT', 'STOPS_NULL_NAME', 'POPULATION_TOTAL', 'OSM_POINTS', 'OSM_POLYGONS', 'OSM_NULL_CAT']]
    print(df_spatial.to_string(index=False))
    
    print("\n--- 2. REAL ESTATE (RCN) INTEGRITY ---")
    df_rcn = df[['CITY', 'RCN_COUNT', 'RCN_MIN_DATE', 'RCN_MAX_DATE', 'RCN_NULL_PRICE', 'RCN_AVG_M2']]
    print(df_rcn.to_string(index=False))
    
    print("\n--- 3. CRITICAL ERRORS & MISSING DATA ---")
    errors_exist = False
    for r in reports:
        if r['ERRORS']:
            errors_exist = True
            print(f"[{r['CITY']}] -> " + " | ".join(r['ERRORS']))
    
    if not errors_exist:
        print("ALL CLEAR. NO CRITICAL FILE STRUCTURE ERRORS DETECTED.")
        
    print("\n=========================================================================================")
    print(f" TOTAL STOPS ACROSS POLAND: {df['STOPS_COUNT'].sum():,}")
    print(f" TOTAL TRACKED POPULATION:  {df['POPULATION_TOTAL'].sum():,}")
    print(f" TOTAL RCN TRANSACTIONS:    {df['RCN_COUNT'].sum():,}")
    print("=========================================================================================")

if __name__ == "__main__":
    main()
