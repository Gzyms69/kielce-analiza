import geopandas as gpd
import pandas as pd
from pathlib import Path
import os
import argparse
import json
import sys
import warnings

warnings.filterwarnings("ignore")

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def restore_full_data(data_dir):
    master_db = data_dir / "database" / "master_analytical.gpkg"
    
    if master_db.exists():
        os.remove(master_db)
        
    master_db.parent.mkdir(parents=True, exist_ok=True)
    cities_root = data_dir / "cities"
    
    cities = sorted([d.name for d in cities_root.iterdir() if d.is_dir() and d.name != 'rail'])
    
    all_stops = []
    all_transactions = []
    
    for city in cities:
        city_dir = cities_root / city
        stops_path = city_dir / "02_spatial" / "stops.gpkg"
        rcn_path = city_dir / "02_spatial" / "transactions.gpkg"
        
        if stops_path.exists():
            try:
                stops = gpd.read_file(stops_path).to_crs("EPSG:2180")
                stops['city'] = city
                all_stops.append(stops)
            except Exception as e:
                print(f"  [CRITICAL] Failed to load stops for {city}: {e}", file=sys.stderr)
            
        if rcn_path.exists():
            try:
                rcn = gpd.read_file(rcn_path).to_crs("EPSG:2180")
                rcn['city'] = city
                all_transactions.append(rcn)
            except Exception as e:
                print(f"  [CRITICAL] Failed to load RCN for {city}: {e}", file=sys.stderr)

    metrics = {"step": "11"}

    if all_stops:
        stops_combined = pd.concat(all_stops, ignore_index=True)
        stops_combined.to_file(master_db, driver="GPKG", layer="stops")
        metrics['total_stops'] = len(stops_combined)
        
    if all_transactions:
        final_rcn = pd.concat(all_transactions, ignore_index=True)
        final_rcn.to_file(master_db, driver="GPKG", layer="transactions")
        metrics['total_rcn'] = len(final_rcn)

    print(f"__PIPELINE_METRICS__={json.dumps(metrics)}")
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    data_dir = get_data_dir()
    restore_full_data(data_dir)

if __name__ == "__main__":
    main()
