import geopandas as gpd
import pandas as pd
from pathlib import Path
import sqlite3
import os

CITIES_ROOT = Path("data/cities")
REPORT_PATH = Path("reports/national_data_audit_2026.txt")

def audit_city(city_name):
    report = []
    report.append(f"CITY: {city_name.upper()}")
    report.append("-" * 30)
    
    city_dir = CITIES_ROOT / city_name
    stops_path = city_dir / "smart_stops.gpkg"
    rcn_path = city_dir / "rcn" / "transactions.gpkg"
    osm_path = city_dir / "osm_full.gpkg" # Corrected name
    
    # 1. Stops Check
    if stops_path.exists():
        try:
            stops = gpd.read_file(stops_path)
            report.append(f"  [STOPS] Total: {len(stops)}")
            report.append(f"  [STOPS] CRS: {stops.crs}")
        except Exception as e:
            report.append(f"  [STOPS] ERROR: {e}")
    else:
        report.append("  [STOPS] MISSING!")

    # 2. RCN Check
    if rcn_path.exists():
        try:
            rcn = gpd.read_file(rcn_path)
            if 'dok_data' in rcn.columns:
                rcn['dok_dt'] = pd.to_datetime(rcn['dok_data'], utc=True, errors='coerce')
                rcn_2025 = rcn[rcn['dok_dt'] >= '2025-01-01']
                report.append(f"  [RCN] Total Verified (2025+): {len(rcn_2025)}")
                if not rcn_2025.empty:
                    report.append(f"  [RCN] Date Range: {rcn_2025['dok_dt'].min().date()} to {rcn_2025['dok_dt'].max().date()}")
            
            # Price Stats
            if 'tran_cena_brutto' in rcn.columns:
                prices = pd.to_numeric(rcn['tran_cena_brutto'], errors='coerce').dropna()
                if not prices.empty:
                    report.append(f"  [RCN] Price Stats: Min={prices.min():.0f}, Max={prices.max():.0f}, Median={prices.median():.0f}")
            
            # Coverage Test
            if stops_path.exists() and not rcn_2025.empty:
                stops_2180 = stops.to_crs("EPSG:2180")
                rcn_2180 = rcn_2025.to_crs("EPSG:2180")
                stops_buffer = stops_2180.copy()
                stops_buffer['geometry'] = stops_buffer.geometry.buffer(1500)
                
                covered_stops = gpd.sjoin(stops_buffer, rcn_2180, how="inner", predicate="intersects")
                unique_covered = covered_stops.index.unique().shape[0]
                coverage_pct = (unique_covered / len(stops)) * 100
                report.append(f"  [COVERAGE] Stops within 1500m of RCN: {unique_covered} ({coverage_pct:.2f}%)")

        except Exception as e:
            report.append(f"  [RCN] ERROR: {e}")
    else:
        report.append("  [RCN] MISSING!")

    # 3. OSM Check
    if osm_path.exists():
        report.append(f"  [OSM] Found: {osm_path.name}")
    else:
        report.append("  [OSM] MISSING!")

    report.append("\n")
    return "\n".join(report)

def run_total_audit():
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    cities = sorted([d.name for d in CITIES_ROOT.iterdir() if d.is_dir()])
    with open(REPORT_PATH, "w") as f:
        f.write("COMPREHENSIVE DATA INTEGRITY REPORT 2026\n")
        f.write("=" * 40 + "\n\n")
        for city in cities:
            f.write(audit_city(city))
    print(f"Audit saved to: {REPORT_PATH}")

if __name__ == "__main__":
    run_total_audit()
