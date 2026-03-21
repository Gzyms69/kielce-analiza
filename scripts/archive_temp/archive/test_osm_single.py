import os
import sys
from pathlib import Path

# Dodajemy scripts/core do ścieżki, aby móc zaimportować funkcję
sys.path.append(str(Path("scripts/core").absolute()))
from extract_all_osm_turbo import process_city_turbo

def test_single_city():
    city_name = "legnica"
    city_dir = Path(f"data/cities/{city_name}")
    print(f"Testowa ekstrakcja OSM dla: {city_name}...")
    
    # Uruchamiamy funkcję procesującą
    result = process_city_turbo(city_dir)
    print(result)
    
    osm_file = city_dir / "osm_full.gpkg"
    if osm_file.exists() and osm_file.stat().st_size > 1000:
        print(f"SUKCES: Plik {osm_file} został utworzony poprawnie ({osm_file.stat().st_size / 1024:.1f} KB).")
    else:
        print(f"PORAŻKA: Plik {osm_file} nie istnieje lub jest uszkodzony.")

if __name__ == "__main__":
    test_single_city()
