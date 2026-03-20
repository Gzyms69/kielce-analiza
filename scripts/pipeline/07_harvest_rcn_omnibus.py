import os
import json
import subprocess
import time
import requests
import zipfile
import io
from pathlib import Path
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

WFS_URL = "https://mapy.geoportal.gov.pl/wss/service/rcn"
DATE_START = "2025-01-01"

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def download_zip_and_extract(url, target_dir):
    try:
        target_dir = Path(target_dir).resolve()
        r = requests.get(url, stream=True, timeout=120, verify=False)
        r.raise_for_status()
        with zipfile.ZipFile(io.BytesIO(r.content)) as z:
            z.extractall(target_dir)
            
        # Flatten structure
        to_move = []
        for root, dirs, files in os.walk(target_dir):
            for file in files:
                if any(file.lower().endswith(ext) for ext in [".gml", ".xml", ".shp", ".dbf", ".shx"]):
                    source = Path(root) / file
                    destination = target_dir / file
                    if source.resolve() != destination.resolve():
                        to_move.append((source, destination))
        
        for src, dst in to_move:
            if dst.exists(): os.remove(dst)
            import shutil
            shutil.move(str(src), str(dst))
        return True
    except Exception as e:
        print(f"    [ERR ZIP] {url}: {e}")
        return False

def harvest_single_teryt(teryt, cache_dir):
    """Pobiera jeden powiat do cache, jeśli go tam nie ma."""
    gml_path = cache_dir / f"{teryt}.gml"
    if gml_path.exists() and gml_path.stat().st_size > 1000:
        return True

    print(f"  [WFS] Pobieranie powiatu {teryt}...", flush=True)
    where_clause = f"teryt LIKE '{teryt}%' AND dok_data >= '{DATE_START}'"
    
    try:
        temp_gpkg = cache_dir / f"temp_{teryt}.gpkg"
        if temp_gpkg.exists(): os.remove(temp_gpkg)
        
        subprocess.run([
            "ogr2ogr", "-progress", "-f", "GPKG", str(temp_gpkg),
            f"WFS:{WFS_URL}", "ms:lokale",
            "-where", where_clause,
            "-nln", "transactions",
            "--config", "GDAL_HTTP_TIMEOUT", "60",
            "--config", "OGR_WFS_PAGING_ALLOWED", "YES",
            "--config", "OGR_WFS_PAGE_SIZE", "2000"
        ], check=True)
        
        if temp_gpkg.exists():
            print(f"    [OK] Pobrano {teryt}. Archwizacja w cache...", flush=True)
            subprocess.run([
                "ogr2ogr", "-f", "GML", str(gml_path), str(temp_gpkg)
            ], check=True)
            os.remove(temp_gpkg)
            return True
    except:
        print(f"    [FALLBACK] Brak w WFS {teryt}. Szukanie OpenData...", flush=True)
        opendata_url = f"https://opendata.geoportal.gov.pl/rcn/{teryt}.zip"
        return download_zip_and_extract(opendata_url, cache_dir)
    
    return False

def main():
    data_dir = get_data_dir()
    cache_dir = data_dir / "poland" / "rcn_cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    cities_root = data_dir / "cities"
    if not cities_root.exists(): return

    print("=== AGREGACJA CELÓW RCN (Inteligentny Cache) ===", flush=True)
    all_targets = set()
    city_map = {} 
    
    for city_dir in sorted(cities_root.iterdir()):
        if not city_dir.is_dir(): continue
        target_file = city_dir / "rcn_targets.json"
        if target_file.exists():
            with open(target_file, "r") as f:
                t_list = json.load(f)
                city_map[city_dir.name] = t_list
                all_targets.update(t_list)

    all_targets = sorted(list(all_targets))
    print(f"Zidentyfikowano {len(all_targets)} unikalnych powiatów dla {len(city_map)} miast.", flush=True)

    for i, teryt in enumerate(all_targets):
        if len(teryt) != 4: continue
        print(f"[{i+1}/{len(all_targets)}] Przetwarzanie: {teryt}", flush=True)
        harvest_single_teryt(teryt, cache_dir)

    print("\n=== DYSTRYBUCJA DANYCH DO HUBÓW ===", flush=True)
    for city, teryts in city_map.items():
        print(f"  Budowanie bazy dla: {city}...", flush=True)
        spatial_dir = data_dir / "cities" / city / "02_spatial"
        spatial_dir.mkdir(parents=True, exist_ok=True)
        out_gpkg = spatial_dir / "transactions.gpkg"
        
        if out_gpkg.exists(): os.remove(out_gpkg)
        
        for t in teryts:
            cache_gml = cache_dir / f"{t}.gml"
            if cache_gml.exists():
                subprocess.run([
                    "ogr2ogr", "-f", "GPKG", "-update", "-append",
                    str(out_gpkg), str(cache_gml),
                    "-nln", "transactions"
                ])
        
        if out_gpkg.exists():
            print(f"    [SUCCESS] Baza {city} gotowa.", flush=True)

if __name__ == "__main__":
    main()
