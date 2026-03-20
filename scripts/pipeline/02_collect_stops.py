import pandas as pd
import geopandas as gpd
from pathlib import Path
from shapely.ops import unary_union
import os

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def get_allowed_cities():
    cities_env = os.environ.get("PIPELINE_CITIES")
    if cities_env:
        return [c.strip() for c in cities_env.split(',')]
    return None

CITIES_ROOT = get_data_dir() / "cities"
ALL_STOPS_OUTPUT = get_data_dir() / "poland" / "admin" / "all_stops_smart.gpkg"

# Definicja źródeł kolejowych (WKD i LKA są traktowane jako czysta komunikacja miejska)
RAIL_KEYWORDS = ['pkp', 'kolej', 'rail']

def load_global_rail_stops(cities_root):
    """Wczytuje globalne sieci kolejowe (PKP IC, PR itp.) i wykonuje bezpieczną deduplikację hybrydową."""
    global_rail_root = cities_root / "rail" / "gtfs"
    rail_gdfs = []
    
    if not global_rail_root.exists():
        return pd.DataFrame() # empty
        
    for source_dir in global_rail_root.iterdir():
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
            rail_gdfs.append(gdf)
        except Exception as e:
            print(f"  [ERR] rail/{source_dir.name}: {e}")
            
    if not rail_gdfs:
        return pd.DataFrame()
        
    all_rail = pd.concat(rail_gdfs, ignore_index=True)
    print(f"  [GLOBAL RAIL] Wczytano {len(all_rail)} surowych punktów kolejowych z całego kraju.")
    
    # HYBRYDOWE KLASTROWANIE (Przestrzeń + Semantyka)
    import re
    import unicodedata
    
    def normalize_name(name):
        n = str(name).lower()
        # Usuwanie polskich znaków
        n = ''.join(c for c in unicodedata.normalize('NFD', n) if unicodedata.category(c) != 'Mn')
        # Usuwanie przyrostków tworzących duplikaty między przewoźnikami
        n = re.sub(r'glown[ya]', '', n)
        n = re.sub(r'osobow[ya]', '', n)
        # Zostawiamy tylko znaki alfanumeryczne
        return re.sub(r'[^a-z0-9]', '', n)
        
    all_rail['norm_name'] = all_rail['stop_name'].apply(normalize_name)
    
    # Siatka przestrzenna (0.02 stopnia to zaokrąglenie grupujące punkty w promieniu ok 1-2km)
    all_rail['lat_grid'] = all_rail['stop_lat'].round(2)
    all_rail['lon_grid'] = all_rail['stop_lon'].round(2)
    
    # Usuwamy tylko te wpisy, które mają ZBIEŻNĄ NAZWĘ i leżą w TEJ SAMEJ SIATCE
    # To zapobiega fuzji Warszawy Centralnej ze Śródmieściem (inne nazwy)
    deduped_rail = all_rail.drop_duplicates(subset=['norm_name', 'lat_grid', 'lon_grid'])
    
    print(f"  [GLOBAL RAIL] Po klastrowaniu: {len(deduped_rail)} unikalnych stacji.")
    
    return deduped_rail

def process_city_smart(city_dir, global_rail_gdf):
    city_name = city_dir.name
    
    # "rail" to pseudo-miasto, nie generujemy dla niego osobnej strefy przestrzennej
    if city_name == "rail":
        return None
        
    gtfs_root = city_dir / "gtfs"
    if not gtfs_root.exists():
        return None

    urban_stops = []
    rail_stops = []
    
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
            
            # Klasyfikacja (lokalne koleje wrzucane do miasta np. lka, wkd, kw)
            is_rail = any(k in source_dir.name.lower() for k in RAIL_KEYWORDS)
            if is_rail:
                rail_stops.append(gdf)
            else:
                urban_stops.append(gdf)
            
        except Exception as e:
            print(f"  [ERR] {city_name}/{source_dir.name}: {e}")

    # Jeśli miasto nie ma ZADNYCH przystanków miejskich, to je odrzucamy jako całość
    if not urban_stops:
        print(f"  [SKIP] {city_name}: Brak bazowych przystanków miejskich (tylko kolej lub pustki)!")
        return None

    # 2. Tworzenie "Śladu Miejskiego" (Urban Footprint) z czystej komunikacji miejskiej
    # Używamy bufora 3km, co jest rozsadnym promieniem dla stacji PKP służących miastu
    urban_gdf = pd.concat(urban_stops, ignore_index=True)
    urban_footprint = urban_gdf.geometry.buffer(3000).unary_union
    
    # 3. Inteligentna Filtracja Kolei
    filtered_rail = []
    
    # Najpierw kolej lokalna przypisana do tego miasta
    all_rail_sources = list(rail_stops)
    
    # Dodajemy globalną kolej (jeśli istnieje)
    if not global_rail_gdf.empty:
        # Kopiujemy by nie nadpisać 'source' globalnego
        all_rail_sources.append(global_rail_gdf)
        
    if all_rail_sources:
        all_rail_gdf = pd.concat(all_rail_sources, ignore_index=True)
        # Zatrzymujemy TYLKO te stacje PKP/Regionalne, które leżą wewnątrz 3km od sieci miejskiej
        valid_rail = all_rail_gdf[all_rail_gdf.geometry.intersects(urban_footprint)]
        if not valid_rail.empty:
            filtered_rail.append(valid_rail)
            print(f"  [{city_name}] PKP: Wycięto lasy. Zostawiono {len(valid_rail)} stacji kolejowych w obrębie aglomeracji.")
        else:
            print(f"  [{city_name}] PKP: Odrzucono wszystkie stacje (poza zasięgiem miasta).")

    # 4. Łączenie w finalny zbiór Smart
    if filtered_rail:
        final_city_stops = pd.concat([urban_gdf] + filtered_rail, ignore_index=True)
    else:
        final_city_stops = urban_gdf
        
    final_city_stops['city'] = city_name
    
    # 5. Generowanie Ciasnego Wykrojnika (1500m od ZAAKCEPTOWANYCH przystanków)
    transport_zone = final_city_stops.geometry.buffer(1500).unary_union
    simplified_zone = transport_zone.simplify(10)
    
    # Zapis
    spatial_dir = city_dir / "02_spatial"
    spatial_dir.mkdir(parents=True, exist_ok=True)
    
    zone_gdf = gpd.GeoDataFrame(geometry=[simplified_zone], crs="EPSG:2180").to_crs("EPSG:4326")
    zone_gdf.to_file(city_dir / "transport_zone.gpkg", driver="GPKG")
    
    stops_output = spatial_dir / "stops.gpkg"
    final_city_stops.to_crs("EPSG:4326").to_file(stops_output, driver="GPKG")
    
    print(f"  [OK] {city_name}: Baza gotowa ({len(final_city_stops)} przystanków).")
    return final_city_stops

def main():
    print("=== START URBAN GRAVITY ENGINE (Faza 2: Ciasne Strefy) ===")
    allowed_cities = get_allowed_cities()
    
    cities = []
    if CITIES_ROOT.exists():
        cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
        
    all_poland_smart = []
    
    # KRYTYCZNE: Ładujemy globalną kolej raz, żeby nie mielić Polski 29 razy
    print("Ładowanie globalnej sieci kolejowej (IC, PR)...")
    global_rail_gdf = load_global_rail_stops(CITIES_ROOT)
    if not global_rail_gdf.empty:
        print(f"  Gotowe. Załadowano {len(global_rail_gdf)} stacji krajowych.")
    else:
        print("  Brak danych globalnej kolei.")

    for city_dir in cities:
        if allowed_cities and city_dir.name not in allowed_cities:
            continue
        res = process_city_smart(city_dir, global_rail_gdf)
        if res is not None:
            all_poland_smart.append(res)

    if all_poland_smart:
        combined = pd.concat(all_poland_smart, ignore_index=True)
        ALL_STOPS_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        combined.to_crs("EPSG:4326").to_file(ALL_STOPS_OUTPUT, driver="GPKG")
        print(f"\nSukces! Wygenerowano Smart Stops dla {len(all_poland_smart)} aglomeracji.")
        print(f"Globalna baza: {len(combined)} przystanków.")

if __name__ == "__main__":
    main()
