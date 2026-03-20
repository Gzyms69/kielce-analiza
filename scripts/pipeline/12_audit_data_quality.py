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

def get_file_info(path):
    if not path.exists(): return "MISSING", None, []
    try:
        gdf = gpd.read_file(path, rows=5) 
        return "OK", str(gdf.crs), gdf.columns.tolist()
    except Exception as e:
        return f"ERROR ({e})", None, []

def audit_city(city_name, data_dir):
    print(f"  Auditing {city_name}...")
    city_dir = data_dir / "cities" / city_name
    
    # Obsługa obu lokalizacji, na wypadek gdyby audyt był odpalony po kroku 13
    stops_path = city_dir / "02_spatial" / "stops.gpkg"
    if not stops_path.exists(): stops_path = city_dir / "smart_stops.gpkg"
        
    rcn_path = city_dir / "02_spatial" / "transactions.gpkg"
    if not rcn_path.exists(): rcn_path = city_dir / "rcn" / "transactions.gpkg"
        
    osm_path = city_dir / "02_spatial" / "infrastructure.gpkg"
    if not osm_path.exists(): osm_path = city_dir / "osm_full.gpkg"
    if not osm_path.exists(): osm_path = city_dir / "infrastructure.gpkg"
    
    issues = []
    
    # 1. Stops Audit
    status, crs, cols = get_file_info(stops_path)
    if status != "OK":
        issues.append("STOPS: Missing or corrupted")
    elif "2180" not in crs and "4326" not in crs:
        issues.append(f"STOPS: Unknown CRS ({crs})")

    # 2. RCN Audit
    status, crs, cols = get_file_info(rcn_path)
    if status != "OK":
        issues.append("RCN: Missing or corrupted")
    else:
        try:
            rcn = gpd.read_file(rcn_path)
            prices = pd.to_numeric(rcn['price_m2'], errors='coerce').dropna()
            if prices.empty:
                issues.append("RCN: No valid numerical price_m2 data")
            elif len(rcn) < 10:
                issues.append("RCN: Critically low number of transactions (<10)")
        except:
            issues.append("RCN: Failed to parse price_m2")

    # 3. OSM Audit
    status, crs, cols = get_file_info(osm_path)
    if status != "OK":
        issues.append("OSM: Missing or corrupted")

    if issues:
        print(f"    [!] FAILED QUALITY GATE for {city_name}:")
        for i in issues: print(f"        - {i}")
        return False
        
    print(f"    [+] PASSED QUALITY GATE for {city_name}.")
    return True

def run_quality_gate():
    print("=== TASK 1.9: PRE-FLIGHT QUALITY GATE (Audit) ===\n")
    data_dir = get_data_dir()
    cities_root = data_dir / "cities"
    allowed_cities = get_allowed_cities()
    
    if not cities_root.exists(): return
    
    cities = sorted([d.name for d in cities_root.iterdir() if d.is_dir()])
    
    failed_cities = []
    for city in cities:
        if allowed_cities and city not in allowed_cities:
            continue
        success = audit_city(city, data_dir)
        if not success:
            failed_cities.append(city)
            
    if failed_cities:
        print(f"\n[CRITICAL] Quality Gate failed for: {', '.join(failed_cities)}")
        # Zatrzymujemy cały pipeline, bo błędy są zbyt poważne by wejść w fazę 13/14
        sys.exit(1)
    else:
        print("\n[SUCCESS] All targeted cities passed the Quality Gate.")

if __name__ == "__main__":
    run_quality_gate()