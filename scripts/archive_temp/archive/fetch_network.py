import osmnx as ox
import geopandas as gpd
import pandas as pd
from shapely.geometry import box
import os
from pathlib import Path

# --- CONFIG ---
STOPS_GPKG = "data/processed/kielce_stops.gpkg"
RAW_NETWORK_DIR = Path("data/raw/network")
PROCESSED_NETWORK_DIR = Path("data/processed/network")

def fetch_kielce_network():
    print("Wczytywanie maski Kielc (z przystanków)...")
    stops_gdf = gpd.read_file(STOPS_GPKG)
    # Wyznaczamy obszar analityczny (bufor 3km wokół przystanków)
    # Musimy to rzutować na WGS84 dla OSMNX
    bounds_2180 = box(*stops_gdf.total_bounds).buffer(3000)
    bounds_wgs84 = gpd.GeoSeries([bounds_2180], crs="EPSG:2180").to_crs("EPSG:4326").iloc[0]

    # 1. POBIERANIE SIECI DROGOWEJ (Dla autobusów)
    print("Pobieranie sieci drogowej (drive) z OSM...")
    graph_drive = ox.graph_from_polygon(bounds_wgs84, network_type='drive')
    ox.save_graphml(graph_drive, filepath=RAW_NETWORK_DIR / "kielce_drive.graphml")
    print(f"Zapisano sieć drogową: {RAW_NETWORK_DIR / 'kielce_drive.graphml'}")

    # 2. POBIERANIE SIECI PIESZEJ (Dla dojścia do przystanków)
    print("Pobieranie sieci pieszej (walk) z OSM...")
    graph_walk = ox.graph_from_polygon(bounds_wgs84, network_type='walk')
    ox.save_graphml(graph_walk, filepath=RAW_NETWORK_DIR / "kielce_walk.graphml")
    print(f"Zapisano sieć pieszą: {RAW_NETWORK_DIR / 'kielce_walk.graphml'}")

if __name__ == "__main__":
    fetch_kielce_network()
