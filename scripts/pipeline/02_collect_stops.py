import pandas as pd
import geopandas as gpd
from pathlib import Path
from shapely.ops import unary_union
import os

CITIES_ROOT = Path("data/cities")
ALL_STOPS_OUTPUT = Path("data/poland/admin/all_stops_smart.gpkg")

# Definicja źródeł kolejowych (do filtracji grawitacyjnej)
RAIL_KEYWORDS = ['pkp-', 'wkd', 'lka', 'koleje-', 'rail']

def process_city_smart(city_dir):
    city_name = city_dir.name
    gtfs_root = city_dir / "gtfs"
    if not gtfs_root.exists():
        return None

    urban_stops = []
    rail_stops = []

    # 1. Agregacja przystanków z podziałem na klasy
    for source_dir in gtfs_root.iterdir():
        if not source_dir.is_dir(): continue
        stops_file = source_dir / "stops.txt"
        if not stops_file.exists(): continue

        try:
            df = pd.read_csv(stops_file)
            if 'stop_lat' not in df.columns or 'stop_lon' not in df.columns:
                continue
                
            gdf = gpd.GeoDataFrame(
                df[['stop_id', 'stop_name', 'stop_lat', 'stop_lon']],
                geometry=gpd.points_from_xy(df.stop_lon, df.stop_lat),
                crs="EPSG:4326"
            ).to_crs("EPSG:2180")
            
            gdf['source'] = source_dir.name
            
            # Klasyfikacja: Kolej vs Miasto
            if any(k in source_dir.name.lower() for k in RAIL_KEYWORDS):
                rail_stops.append(gdf)
            else:
                urban_stops.append(gdf)
        except Exception as e:
            print(f"  [ERR] {city_name}/{source_dir.name}: {e}")

    if not urban_stops:
        print(f"  [SKIP] {city_name}: Brak przystanków miejskich!")
        return None

    # 2. Tworzenie "Śladu Miejskiego" (Urban Footprint) - 5km od autobusu
    urban_gdf = pd.concat(urban_stops)
    urban_footprint = urban_gdf.geometry.buffer(5000).unary_union
    
    # 3. Filtracja Grawitacyjna Kolei
    filtered_rail = []
    if rail_stops:
        all_rail_gdf = pd.concat(rail_stops)
        # Zostawiamy tylko te stacje PKP, które są wewnątrz 5km od miasta
        valid_rail = all_rail_gdf[all_rail_gdf.geometry.intersects(urban_footprint)]
        if not valid_rail.empty:
            filtered_rail.append(valid_rail)
            print(f"  [{city_name}] Pozostawiono {len(valid_rail)}/{len(all_rail_gdf)} stacji kolejowych.")

    # 4. Łączenie w finalny zbiór Smart
    final_city_stops = pd.concat([urban_gdf] + filtered_rail)
    final_city_stops['city'] = city_name
    
    # 5. Generowanie Wykrojnika (1500m bufor od Smart Stops)
    transport_zone = final_city_stops.geometry.buffer(1500).unary_union
    # Uproszczenie geometrii dla wydajności narzędzi C++ (osmium/gdal)
    simplified_zone = transport_zone.simplify(10)
    
    # Zapis wykrojnika
    zone_gdf = gpd.GeoDataFrame(geometry=[simplified_zone], crs="EPSG:2180").to_crs("EPSG:4326")
    zone_gdf.to_file(city_dir / "transport_zone.gpkg", driver="GPKG")
    
    # Zapis Smart Stops
    stops_output = city_dir / "smart_stops.gpkg"
    final_city_stops.to_crs("EPSG:4326").to_file(stops_output, driver="GPKG")
    
    return final_city_stops

def main():
    print("=== START URBAN GRAVITY ENGINE (Faza 2) ===")
    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    all_poland_smart = []

    for city_dir in cities:
        res = process_city_smart(city_dir)
        if res is not None:
            all_poland_smart.append(res)

    if all_poland_smart:
        # Zapisujemy globalną bazę Smart Stops
        combined = pd.concat(all_poland_smart)
        ALL_STOPS_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        combined.to_crs("EPSG:4326").to_file(ALL_STOPS_OUTPUT, driver="GPKG")
        print(f"\nSukces! Wygenerowano Smart Stops dla {len(all_poland_smart)} aglomeracji.")
        print(f"Globalna baza: {len(combined)} przystanków.")

if __name__ == "__main__":
    main()
