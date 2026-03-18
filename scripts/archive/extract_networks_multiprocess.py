import os
import subprocess
import pandas as pd
import osmnx as ox
import time
from pathlib import Path
import concurrent.futures
from shapely.geometry import box

# --- CONFIG ---
PBF_SOURCE = Path("data/poland/osm/poland-latest.osm.pbf")
CITIES_ROOT = Path("data/cities")
MAX_WORKERS = 4 # Ograniczamy do 4, aby nie zabić RAMu przy wielkich miastach

def process_city(task_data):
    city_name, min_lon, min_lat, max_lon, max_lat, city_dir = task_data
    net_dir = city_dir / "network"
    net_dir.mkdir(parents=True, exist_ok=True)
    
    if (net_dir / "walk.graphml").exists() and (net_dir / "drive.graphml").exists():
        return f"[SKIP] {city_name} (Gotowe)"

    bbox_str = f"{min_lon-0.03},{min_lat-0.03},{max_lon+0.03},{max_lat+0.03}"
    temp_pbf = net_dir / f"temp_bbox_{city_name}.pbf"
    temp_osm = net_dir / f"temp_roads_{city_name}.osm"

    try:
        # 1. Osmium BBOX
        subprocess.run(["osmium", "extract", "--bbox", bbox_str, str(PBF_SOURCE), "-o", str(temp_pbf), "--overwrite"], 
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # 2. Osmium Filter (Tylko drogi) -> XML
        subprocess.run(["osmium", "tags-filter", str(temp_pbf), "w/highway", "-o", str(temp_osm), "--overwrite"], 
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        file_size_mb = temp_osm.stat().st_size / (1024 * 1024)
        
        # 3. OSMNX Parsing (Czasochłonne!)
        start_time = time.time()
        G = ox.graph_from_xml(str(temp_osm))
        parse_time = time.time() - start_time
        
        ox.save_graphml(G, filepath=net_dir / "full_network.graphml")
        
        if not (net_dir / "walk.graphml").exists(): os.link(net_dir / "full_network.graphml", net_dir / "walk.graphml")
        if not (net_dir / "drive.graphml").exists(): os.link(net_dir / "full_network.graphml", net_dir / "drive.graphml")

        temp_pbf.unlink(missing_ok=True)
        temp_osm.unlink(missing_ok=True)
        
        return f"[OK] {city_name:<15} | XML: {file_size_mb:>5.1f} MB | Parsowanie: {parse_time:>4.1f}s | Węzły: {len(G.nodes)}"

    except Exception as e:
        temp_pbf.unlink(missing_ok=True)
        temp_osm.unlink(missing_ok=True)
        return f"[BŁĄD] {city_name}: {e}"

def main():
    print("Inicjalizacja Parallel Harvester...")
    tasks = []
    
    cities = [d for d in CITIES_ROOT.iterdir() if d.is_dir()]
    print(f"Skanowanie obszarów dla {len(cities)} aglomeracji...")

    for city_dir in cities:
        city_name = city_dir.name
        gtfs_dir = city_dir / "gtfs"
        
        all_stops = []
        for stops_file in gtfs_dir.rglob("stops.txt"):
            try:
                df = pd.read_csv(stops_file)
                if 'stop_lat' in df.columns:
                    all_stops.append(df[['stop_lat', 'stop_lon']])
            except: pass
            
        if not all_stops:
            continue
            
        combined = pd.concat(all_stops)
        min_lat, min_lon = combined.min()
        max_lat, max_lon = combined.max()
        
        # Obliczamy pole bounding boxa do posortowania
        area = (max_lon - min_lon) * (max_lat - min_lat)
        tasks.append((area, (city_name, min_lon, min_lat, max_lon, max_lat, city_dir)))

    # Sortujemy od najmniejszych do największych (molochy na koniec)
    tasks.sort(key=lambda x: x[0])
    task_data_sorted = [t[1] for t in tasks]

    print(f"Uruchamiam pulę {MAX_WORKERS} procesów...\n" + "-"*70)

    # Odpalenie wielowątkowe
    with concurrent.futures.ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # submit tasks and get futures
        futures = {executor.submit(process_city, data): data[0] for data in task_data_sorted}
        
        # Odbieranie wyników w miarę kończenia
        for future in concurrent.futures.as_completed(futures):
            city_name = futures[future]
            try:
                result = future.result()
                print(result)
            except Exception as e:
                print(f"[CRASH] Wątek dla {city_name} wywalił się: {e}")

if __name__ == "__main__":
    main()
