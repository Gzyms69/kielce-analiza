import subprocess
import geopandas as gpd
from pathlib import Path
import time
import os

PBF_SOURCE = Path("data/poland/osm/poland-latest.osm.pbf")
CITIES_ROOT = Path("data/cities")
OSMCONF = Path("scripts/core/osmconf.ini")

def extract_city_safe(city_dir):
    city_name = city_dir.name
    zone_file = city_dir / "transport_zone.gpkg"
    bbox_pbf = city_dir / "osm_bbox.pbf"
    output_gpkg = city_dir / "osm_full.gpkg"
    
    if not zone_file.exists():
        print(f"[SKIP] {city_name}: Brak wykrojnika")
        return
        
    print(f"\n--- Przetwarzanie: {city_name.upper()} ---")
    start_time = time.time()
    
    # 1. Pobranie prostego prostokąta (BBOX)
    gdf = gpd.read_file(zone_file)
    minx, miny, maxx, maxy = gdf.total_bounds
    bbox_str = f"{minx},{miny},{maxx},{maxy}"
    
    # 2. OSMIUM: Szybkie cięcie BBOX (zero złożoności geometrycznej)
    if not bbox_pbf.exists():
        print(f"  [1/2] Osmium BBOX extract...")
        try:
            subprocess.run([
                "osmium", "extract",
                "-b", bbox_str,
                str(PBF_SOURCE),
                "-o", str(bbox_pbf),
                "--overwrite"
            ], check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            print(f"  [ERR] Osmium: {e.stderr.decode()}")
            return
            
    # 3. OGR2OGR: Prosta konwersja (BEZ -clipsrc)
    if not output_gpkg.exists():
        print(f"  [2/2] OGR2OGR konwersja (Bez wycinania geometrycznego)...")
        try:
            # Wymuszenie zapisu temp w bieżącym katalogu, a nie w RAM (/tmp)
            os.environ["CPL_TMPDIR"] = str(city_dir) 
            
            subprocess.run([
                "ogr2ogr", "-f", "GPKG", str(output_gpkg), str(bbox_pbf),
                "-oo", f"CONFIG_FILE={OSMCONF}",
                "-gt", "65536", "-nlt", "PROMOTE_TO_MULTI",
                "--config", "OSM_USE_CUSTOM_INDEXING", "NO"
            ], check=True, capture_output=True)
            
            # Sprzątanie PBF po udanej konwersji
            bbox_pbf.unlink()
            
        except subprocess.CalledProcessError as e:
            print(f"  [ERR] OGR2OGR: {e.stderr.decode()}")
            return
            
    duration = time.time() - start_time
    size = output_gpkg.stat().st_size / (1024*1024) if output_gpkg.exists() else 0
    print(f"  [OK] Zakończono w {duration:.1f}s. Rozmiar: {size:.1f} MB")

def main():
    print("=== BEZPIECZNA EKSTRAKCJA OSM (Low-RAM, Sequential) ===")
    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    for city_dir in cities:
        extract_city_safe(city_dir)

if __name__ == "__main__":
    main()
