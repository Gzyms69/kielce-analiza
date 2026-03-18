import subprocess
import concurrent.futures
from pathlib import Path
import time

CITIES_ROOT = Path("data/cities")
MAX_THREADS = 4 # 4 wątki dla bezpieczeństwa RAM podczas precyzyjnego cięcia

def convert_city(city_dir):
    city_name = city_dir.name
    pbf_file = city_dir / "osm_bbox.pbf"
    output_gpkg = city_dir / "osm_full.gpkg"
    zone_file = city_dir / "transport_zone.gpkg"
    
    if not pbf_file.exists(): return None
    if output_gpkg.exists(): output_gpkg.unlink() # Wymuszenie czystego startu
    
    start_time = time.time()
    try:
        # Precyzyjne docięcie (-clipsrc) na już małym pliku PBF
        subprocess.run([
            "ogr2ogr", "-f", "GPKG", str(output_gpkg), str(pbf_file),
            "-oo", "CONFIG_FILE=scripts/core/osmconf.ini",
            "-gt", "65536", "-nlt", "PROMOTE_TO_MULTI",
            "-clipsrc", str(zone_file),
            "--config", "OSM_USE_CUSTOM_INDEXING", "NO"
        ], check=True, capture_output=True)
        
        duration = time.time() - start_time
        size_mb = output_gpkg.stat().st_size / (1024 * 1024)
        
        # Opcjonalne usunięcie tymczasowego kwadratu
        pbf_file.unlink() 
        
        return f"[OK] {city_name.ljust(15)} | {duration:4.1f} s | {size_mb:6.1f} MB | Skalpel precyzyjny"
    except subprocess.CalledProcessError as e:
        return f"[ERR] {city_name}: {e.stderr.decode()}"
    except Exception as e:
        return f"[ERR] {city_name}: {e}"

def main():
    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    print(f"Uruchamiam precyzyjny Skalpel GDAL (Wątki: {MAX_THREADS})...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        results = list(executor.map(convert_city, cities))
        for r in filter(None, results):
            print(r)

if __name__ == "__main__":
    main()
