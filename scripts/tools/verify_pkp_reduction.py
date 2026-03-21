import geopandas as gpd
import pandas as pd
from pathlib import Path
import os
import sys

def verify_city(city_name):
    print(f"\n--- PKP REDUCTION AUDIT: {city_name.upper()} ---")
    
    old_path = Path("data/cities") / city_name / "02_spatial" / "stops.gpkg"
    new_path = Path("test-pipeline/cities") / city_name / "02_spatial" / "stops.gpkg"
    
    if not old_path.exists() or not new_path.exists():
        print(f"  [ERR] Brak plików do porównania. Old: {old_path.exists()}, New: {new_path.exists()}")
        return

    # Wczytywanie danych
    old_stops = gpd.read_file(old_path)
    new_stops = gpd.read_file(new_path)
    
    old_cnt = len(old_stops)
    new_cnt = len(new_stops)
    reduction = old_cnt - new_cnt
    
    print(f"  Stary pipeline (Baseline): {old_cnt} przystanków")
    print(f"  Nowy pipeline (v7.1):      {new_cnt} przystanków")
    print(f"  Zredukowano:               {reduction} przystanków ({ (reduction/old_cnt*100 if old_cnt > 0 else 0):.1f}%)")
    
    # Analiza powierzchni bufora (ile realnie oszczędzamy "pustego" pola)
    # Rzutujemy na 2180 dla obliczeń w metrach
    old_area = old_stops.to_crs("EPSG:2180").buffer(1500).union_all().area / 1_000_000
    new_area = new_stops.to_crs("EPSG:2180").buffer(1500).union_all().area / 1_000_000
    
    area_diff = old_area - new_area
    print(f"  Powierzchnia strefy (km2): Old={old_area:.1f} | New={new_area:.1f}")
    print(f"  Zaoszczędzono:             {area_diff:.1f} km2 pola do analizy RCN/POP.")

    if reduction > 0:
        # Znajdź nazwy odrzuconych stacji (jeśli mają nazwy)
        old_names = set(old_stops['stop_name'].tolist()) if 'stop_name' in old_stops.columns else set()
        new_names = set(new_stops['stop_name'].tolist()) if 'stop_name' in new_stops.columns else set()
        dropped = sorted(list(old_names - new_names))
        
        if dropped:
            print(f"  Przykładowe odrzucone stacje (Lasy/Pustostany):")
            for d in dropped[:10]:
                print(f"    - {d}")
            if len(dropped) > 10:
                print(f"    ... i {len(dropped)-10} więcej.")

if __name__ == "__main__":
    cities = ["kielce", "warszawa", "lodz", "swinoujscie"]
    for c in cities:
        verify_city(c)
