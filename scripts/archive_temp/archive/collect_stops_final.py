import pandas as pd
import geopandas as gpd
from pathlib import Path

CITIES_ROOT = Path("data/cities")
OUTPUT_GPKG = Path("data/poland/admin/all_stops.gpkg")

def collect_stops():
    print("Agregacja przystanków ze wszystkich aglomeracji...")
    all_stops = []
    
    # Przeszukujemy foldery miast w poszukiwaniu stops.txt
    for stops_file in CITIES_ROOT.rglob("stops.txt"):
        try:
            # Nazwa aglomeracji to nazwa folderu w data/cities/
            city_name = stops_file.relative_to(CITIES_ROOT).parts[0]
            df = pd.read_csv(stops_file)
            
            if 'stop_lat' in df.columns and 'stop_lon' in df.columns:
                gdf = gpd.GeoDataFrame(
                    df[['stop_id', 'stop_name', 'stop_lat', 'stop_lon']],
                    geometry=gpd.points_from_xy(df.stop_lon, df.stop_lat),
                    crs="EPSG:4326"
                )
                gdf['city'] = city_name
                all_stops.append(gdf)
                # print(f"  [OK] {city_name}")
        except Exception as e:
            print(f"  [ERR] {stops_file}: {e}")

    if all_stops:
        combined = gpd.GeoDataFrame(pd.concat(all_stops, ignore_index=True), crs="EPSG:4326")
        OUTPUT_GPKG.parent.mkdir(parents=True, exist_ok=True)
        combined.to_file(OUTPUT_GPKG, driver="GPKG")
        print(f"Sukces! Odtworzono bazę: {len(combined)} przystanków.")
        print(f"Zapisano w: {OUTPUT_GPKG}")
    else:
        print("Nie znaleziono żadnych plików GTFS!")

if __name__ == "__main__":
    collect_stops()
