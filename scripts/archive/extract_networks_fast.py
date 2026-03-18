import os
import subprocess
import pandas as pd
import osmnx as ox
from pathlib import Path

# --- CONFIG ---
PBF_SOURCE = Path("data/poland/osm/poland-latest.osm.pbf")
CITIES_ROOT = Path("data/cities")

def extract_networks():
    print(f"Rozpoczynam zoptymalizowaną ekstrakcję grafów z PBF ({PBF_SOURCE})...")
    
    cities = [d for d in CITIES_ROOT.iterdir() if d.is_dir()]
    
    for i, city_dir in enumerate(cities, 1):
        city_name = city_dir.name
        gtfs_dir = city_dir / "gtfs"
        net_dir = city_dir / "network"
        net_dir.mkdir(parents=True, exist_ok=True)
        
        # Sprawdzamy czy już są grafy
        if (net_dir / "walk.graphml").exists() and (net_dir / "drive.graphml").exists():
            continue

        print(f"[{i}/{len(cities)}] Przetwarzanie: {city_name}...", end=" ", flush=True)
        
        all_stops = []
        for stops_file in gtfs_dir.rglob("stops.txt"):
            try:
                df = pd.read_csv(stops_file)
                if 'stop_lat' in df.columns:
                    all_stops.append(df[['stop_lat', 'stop_lon']])
            except: pass
            
        if not all_stops:
            print("POMINIĘTO (Brak przystanków)")
            continue
            
        combined_stops = pd.concat(all_stops)
        min_lat, min_lon = combined_stops.min()
        max_lat, max_lon = combined_stops.max()
        
        # Margines ~3km
        bbox_str = f"{min_lon-0.03},{min_lat-0.03},{max_lon+0.03},{max_lat+0.03}"
        temp_pbf = net_dir / "temp_bbox.pbf"
        temp_osm = net_dir / "temp_roads.osm"

        try:
            # 1. WYCINANIE BBOX (do binarnego PBF, bo najszybciej)
            subprocess.run([
                "osmium", "extract", 
                "--bbox", bbox_str, 
                str(PBF_SOURCE), 
                "-o", str(temp_pbf), 
                "--overwrite"
            ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            # 2. FILTROWANIE (tylko drogi) -> Zapis do XML dla OSMNX
            subprocess.run([
                "osmium", "tags-filter",
                str(temp_pbf),
                "w/highway",  # Zatrzymaj tylko drogi/ścieżki
                "-o", str(temp_osm),
                "--overwrite"
            ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            # 3. OSMNX: Wczytanie czystego, małego XML i budowa grafu
            G = ox.graph_from_xml(str(temp_osm))
            
            ox.save_graphml(G, filepath=net_dir / "full_network.graphml")
            
            # Linki symboliczne
            if not (net_dir / "walk.graphml").exists():
                os.link(net_dir / "full_network.graphml", net_dir / "walk.graphml")
            if not (net_dir / "drive.graphml").exists():
                os.link(net_dir / "full_network.graphml", net_dir / "drive.graphml")

            # Sprzątanie
            temp_pbf.unlink()
            temp_osm.unlink()
            
            # Sprawdzenie ile węzłów ma graf
            print(f"GOTOWE ({len(G.nodes)} węzłów)")

        except Exception as e:
            print(f"BŁĄD: {e}")
            if temp_pbf.exists(): temp_pbf.unlink()
            if temp_osm.exists(): temp_osm.unlink()

if __name__ == "__main__":
    extract_networks()
