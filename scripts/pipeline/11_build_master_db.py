import geopandas as gpd
import pandas as pd
from pathlib import Path
import os
import sys

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def get_allowed_cities():
    cities_env = os.environ.get("PIPELINE_CITIES")
    if cities_env:
        return [c.strip() for c in cities_env.split(',')]
    return None

def restore_full_data():
    print("=== TASK 1.8: MASTER DB CONSOLIDATION ===\n")
    data_dir = get_data_dir()
    master_db = data_dir / "database" / "master_analytical.gpkg"
    
    if master_db.exists():
        os.remove(master_db)
        
    master_db.parent.mkdir(parents=True, exist_ok=True)
    
    cities_root = data_dir / "cities"
    if not cities_root.exists(): return
    
    cities = sorted([d.name for d in cities_root.iterdir() if d.is_dir()])
    allowed_cities = get_allowed_cities()
    
    all_stops = []
    all_transactions = []
    
    for city in cities:
        if allowed_cities and city not in allowed_cities:
            continue
            
        print(f"  Restoring {city}...")
        city_dir = cities_root / city
        stops_path = city_dir / "smart_stops.gpkg"
        
        # Checking old and new location for stops
        if not stops_path.exists():
            stops_path = city_dir / "02_spatial" / "stops.gpkg"
            
        rcn_path = city_dir / "02_spatial" / "transactions.gpkg"
        if not rcn_path.exists():
            rcn_path = city_dir / "rcn" / "transactions.gpkg"
        
        if stops_path.exists():
            try:
                stops = gpd.read_file(stops_path).to_crs("EPSG:2180")
                stops['city'] = city
                all_stops.append(stops)
            except Exception as e: 
                print(f"    [ERR STOPS] {city}: {e}")
            
        if rcn_path.exists():
            try:
                rcn = gpd.read_file(rcn_path).to_crs("EPSG:2180")
                rcn['city'] = city
                
                # Tylko odrzucenie absolutnych anomalii technicznych (powyżej 5 mln/m2)
                if 'price_m2' in rcn.columns:
                    rcn['price_m2'] = pd.to_numeric(rcn['price_m2'], errors='coerce')
                    rcn = rcn[(rcn['price_m2'] < 5000000) | (rcn['price_m2'].isna())]
                
                all_transactions.append(rcn)
            except Exception as e:
                print(f"    [ERR RCN] {city}: {e}")

    if all_stops:
        stops_combined = gpd.pd.concat(all_stops)
        print(f"\n  Consolidating {len(stops_combined)} Stops...")
        stops_combined.to_file(master_db, driver="GPKG", layer="stops")
        
    if all_transactions:
        final_rcn = gpd.pd.concat(all_transactions)
        print(f"  Consolidating {len(final_rcn)} RAW records...")
        final_rcn.to_file(master_db, driver="GPKG", layer="transactions")
        
    print(f"\nSUCCESS: Full Spectrum Analytical Database Restored in {master_db}")

if __name__ == "__main__":
    restore_full_data()
