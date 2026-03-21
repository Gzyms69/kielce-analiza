import geopandas as gpd
import pandas as pd
from pathlib import Path
import os
import argparse
import json
import sys
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", message=".*Geometry is in a geographic CRS.*")

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def restore_full_data(data_dir):
    master_db = data_dir / "database" / "master_analytical.gpkg"
    tmp_db = data_dir / "database" / "master_analytical.tmp.gpkg"
    
    master_db.parent.mkdir(parents=True, exist_ok=True)
    
    # Atomic write: budujemy do pliku tymczasowego, potem rename
    if tmp_db.exists():
        os.remove(tmp_db)
    
    cities_root = data_dir / "cities"
    cities = sorted([d.name for d in cities_root.iterdir() if d.is_dir() and d.name != 'rail'])
    
    metrics = {"step": "11"}
    total_stops = 0
    total_rcn = 0
    
    # STREAMING: Zamiast ladowac wszystko do RAM, dopisujemy miasto po miescie
    for city in cities:
        city_dir = cities_root / city
        stops_path = city_dir / "02_spatial" / "stops.gpkg"
        rcn_path = city_dir / "02_spatial" / "transactions.gpkg"
        
        if stops_path.exists():
            try:
                stops = gpd.read_file(stops_path).to_crs("EPSG:2180")
                stops['city'] = city
                mode = 'a' if tmp_db.exists() else 'w'
                stops.to_file(tmp_db, driver="GPKG", layer="stops", mode=mode)
                total_stops += len(stops)
                del stops  # Jawne zwolnienie RAM
            except Exception as e:
                print(f"  [CRITICAL] Failed to load stops for {city}: {e}", file=sys.stderr)
            
        if rcn_path.exists():
            try:
                rcn = gpd.read_file(rcn_path).to_crs("EPSG:2180")
                rcn['city'] = city
                mode = 'a' if tmp_db.exists() else 'w'
                rcn.to_file(tmp_db, driver="GPKG", layer="transactions", mode=mode)
                total_rcn += len(rcn)
                del rcn  # Jawne zwolnienie RAM
            except Exception as e:
                print(f"  [CRITICAL] Failed to load RCN for {city}: {e}", file=sys.stderr)

    # Atomic swap
    if tmp_db.exists():
        os.replace(tmp_db, master_db)
    
    metrics['total_stops'] = total_stops
    metrics['total_rcn'] = total_rcn
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
