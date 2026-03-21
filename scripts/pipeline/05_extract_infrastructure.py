import os
import json
import subprocess
import concurrent.futures
from pathlib import Path
import geopandas as gpd
import time
import sys
import argparse

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def get_allowed_cities():
    cities_env = os.environ.get("PIPELINE_CITIES")
    if cities_env:
        return [c.strip() for c in cities_env.split(',')]
    return None

def get_worker_limit():
    # KRYTYCZNA POPRAWKA: Wymuszamy 2 wątki dla Osmium (kompromis RAM/Szybkość).
    return 2

def run_osmium_and_ogr(city_name, data_dir, pbf_source, force):
    """Wykonuje precyzyjne cięcie i konwersję (Twoja oryginalna metoda Turbo)."""
    city_dir = data_dir / "cities" / city_name
    spatial_dir = city_dir / "02_spatial"
    zone_file = city_dir / "transport_zone.gpkg"
    output_gpkg = spatial_dir / "infrastructure.gpkg"
    temp_pbf = spatial_dir / "temp_extract.pbf"
    temp_geojson = spatial_dir / "zone.geojson"
    
    if output_gpkg.exists() and not force:
        return True, city_name, "CACHED"

    try:
        # 1. Przygotowanie wykrojnika GeoJSON (wymagane przez Osmium)
        spatial_dir.mkdir(parents=True, exist_ok=True)
        gdf = gpd.read_file(zone_file)
        gdf.to_file(temp_geojson, driver='GeoJSON')
        
        # 2. OSMIUM: Najszybsze cięcie poligonem (Twój wzorzec z archiwum)
        print(f"[{city_name}] OSMIUM: Wycinanie poligonem...", flush=True)
        result = subprocess.run([
            "osmium", "extract", "-p", str(temp_geojson),
            str(pbf_source), "-o", str(temp_pbf), "--overwrite"
        ], check=True, capture_output=True, text=True)
        if result.stderr:
            print(f"[{city_name}] OSMIUM stderr: {result.stderr.strip()}", flush=True)
        
        # 3. OGR2OGR: Błyskawiczna konwersja gotowego wycinka
        osmconf = Path("config/osmconf.ini")
        os.environ["OSM_CONFIG_FILE"] = str(osmconf)
        print(f"[{city_name}] OGR2OGR: Konwersja do GPKG...", flush=True)
        result = subprocess.run([
            "ogr2ogr", "-f", "GPKG", str(output_gpkg), str(temp_pbf),
            "-gt", "65536", "-nlt", "PROMOTE_TO_MULTI",
            "-dim", "XY", "-lco", "GEOMETRY_NAME=geometry", "-skipfailures",
            "--config", "OGR_SQLITE_SYNCHRONOUS", "OFF",
            "--config", "OSM_USE_CUSTOM_INDEXING", "NO"
        ], check=True, capture_output=True, text=True)
        if result.stderr:
            err_text = result.stderr.strip()
            # OGR2OGR spamuje milionami linijek warningów z OSM o otwartych poligonach
            if "Non closed ring detected" not in err_text:
                print(f"[{city_name}] OGR2OGR stderr: {err_text}", flush=True)
        
        # --- AUDYT DANYCH ---
        pts = gpd.read_file(output_gpkg, layer="points")
        polys = gpd.read_file(output_gpkg, layer="multipolygons")
        print(f"[{city_name}] WYNIK: POI={len(pts)}, Budynki={len(polys)}", flush=True)
        
        # Sprzątanie
        for f in [temp_pbf, temp_geojson]:
            if f.exists(): f.unlink()
            
        return True, city_name, {"poi": len(pts), "poly": len(polys)}
    except Exception as e:
        print(f"[{city_name}] BŁĄD: {e}", flush=True)
        return False, city_name, str(e)

def extract_all(force=False):
    print("\n=== TURBO OSM EXTRACTION 3.0 (BACK TO ARCHIVE PATTERN) ===", flush=True)
    data_dir = get_data_dir()
    pbf_source = data_dir / "poland" / "osm" / "poland-latest.osm.pbf"
    cities_root = data_dir / "cities"
    
    allowed_cities = get_allowed_cities()
    cities_to_process = []
    
    for city_dir in sorted(cities_root.iterdir()):
        if not city_dir.is_dir() or city_dir.name == 'rail': continue
        if allowed_cities and city_dir.name not in allowed_cities: continue
        if (city_dir / "transport_zone.gpkg").exists():
            cities_to_process.append(city_dir.name)

    start_time = time.time()
    success_count = 0
    # Osmium i OGR2OGR są na tyle szybkie przy małych wycinkach, że możemy jechać równolegle (limit 2-3)
    with concurrent.futures.ThreadPoolExecutor(max_workers=get_worker_limit()) as executor:
        futures = [executor.submit(run_osmium_and_ogr, c, data_dir, pbf_source, force) for c in cities_to_process]
        for future in concurrent.futures.as_completed(futures):
            ok, name, res = future.result()
            if ok: success_count += 1

    duration = int(time.time() - start_time)
    print(f"\nAnaliza OSM ukończona w {duration}s.", flush=True)
    print(f"__PIPELINE_METRICS__={json.dumps({'step': '05', 'success': success_count, 'time_s': duration})}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    extract_all(force=args.force)

if __name__ == "__main__":
    main()
