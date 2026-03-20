import geopandas as gpd
import pandas as pd
from pathlib import Path
import shutil
import os
import warnings

warnings.filterwarnings("ignore")

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def get_allowed_cities():
    cities_env = os.environ.get("PIPELINE_CITIES")
    if cities_env:
        return [c.strip() for c in cities_env.split(',')]
    return None

def isolate_city(city_name, data_dir):
    city_dir = data_dir / "cities" / city_name
    print(f"\n--- Izolacja danych dla: {city_name.upper()} ---")
    
    # 1. Tworzenie nowej struktury
    subdirs = ["01_source", "02_spatial", "03_config", "04_results"]
    for sd in subdirs:
        (city_dir / sd).mkdir(parents=True, exist_ok=True)
        
    # 2. Segregacja istniejących plików
    # stops -> 02_spatial
    stops_old = city_dir / "smart_stops.gpkg"
    if stops_old.exists():
        shutil.move(str(stops_old), str(city_dir / "02_spatial" / "stops.gpkg"))
        
    # infrastructure -> 02_spatial
    osm_old = city_dir / "osm_full.gpkg"
    if osm_old.exists():
        shutil.move(str(osm_old), str(city_dir / "02_spatial" / "infrastructure.gpkg"))
        
    # transactions -> 02_spatial
    rcn_old = city_dir / "rcn" / "transactions.gpkg"
    if rcn_old.exists():
        shutil.move(str(rcn_old), str(city_dir / "02_spatial" / "transactions.gpkg"))
        # Usuwamy stary pusty folder rcn/
        if (city_dir / "rcn").exists() and not os.listdir(city_dir / "rcn"):
            shutil.rmtree(city_dir / "rcn")
        
    # 3. Wycinanie lokalnej siatki populacji
    stops_path = city_dir / "02_spatial" / "stops.gpkg"
    target_pop = city_dir / "02_spatial" / "population_250m.gpkg"
    pop_path = data_dir / "poland" / "population" / "nsp2021_grid250m.gpkg"
    
    if stops_path.exists() and pop_path.exists() and not target_pop.exists():
        try:
            print(f"  Wycinanie lokalnej siatki populacji (odczyt BBOX bez przepełniania RAM)...")
            stops = gpd.read_file(stops_path)
            
            # 1. Pobieramy CRS siatki (nsp2021 jest w EPSG:3035 - ETRS89-LAEA)
            import fiona
            with fiona.open(pop_path) as src:
                grid_crs = src.crs
            
            print(f"  Wykryto CRS siatki: {grid_crs}")
            
            # 2. Transformacja BBOX do układu siatki
            # Przystanki są w 4326. Musimy je rzutować na 3035, aby BBOX był w metrach LAEA.
            stops_in_grid_crs = stops.to_crs(grid_crs)
            city_bbox = stops_in_grid_crs.total_bounds
            print(f"  BBOX w CRS siatki: {city_bbox}")
            
            # 3. Wczytujemy z dysku tylko wycinek dla danego BBOX!
            clipped_pop = gpd.read_file(pop_path, bbox=tuple(city_bbox))
            
            if not clipped_pop.empty:
                # KRYTYCZNE: Konwertujemy wynik do standardu projektu EPSG:2180
                clipped_pop = clipped_pop.to_crs("EPSG:2180")
                
                if 'TOT' in clipped_pop.columns:
                    clipped_pop[['TOT', 'geometry']].to_file(target_pop, driver="GPKG")
                else:
                    clipped_pop.to_file(target_pop, driver="GPKG")
                print(f"  [SUKCES] Zapisano {len(clipped_pop)} komórek populacji w EPSG:2180.")
            else:
                print(f"  [BŁĄD] Pusty wycinek populacji! BBOX: {city_bbox}")
                # Nie tworzymy pustego pliku
        except Exception as e:
            print(f"  [BŁĄD KRYTYCZNY] Wycinanie populacji nie powiodło się: {e}")
            raise e

def run_isolation():
    data_dir = get_data_dir()
    cities_root = data_dir / "cities"
    allowed_cities = get_allowed_cities()
    
    if not cities_root.exists(): return
    
    cities = sorted([d.name for d in cities_root.iterdir() if d.is_dir()])

    for city in cities:
        if allowed_cities and city not in allowed_cities:
            continue
        isolate_city(city, data_dir)
        
    print("\nPROCES IZOLACJI ZAKOŃCZONY.")

if __name__ == "__main__":
    run_isolation()
