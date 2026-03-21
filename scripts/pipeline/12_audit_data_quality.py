import geopandas as gpd
import pandas as pd
from pathlib import Path
import os
import argparse
import json

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def get_file_info(path):
    if not path.exists(): return "MISSING", None, []
    try:
        gdf = gpd.read_file(path, rows=5) 
        return "OK", str(gdf.crs), gdf.columns.tolist()
    except Exception as e:
        return f"ERROR ({e})", None, []

def audit_city(city_name, data_dir):
    city_dir = data_dir / "cities" / city_name
    
    stops_path = city_dir / "02_spatial" / "stops.gpkg"
    rcn_path = city_dir / "02_spatial" / "transactions.gpkg"
    osm_path = city_dir / "02_spatial" / "infrastructure.gpkg"
    
    issues = []
    
    s_stat, s_crs, s_cols = get_file_info(stops_path)
    if s_stat != "OK": issues.append("STOPS: Missing")
    
    r_stat, r_crs, r_cols = get_file_info(rcn_path)
    if r_stat != "OK": issues.append("RCN: Missing")
    
    o_stat, o_crs, o_cols = get_file_info(osm_path)
    if o_stat != "OK": issues.append("OSM: Missing")

    metrics = {
        "city": city_name,
        "status": "FAILED" if issues else "PASSED",
        "issues": len(issues)
    }
    
    if issues:
        print(f"  [!] Błędy dla {city_name}: {', '.join(issues)}")
    else:
        pass # All good
        
    print(f"__PIPELINE_METRICS__={json.dumps(metrics)}")
    return not issues

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", help="Miasto do audytu", required=True)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    data_dir = get_data_dir()
    audit_city(args.city, data_dir)

if __name__ == "__main__":
    main()
