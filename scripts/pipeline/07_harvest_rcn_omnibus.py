import os
import json
import time
import requests
from pathlib import Path
import urllib3
import argparse
import concurrent.futures
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

WFS_URL = "https://mapy.geoportal.gov.pl/wss/service/rcn"
DATE_START = "2025-01-01"
PAGE_SIZE = 5000

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def get_allowed_cities():
    cities_env = os.environ.get("PIPELINE_CITIES")
    if cities_env:
        return [c.strip() for c in cities_env.split(',')]
    return None

def fetch_county_wfs(teryt, cache_dir):
    gml_path = cache_dir / f"{teryt}.gml"
    if gml_path.exists() and gml_path.stat().st_size > 1000:
        return True

    print(f"  [WFS] Pobieranie powiatu {teryt}...", flush=True)
    all_content = []
    start_index = 0
    
    while True:
        filter_xml = f"""<ogc:Filter xmlns:ogc='http://www.opengis.net/ogc'>
            <ogc:And>
                <ogc:PropertyIsLike wildCard='*' singleChar='.' escapeChar='!'>
                    <ogc:PropertyName>teryt</ogc:PropertyName>
                    <ogc:Literal>{teryt}*</ogc:Literal>
                </ogc:PropertyIsLike>
                <ogc:PropertyIsGreaterThanOrEqualTo>
                    <ogc:PropertyName>dok_data</ogc:PropertyName>
                    <ogc:Literal>{DATE_START}</ogc:Literal>
                </ogc:PropertyIsGreaterThanOrEqualTo>
            </ogc:And>
        </ogc:Filter>"""

        params = {
            "service": "WFS",
            "version": "1.1.0",
            "request": "GetFeature",
            "typename": "ms:lokale",
            "filter": filter_xml,
            "count": PAGE_SIZE,
            "startIndex": start_index
        }

        try:
            r = requests.get(WFS_URL, params=params, timeout=60, verify=False)
            r.raise_for_status()
            if "<ms:lokale" not in r.text: break
            
            all_content.append(r.text)
            if r.text.count("<ms:lokale") < PAGE_SIZE: break
            start_index += PAGE_SIZE
            time.sleep(0.2)
        except Exception as e:
            print(f"    [ERR] {teryt} at {start_index}: {e}", flush=True)
            return False

    if all_content:
        with open(gml_path, "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?><wfs:FeatureCollection xmlns:wfs="http://www.opengis.net/wfs">')
            for part in all_content:
                body = re.search(r'<wfs:FeatureCollection.*?>(.*)</wfs:FeatureCollection>', part, re.DOTALL)
                if body: f.write(body.group(1))
            f.write('</wfs:FeatureCollection>')
        return True
    return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    data_dir = get_data_dir()
    cache_dir = data_dir / "poland" / "rcn_cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    cities_root = data_dir / "cities"
    allowed_cities = get_allowed_cities()
    
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

    print(f"=== OMNIBUS RCN HARVESTER (v7.6 - STABLE) ===")
    print(f"Aktywne aglomeracje: {list(city_map.keys())}")
    print(f"Unikalnych powiatów do sprawdzenia: {len(all_targets)}")

    success_count = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(fetch_county_wfs, t, cache_dir): t for t in all_targets if len(t) == 4}
        for future in concurrent.futures.as_completed(futures):
            if future.result(): success_count += 1

    import subprocess
    import geopandas as gpd
    for city, teryts in city_map.items():
        spatial_dir = data_dir / "cities" / city / "02_spatial"
        spatial_dir.mkdir(parents=True, exist_ok=True)
        out_gpkg = spatial_dir / "transactions.gpkg"
        
        if out_gpkg.exists() and args.force: out_gpkg.unlink()
        if not out_gpkg.exists():
            print(f"[{city}] Składanie bazy RCN z cache...", flush=True)
            for t in teryts:
                cache_gml = cache_dir / f"{t}.gml"
                if cache_gml.exists():
                    subprocess.run(["ogr2ogr", "-f", "GPKG", "-update", "-append", str(out_gpkg), str(cache_gml), "-nln", "transactions"], capture_output=True)

        print(f"[{city}] --- AUDIT RCN ---", flush=True)
        try:
            if out_gpkg.exists():
                gdf = gpd.read_file(out_gpkg)
                print(f"[{city}] > Pobrano: {len(gdf)} transakcji.", flush=True)
            else:
                print(f"[{city}] > [!] BRAK DANYCH", flush=True)
        except Exception as e:
            print(f"[{city}] > [!] Błąd: {e}", flush=True)

    print(f"__PIPELINE_METRICS__={json.dumps({'step': '07', 'success': success_count, 'hubs': len(city_map)})}")

if __name__ == "__main__":
    main()
