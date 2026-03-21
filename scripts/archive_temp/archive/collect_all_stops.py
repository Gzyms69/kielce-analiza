import pandas as pd
import geopandas as gpd
from pathlib import Path
import os

GTFS_ROOT = Path("data/raw/gtfs")
OUTPUT_POINTS = Path("data/processed/all_stops_poland.gpkg")

def collect_all_stops():
    all_stops = []
    print("Rozpoczynam audyt przystanków...")

    for stops_file in GTFS_ROOT.rglob("stops.txt"):
        try:
            city_name = stops_file.parent.relative_to(GTFS_ROOT)
            df = pd.read_csv(stops_file)
            if 'stop_lat' in df.columns and 'stop_lon' in df.columns:
                # Wyciągamy tylko potrzebne kolumny
                df = df[['stop_id', 'stop_name', 'stop_lat', 'stop_lon']].copy()
                df['source_city'] = str(city_name)
                all_stops.append(df)
                print(f"[OK] Przetworzono: {city_name} ({len(df)} przystanków)")
        except Exception as e:
            print(f"[ERR] Błąd w {stops_file}: {e}")

    if all_stops:
        combined = pd.concat(all_stops, ignore_index=True)
        gdf = gpd.GeoDataFrame(
            combined, 
            geometry=gpd.points_from_xy(combined.stop_lon, combined.stop_lat),
            crs="EPSG:4326"
        )
        # Zapisujemy do GPKG (może być duże, ale to punkty, więc spokojnie)
        gdf.to_file(OUTPUT_POINTS, driver="GPKG")
        print(f"\nSukces! Zebrano łącznie {len(gdf)} przystanków z całej Polski.")
        print(f"Dane zapisano w: {OUTPUT_POINTS}")
    else:
        print("Nie znaleziono żadnych danych GTFS.")

if __name__ == "__main__":
    collect_all_stops()
