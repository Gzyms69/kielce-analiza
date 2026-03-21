import os
import subprocess
import pandas as pd
import osmnx as ox
import time
import gc
from pathlib import Path

# --- CONFIG ---
PBF_SOURCE = Path("data/poland/osm/poland-latest.osm.pbf")
CITIES_ROOT = Path("data/cities")

def process_city_safe(city_dir):
    city_name = city_dir.name
    net_dir = city_dir / "network"
    net_dir.mkdir(parents=True, exist_ok=True)
    
    # Skalujemy bezpiecznie: pomijamy jeśli już mamy wynik
    if (net_dir / "walk.graphml").exists():
        return

    print(f"\n>>> PRZETWARZANIE: {city_name}")
    
    # 1. Wyznaczamy BBOX
    all_stops = []
    for stops_file in (city_dir / "gtfs").rglob("stops.txt"):
        try:
            df = pd.read_csv(stops_file)
            if 'stop_lat' in df.columns:
                all_stops.append(df[['stop_lat', 'stop_lon']])
        except: pass
            
    if not all_stops:
        print(f"    [SKIP] Brak przystanków")
        return
            
    combined = pd.concat(all_stops)
    min_lat, min_lon = combined.min()
    max_lat, max_lon = combined.max()
    bbox_str = f"{min_lon-0.03},{min_lat-0.03},{max_lon+0.03},{max_lat+0.03}"
    
    temp_pbf = net_dir / f"tmp_{city_name}.pbf"
    temp_osm = net_dir / f"tmp_{city_name}.osm"

    try:
        # 2. OSMIUM: Surgical Extract (Błyskawiczne)
        subprocess.run(["osmium", "extract", "--bbox", bbox_str, str(PBF_SOURCE), "-o", str(temp_pbf), "--overwrite"], 
                       check=True, capture_output=True)

        # 3. OSMIUM: Ultra-Aggressive Filter (Tylko drogi omijając pola i lasy)
        # Zostawiamy tylko to co faktycznie moze byc trasa spaceru/autobusu
        subprocess.run(["osmium", "tags-filter", str(temp_pbf), 
                        "w/highway=primary,secondary,tertiary,residential,unclassified,service,footway,living_street", 
                        "-o", str(temp_osm), "--overwrite"], 
                       check=True, capture_output=True)
        
        # 4. OSMNX: Build Graph (Sekwencyjnie i z pomiarem)
        print(f"    Budowanie grafu z {temp_osm.stat().st_size / (1024*1024):.1f} MB XML...")
        start = time.time()
        G = ox.graph_from_xml(str(temp_osm))
        
        # 5. SAVE & LINK
        output_file = net_dir / "walk.graphml"
        ox.save_graphml(G, filepath=output_file)
        
        # Drive to na razie link do walk dla uproszczenia (lub oddzielna analiza później)
        if not (net_dir / "drive.graphml").exists():
            os.link(output_file, net_dir / "drive.graphml")

        print(f"    [OK] Sukces w {time.time()-start:.1f}s. Węzły: {len(G.nodes)}")

    except Exception as e:
        print(f"    [ERROR] {city_name}: {e}")
    finally:
        # SPRZĄTANIE I ZWALNIANIE RAM
        if temp_pbf.exists(): temp_pbf.unlink()
        if temp_osm.exists(): temp_osm.unlink()
        if 'G' in locals(): del G
        gc.collect()

def main():
    print("Inicjalizacja Safe Harvester (Sequential Mode)...")
    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    for city_dir in cities:
        process_city_safe(city_dir)

    print("\n--- PROCES ZAKOŃCZONY POMYŚLNIE ---")

if __name__ == "__main__":
    main()
