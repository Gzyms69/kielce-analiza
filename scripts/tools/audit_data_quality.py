import geopandas as gpd
import pandas as pd
from pathlib import Path
import os

CITIES_ROOT = Path("data/cities")
POP_PATH = Path("data/poland/population/nsp2021_grid250m.gpkg")
REPORT_PATH = Path("reports/ultimate_national_audit.txt")

def get_file_info(path):
    if not path.exists(): return "MISSING", None, []
    try:
        gdf = gpd.read_file(path, rows=5) # Tylko nagłówek dla szybkości
        return "OK", str(gdf.crs), gdf.columns.tolist()
    except Exception as e:
        return f"ERROR ({e})", None, []

def audit_city(city_name):
    print(f"  Auditing {city_name}...")
    city_dir = CITIES_ROOT / city_name
    stops_path = city_dir / "smart_stops.gpkg"
    rcn_path = city_dir / "rcn" / "transactions.gpkg"
    osm_path = city_dir / "osm_full.gpkg"
    
    res = [f"CITY: {city_name.upper()}", "="*40]
    
    # 1. Stops Audit
    status, crs, cols = get_file_info(stops_path)
    res.append(f"[STOPS] Status: {status}")
    if status == "OK":
        res.append(f"  - CRS: {crs}")
        res.append(f"  - Columns: {cols}")
        count = len(gpd.read_file(stops_path))
        res.append(f"  - Total Count: {count}")

    # 2. RCN Audit
    status, crs, cols = get_file_info(rcn_path)
    res.append(f"[RCN] Status: {status}")
    if status == "OK":
        res.append(f"  - CRS: {crs}")
        res.append(f"  - Columns: {cols}")
        rcn = gpd.read_file(rcn_path)
        rcn['dok_dt'] = pd.to_datetime(rcn['dok_data'], utc=True, errors='coerce')
        fresh = rcn[rcn['dok_dt'] >= '2025-01-01']
        res.append(f"  - Total (2025+): {len(fresh)}")
        if 'price_m2' in cols or 'tran_cena_brutto' in cols:
            p_col = 'price_m2' if 'price_m2' in cols else 'tran_cena_brutto'
            prices = pd.to_numeric(rcn[p_col], errors='coerce').dropna()
            res.append(f"  - Price Stats ({p_col}): Med={prices.median():.0f}, Min={prices.min():.0f}, Max={prices.max():.0f}")

    # 3. OSM Audit
    status, crs, cols = get_file_info(osm_path)
    res.append(f"[OSM] Status: {status}")
    if status == "OK":
        res.append(f"  - CRS: {crs}")
        # OSM files are huge, so we just check if it's readable
        res.append(f"  - Layers: Found osm_full.gpkg")

    # 4. Population Alignment (Spatial Check)
    if stops_path.exists() and POP_PATH.exists():
        try:
            stops = gpd.read_file(stops_path).to_crs("EPSG:2180")
            pop_meta = gpd.read_file(POP_PATH, rows=1)
            res.append(f"[POPULATION] Status: OK")
            res.append(f"  - National Grid CRS: {pop_meta.crs}")
            # Check if grid covers stop BBOX
            bounds = stops.total_bounds
            res.append(f"  - City Bounds (2180): {bounds}")
        except:
            res.append("[POPULATION] Error reading grid")
    
    res.append("\n")
    return "\n".join(res)

def run_ultimate_audit():
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    cities = sorted([d.name for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    with open(REPORT_PATH, "w") as f:
        f.write("ULTIMATE NATIONAL DATA AUDIT & COORDINATE VERIFICATION 2026\n")
        f.write("PROJECT STANDARD CRS: EPSG:2180 (Poland 1992)\n")
        f.write("-" * 60 + "\n\n")
        
        for city in cities:
            f.write(audit_city(city))
            
    print(f"\nAudit complete: {REPORT_PATH}")

if __name__ == "__main__":
    run_ultimate_audit()
