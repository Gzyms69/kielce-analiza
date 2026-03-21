import pandas as pd
import geopandas as gpd
from geopy.geocoders import Nominatim
from pathlib import Path
import time
import os

# --- CONFIG ---
INPUT_GPKG = "data/processed/all_stops_poland.gpkg"
OUTPUT_CSV = "reports/city_county_mapping.csv"

def map_cities():
    print("Wczytywanie zagregowanych przystanków...")
    stops = gpd.read_file(INPUT_GPKG)
    
    # Wybieramy po jednym punkcie reprezentatywnym dla każdego źródła danych (miasta/aglomeracji)
    # To wystarczy, by Nominatim zwrócił nam powiat
    cities = stops.groupby('source_city').first().reset_index()
    print(f"Znaleziono {len(cities)} unikalnych źródeł danych. Rozpoczynam geokodowanie...")

    geolocator = Nominatim(user_agent="kielce_analiza_v2")
    mapping = []

    for _, row in cities.iterrows():
        source = row['source_city']
        try:
            print(f"  Analizowanie: {source}...", end="", flush=True)
            # Reverse geocoding
            location = geolocator.reverse((row['stop_lat'], row['stop_lon']), language='pl')
            if location and 'address' in location.raw:
                address = location.raw['address']
                # Szukamy powiatu, miasta na prawach powiatu lub gminy
                county = address.get('county', address.get('city', address.get('town', 'Nieznany')))
                mapping.append({
                    'source_city': source,
                    'identified_county': county,
                    'lat': row['stop_lat'],
                    'lon': row['stop_lon']
                })
                print(f" -> {county}")
            else:
                print(" -> NIE ZNALEZIONO")
            
            # Limit API Nominatim (1 request per second)
            time.sleep(1.1)
            
        except Exception as e:
            print(f" -> BŁĄD: {e}")
            time.sleep(2)

    # Zapis wyników
    df_out = pd.DataFrame(mapping)
    df_out.to_csv(OUTPUT_CSV, index=False)
    print(f"\nMapowanie zakończone. Wyniki zapisano w: {OUTPUT_CSV}")

    # Aktualizacja DevLog
    with open("devlog.md", "a") as f:
        f.write(f"\n### 13. Mapowanie miast na powiaty\n- **Działanie:** Użycie geokodowania odwróconego (Nominatim) dla unikalnych źródeł GTFS.\n- **Uzasadnienie:** Uzyskanie nazw jednostek terytorialnych niezbędnych do pobrania danych RCN z WFS, bez konieczności pobierania ciężkich map granic.\n")

if __name__ == "__main__":
    map_cities()
