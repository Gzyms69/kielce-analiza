import os
import json
import time
import subprocess
from pathlib import Path
import argparse
import concurrent.futures

# --- KONFIGURACJA OSTATECZNA (V8.5 - SMART CACHE WFS) ---
WFS_URL = "https://mapy.geoportal.gov.pl/wss/service/rcn"
DATE_START = "2020-01-01"
PAGE_SIZE = 5000
MAX_WORKERS = 3

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def get_allowed_cities():
    cities_env = os.environ.get("PIPELINE_CITIES")
    if cities_env:
        return [c.strip() for c in cities_env.split(',')]
    return None

def download_wfs(teryt, cache_dir):
    gml_path = cache_dir / f"{teryt}.gml"
    meta_path = cache_dir / f"{teryt}.meta"
    
    # SMART CACHE LOGIC
    use_cache = False
    if gml_path.exists() and gml_path.stat().st_size > 5000:
        if meta_path.exists():
            try:
                with open(meta_path, 'r') as f:
                    meta = json.load(f)
                # Używamy cache tylko wtedy, gdy zawiera dane równie stare lub starsze niż żądamy
                if meta.get("date_start", "2099-01-01") <= DATE_START:
                    use_cache = True
            except:
                pass
                
    if use_cache:
        print(f"  [CACHE] {teryt} OK. Zgodny z zakresem >= {DATE_START}.", flush=True)
        return "CACHE"
        
    where_clause = f"teryt LIKE '{teryt}%' AND dok_data >= '{DATE_START}'"
    print(f"  [WFS-START] {teryt}: Pobieranie od {DATE_START}...", flush=True)
    
    for attempt in range(3):
        try:
            temp_gpkg = cache_dir / f"temp_{teryt}.gpkg"
            if temp_gpkg.exists(): temp_gpkg.unlink()
            
            cmd = [
                "ogr2ogr", "-f", "GPKG", str(temp_gpkg),
                f"WFS:{WFS_URL}", "ms:lokale",
                "-where", where_clause,
                "-nln", "transactions",
                "--config", "GDAL_HTTP_TIMEOUT", "120",
                "--config", "OGR_WFS_PAGING_ALLOWED", "YES",
                "--config", "OGR_WFS_PAGE_SIZE", str(PAGE_SIZE)
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0 and temp_gpkg.exists():
                print(f"    [WFS-OK] {teryt}: Sukces. Zapisywanie z metadanymi...", flush=True)
                subprocess.run(["ogr2ogr", "-f", "GML", str(gml_path), str(temp_gpkg)], capture_output=True)
                temp_gpkg.unlink()
                
                # ZAPIS METADANYCH DO SMART CACHE
                with open(meta_path, 'w') as f:
                    json.dump({"date_start": DATE_START, "timestamp": time.time()}, f)
                    
                time.sleep(2)
                return "WFS"
            else:
                err_msg = result.stderr.strip()[:100] if result.stderr else "Błąd OGR."
                print(f"    [WFS-RETRY] {teryt} ({attempt+1}/3): {err_msg}", flush=True)
                time.sleep(5)
                
        except Exception as e:
            print(f"    [WFS-ERR] {teryt}: {str(e)[:100]}", flush=True)
            time.sleep(5)
            
    print(f"  [FATAL] {teryt} porzucony po 3 próbach!", flush=True)
    return "FAIL"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    data_dir = get_data_dir()
    cache_dir = data_dir / "poland" / "rcn_cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    allowed_cities = get_allowed_cities()
    cities_root = data_dir / "cities"
    
    all_targets = set()
    city_map = {}
    
    for city_dir in sorted(cities_root.iterdir()):
        if not city_dir.is_dir() or city_dir.name == 'rail': continue
        if allowed_cities and city_dir.name not in allowed_cities: continue
        
        target_file = city_dir / "rcn_targets.json"
        if target_file.exists():
            with open(target_file, "r") as f:
                t_list = json.load(f)
                city_map[city_dir.name] = t_list
                all_targets.update(t_list)

    print(f"=== SMART WFS HARVESTER v8.5 (PARALLEL: {MAX_WORKERS}) ===", flush=True)
    print(f"Żądany zakres danych: >= {DATE_START}", flush=True)
    print(f"Unikalnych powiatów: {len(all_targets)}", flush=True)

    stats = {"WFS": 0, "CACHE": 0, "FAIL": 0}
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(download_wfs, t, cache_dir): t for t in sorted([x for x in all_targets if len(x) == 4])}
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            stats[res] += 1
            teryt = futures[future]
            print(f"[WYNIK] {teryt}: {res}", flush=True)

    print(f"\n--- SKŁADANIE BAZ DLA MIAST ---", flush=True)
    for city, teryts in city_map.items():
        spatial_dir = data_dir / "cities" / city / "02_spatial"
        spatial_dir.mkdir(parents=True, exist_ok=True)
        out_gpkg = spatial_dir / "transactions.gpkg"
        
        if out_gpkg.exists() and args.force:
            out_gpkg.unlink()
            
        if not out_gpkg.exists():
            print(f"[{city}] Łączenie {len(teryts)} powiatów...", flush=True)
            for t in teryts:
                cache_gml = cache_dir / f"{t}.gml"
                if cache_gml.exists():
                    subprocess.run([
                        "ogr2ogr", "-f", "GPKG", "-update", "-append",
                        str(out_gpkg), str(cache_gml),
                        "-nln", "transactions",
                        "-where", f"dok_data >= '{DATE_START}'"
                    ], capture_output=True)

        try:
            if out_gpkg.exists():
                import geopandas as gpd
                gdf = gpd.read_file(out_gpkg)
                print(f"[{city}] GOTOWE: {len(gdf)} transakcji.", flush=True)
            else:
                print(f"[{city}] BŁĄD ODCZYTU GPKG.", flush=True)
        except:
            pass

    print(f"__PIPELINE_METRICS__={json.dumps({'step': '07', 'success': stats['WFS']+stats['CACHE'], 'total': len(all_targets)})}", flush=True)

if __name__ == "__main__":
    main()
