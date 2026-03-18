import os
import pandas as pd
import geopandas as gpd
from pathlib import Path

CITIES_ROOT = Path("data/cities")

def run_audit():
    print("Rozpoczynam Totalny Audyt Danych (100% Coverage Check)...")
    report = []

    for city_dir in sorted(CITIES_ROOT.iterdir()):
        if not city_dir.is_dir(): continue
        
        city = city_dir.name
        status = {"city": city}
        
        # 1. Sprawdzenie GTFS
        gtfs_dir = city_dir / "gtfs"
        stops_files = list(gtfs_dir.rglob("stops.txt"))
        status["gtfs_files_count"] = len(stops_files)
        status["has_gtfs"] = len(stops_files) > 0
        
        # 2. Sprawdzenie OSM
        osm_file = city_dir / "osm_full.gpkg"
        status["has_osm"] = osm_file.exists()
        if osm_file.exists():
            status["osm_size_mb"] = round(osm_file.stat().st_size / (1024*1024), 2)
        else:
            status["osm_size_mb"] = 0

        # 3. Sprawdzenie RCN
        rcn_dir = city_dir / "rcn"
        rcn_files = list(rcn_dir.glob("*.gml"))
        status["has_rcn"] = len(rcn_files) > 0
        if rcn_files:
            status["rcn_size_mb"] = round(sum(f.stat().st_size for f in rcn_files) / (1024*1024), 2)
        else:
            status["rcn_size_mb"] = 0
            
        # 4. Sprawdzenie Wykrojnika
        status["has_zone"] = (city_dir / "transport_zone.gpkg").exists()

        report.append(status)

    df = pd.DataFrame(report)
    output_path = "reports/final_audit_report.csv"
    df.to_csv(output_path, index=False)
    
    print("\n=== WYNIKI AUDYTU (TOP 10) ===")
    print(df.head(10).to_string())
    
    missing_rcn = df[~df['has_rcn']]['city'].tolist()
    missing_osm = df[~df['has_osm']]['city'].tolist()
    
    print(f"\nAlerty braków:")
    print(f"  - Brak RCN w {len(missing_rcn)} miastach: {missing_rcn}")
    print(f"  - Brak OSM w {len(missing_osm)} miastach: {missing_osm}")
    
    return df

if __name__ == "__main__":
    run_audit()
