import osmnx as ox
import geopandas as gpd
from pathlib import Path
from shapely.geometry import box
import os

# --- CONFIG ---
STOPS_GPKG = "data/processed/all_stops_poland.gpkg"
NETWORK_DIR = Path("data/raw/network")

def fetch_all_networks():
    print("Inicjalizacja masowego pobierania grafów OSM...")
    NETWORK_DIR.mkdir(parents=True, exist_ok=True)
    
    # Wczytujemy wszystkie przystanki Polski
    stops = gpd.read_file(STOPS_GPKG)
    
    # Grupowanie po aglomeracji
    groups = stops.groupby('source_city')
    print(f"Znaleziono {len(groups)} aglomeracji do przetworzenia.")

    for city_name, group in groups:
        # Normalizacja nazwy folderu (np. "warsaw/ztm" -> "warsaw_ztm")
        safe_name = str(city_name).replace("/", "_")
        
        walk_path = NETWORK_DIR / f"{safe_name}_walk.graphml"
        drive_path = NETWORK_DIR / f"{safe_name}_drive.graphml"
        
        if walk_path.exists() and drive_path.exists():
            # print(f"  [SKIP] {safe_name} - grafy już istnieją.")
            continue

        print(f"\n--- PRZETWARZANIE: {safe_name} ({len(group)} przystanków) ---")
        
        try:
            # Wyznaczamy BBOX w WGS84 z buforem 3km
            # Bufor robimy w układzie metrycznym dla precyzji, potem wracamy do WGS84
            group_2180 = group.to_crs("EPSG:2180")
            bounds_2180 = box(*group_2180.total_bounds).buffer(3000)
            bounds_wgs84 = gpd.GeoSeries([bounds_2180], crs="EPSG:2180").to_crs("EPSG:4326").iloc[0]

            # Pobieranie grafu pieszego
            if not walk_path.exists():
                print(f"  [FETCH] Pobieranie sieci pieszej (walk)...")
                G_walk = ox.graph_from_polygon(bounds_wgs84, network_type='walk')
                ox.save_graphml(G_walk, filepath=walk_path)
                print(f"  [OK] Zapisano walk.")

            # Pobieranie grafu drogowego
            if not drive_path.exists():
                print(f"  [FETCH] Pobieranie sieci drogowej (drive)...")
                G_drive = ox.graph_from_polygon(bounds_wgs84, network_type='drive')
                ox.save_graphml(G_drive, filepath=drive_path)
                print(f"  [OK] Zapisano drive.")

        except Exception as e:
            print(f"  [ERROR] {safe_name}: {e}")

    # Aktualizacja DevLog
    with open("devlog.md", "a") as f:
        f.write(f"\n### 19. Masowe pobieranie grafów sieciowych (OSM)\n- **Działanie:** Wdrożenie `scripts/fetch_all_networks.py` do automatycznej ekstrakcji grafów walk/drive dla każdej aglomeracji.\n- **Uzasadnienie:** Umożliwienie analizy realnych tras dojścia i przejazdu w skali całego kraju.\n")

if __name__ == "__main__":
    fetch_all_networks()
