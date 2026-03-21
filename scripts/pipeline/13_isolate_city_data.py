import geopandas as gpd
import pandas as pd
from pathlib import Path
import shutil
import os
import warnings
import argparse
import json

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", message=".*Geometry is in a geographic CRS.*")

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def isolate_city(city_name, data_dir):
    city_dir = data_dir / "cities" / city_name
    
    subdirs = ["01_source", "02_spatial", "03_config", "04_results"]
    for sd in subdirs:
        (city_dir / sd).mkdir(parents=True, exist_ok=True)
        
    zone_path = city_dir / "transport_zone.gpkg"
    target_pop = city_dir / "02_spatial" / "population_250m.gpkg"
    pop_path = data_dir / "poland" / "population" / "nsp2021_grid250m.gpkg"
    
    pop_cells = 0
    pop_total = 0

    if zone_path.exists() and pop_path.exists():
        if target_pop.exists():
            # Zczytanie danych z istniejącego pliku by wypluć metryki
            existing = gpd.read_file(target_pop)
            pop_cells = len(existing)
            pop_total = existing['TOT'].sum() if 'TOT' in existing.columns else 0
        else:
            try:
                zone = gpd.read_file(zone_path)
                import fiona
                with fiona.open(pop_path) as src:
                    grid_crs = src.crs
                
                zone_in_grid_crs = zone.to_crs(grid_crs)
                city_bbox = zone_in_grid_crs.total_bounds
                
                # KROK 1: Szybkie doczytanie wycinka po BBOX (pre-filtr, lekki dla RAM)
                bbox_pop = gpd.read_file(pop_path, bbox=tuple(city_bbox))
                
                if not bbox_pop.empty:
                    # KROK 2: POPRAWKA P0-2 -- Precyzyjny clip poligonem transport zone
                    # Uzywamy sjoin (intersects) zamiast gpd.clip() -- sjoin korzysta
                    # z R-tree spatial index i NIE tworzy nowych geometrii, wiec jest
                    # lekki dla RAM i CPU (per komentarz usera: "nie rozsadz procesora")
                    zone_2180 = zone.to_crs("EPSG:2180")
                    bbox_pop_2180 = bbox_pop.to_crs("EPSG:2180")
                    
                    clipped_pop = gpd.sjoin(bbox_pop_2180, zone_2180, how="inner", predicate="intersects")
                    # sjoin dodaje kolumny z prawej strony -- usun je
                    clipped_pop = clipped_pop.drop(columns=["index_right"], errors="ignore")
                    # Usun duplikaty (komorka moze intersectowac wiele poligonow strefy)
                    clipped_pop = clipped_pop[~clipped_pop.index.duplicated(keep='first')]
                    
                    if not clipped_pop.empty:
                        cols_to_save = ['TOT', 'geometry'] if 'TOT' in clipped_pop.columns else list(clipped_pop.columns)
                        clipped_pop[cols_to_save].to_file(target_pop, driver="GPKG")
                        
                        pop_cells = len(clipped_pop)
                        pop_total = clipped_pop['TOT'].sum() if 'TOT' in clipped_pop.columns else 0
                    
                    # SANITY CHECK: Populacja > 5M to oznaka wycieku
                    if pop_total > 5_000_000:
                        import sys
                        print(f"  [!!!] {city_name}: Populacja = {pop_total:,.0f} - PODEJRZANIE WYSOKA", file=sys.stderr)
            except Exception as e:
                print(f"  [BŁĄD] Wycinanie populacji dla {city_name}: {e}")
                return False

    # Metryki dla Orkiestratora
    metrics = {
        "city": city_name,
        "pop_cells": pop_cells,
        "pop_total": int(pop_total)
    }
    print(f"__PIPELINE_METRICS__={json.dumps(metrics)}")
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", help="Miasto do izolacji", required=True)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    data_dir = get_data_dir()
    if args.force:
        target_pop = data_dir / "cities" / args.city / "02_spatial" / "population_250m.gpkg"
        if target_pop.exists(): target_pop.unlink()

    isolate_city(args.city, data_dir)

if __name__ == "__main__":
    main()
