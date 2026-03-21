import pandas as pd
import geopandas as gpd
from pathlib import Path
import warnings
import json
import time
import concurrent.futures
import re
import unicodedata
import multiprocessing
import gc
import os

warnings.filterwarnings("ignore")

# --- KONFIGURACJA ---
DATA_DIR = Path("data")
CITIES_ROOT = DATA_DIR / "cities"
POWIATY_PATH = DATA_DIR / "poland" / "admin" / "powiaty.json"
POP_PATH = DATA_DIR / "poland" / "population" / "nsp2021_grid250m.gpkg"
RAIL_KEYWORDS = ['pkp', 'kolej', 'rail', 'lka', 'wkd', 'skm']

# ZMIENNE GLOBALNE (Współdzielone w pamięci na Linuxie przez fork)
GLOBAL_POWIATY = None
GLOBAL_POP = None
GLOBAL_RAIL = None

def init_worker(powiaty_gdf, pop_gdf, rail_gdf):
    """Opcjonalna inicjalizacja dla systemów non-fork, na Linuxie zadziała dziedziczenie globali."""
    global GLOBAL_POWIATY, GLOBAL_POP, GLOBAL_RAIL
    GLOBAL_POWIATY = powiaty_gdf
    GLOBAL_POP = pop_gdf
    GLOBAL_RAIL = rail_gdf

def process_city_coverage(city_name):
    """
    Worker wykonujący analizę dla jednego miasta.
    Korzysta z globalnych GDFów załadowanych RAZ w pamięci.
    """
    city_dir = CITIES_ROOT / city_name
    gtfs_root = city_dir / "gtfs"
    if not gtfs_root.exists(): return None

    # 1. Ładowanie lokalnych przystanków
    urban_stops = []
    local_rail = []
    
    for source_dir in gtfs_root.iterdir():
        if not source_dir.is_dir(): continue
        stops_file = source_dir / "stops.txt"
        if not stops_file.exists(): continue
        try:
            df = pd.read_csv(stops_file)
            gdf = gpd.GeoDataFrame(
                df, geometry=gpd.points_from_xy(df.stop_lon, df.stop_lat), crs="EPSG:4326"
            ).to_crs("EPSG:2180")
            
            if any(k in source_dir.name.lower() for k in RAIL_KEYWORDS):
                local_rail.append(gdf)
            else:
                urban_stops.append(gdf)
        except: pass

    if not urban_stops: return None
    
    urban_gdf = pd.concat(urban_stops, ignore_index=True)
    all_rail_gdf = pd.concat(local_rail + [GLOBAL_RAIL], ignore_index=True) if (local_rail or not GLOBAL_RAIL.empty) else gpd.GeoDataFrame()

    # --- OBLICZENIA SPATIAL ---
    
    # SCENARIUSZ A: BLIND (Wszystko w promieniu 1.5km)
    blind_stops = pd.concat([urban_gdf, all_rail_gdf], ignore_index=True)
    # buffer().union_all() jest szybkie dla kilku tysięcy punktów
    blind_zone = gpd.GeoDataFrame(geometry=[blind_stops.buffer(1500).union_all()], crs="EPSG:2180")
    
    # TERYT (Spatial Join z powiatami)
    blind_teryt = gpd.sjoin(GLOBAL_POWIATY, blind_zone, how="inner")
    blind_teryt_count = len(blind_teryt['JPT_KOD_JE'].unique()) if 'JPT_KOD_JE' in blind_teryt.columns else len(blind_teryt)
    
    # POPULACJA (Spatial Join z punktami populacji - BARDZO SZYBKIE)
    pop_in_blind = gpd.sjoin(GLOBAL_POP, blind_zone, how="inner")
    blind_pop_total = pop_in_blind['TOT'].sum()

    # SCENARIUSZ B: SMART CUT (Tylko kolej blisko miasta)
    urban_footprint = gpd.GeoDataFrame(geometry=[urban_gdf.buffer(3000).union_all()], crs="EPSG:2180")
    
    # Wycinamy tylko te stacje PKP, które leżą w urban_footprint
    valid_rail = gpd.sjoin(all_rail_gdf, urban_footprint, how="inner") if not all_rail_gdf.empty else gpd.GeoDataFrame()
    
    smart_stops = pd.concat([urban_gdf, valid_rail], ignore_index=True)
    smart_zone = gpd.GeoDataFrame(geometry=[smart_stops.buffer(1500).union_all()], crs="EPSG:2180")
    
    # TERYT Smart
    smart_teryt = gpd.sjoin(GLOBAL_POWIATY, smart_zone, how="inner")
    smart_teryt_count = len(smart_teryt['JPT_KOD_JE'].unique()) if 'JPT_KOD_JE' in smart_teryt.columns else len(smart_teryt)
    
    # POPULACJA Smart
    pop_in_smart = gpd.sjoin(GLOBAL_POP, smart_zone, how="inner")
    smart_pop_total = pop_in_smart['TOT'].sum()

    return {
        "city": city_name,
        "urban_stops": len(urban_gdf),
        "rail_total": len(all_rail_gdf),
        "rail_kept": len(valid_rail),
        "blind_teryt": blind_teryt_count,
        "smart_teryt": smart_teryt_count,
        "blind_pop": blind_pop_total,
        "smart_pop": smart_pop_total,
        "saved_teryt": blind_teryt_count - smart_teryt_count
    }

def analyze():
    print("=== DEEP COVERAGE SIMULATOR 2.0 (SINGLE-LOAD ARCHITECTURE) ===")
    
    # 1. ŁADOWANIE DANYCH (RAZ NA CAŁY PROCES)
    print(f"Wczytywanie powiatów...")
    powiaty = gpd.read_file(POWIATY_PATH).to_crs("EPSG:2180")
    
    print(f"Wczytywanie siatki populacji (Konwersja na Centroidy)...")
    pop = gpd.read_file(POP_PATH).to_crs("EPSG:2180")
    pop.geometry = pop.centroid # To klucz do wydajności sjoin
    print(f"  [OK] Siatka populacji gotowa ({len(pop)} punktów).")

    print(f"Wczytywanie globalnej sieci kolejowej...")
    rail_list = []
    rail_root = CITIES_ROOT / "rail" / "gtfs"
    if rail_root.exists():
        for d in rail_root.iterdir():
            f = d / "stops.txt"
            if f.exists():
                try:
                    df = pd.read_csv(f)
                    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.stop_lon, df.stop_lat), crs="EPSG:4326").to_crs("EPSG:2180")
                    rail_list.append(gdf)
                except: pass
    global_rail = pd.concat(rail_list, ignore_index=True) if rail_list else gpd.GeoDataFrame()
    # Lekka deduplikacja stacji (siatka 500m)
    if not global_rail.empty:
        global_rail['gx'] = (global_rail.geometry.x / 500).round()
        global_rail['gy'] = (global_rail.geometry.y / 500).round()
        global_rail = global_rail.drop_duplicates(subset=['gx', 'gy'])
    print(f"  [OK] Załadowano {len(global_rail)} stacji krajowych.")

    # 2. URUCHOMIENIE ANALIZY (Wielowątkowość z dzieleniem pamięci)
    cities = sorted([d.name for d in CITIES_ROOT.iterdir() if d.is_dir() and d.name != "rail"])
    
    # Używamy 4 workerów - przy 32GB RAM to optymalne, siatka zajmuje ok 1GB, sjoiny są CPU-bound
    workers = 4
    results = []
    
    print(f"\nUruchamianie analizy dla {len(cities)} miast na {workers} procesach...")
    
    # Wykorzystujemy 'initializer' by na każdym systemie (nie tylko Linux) dane były dostępne globalnie
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, 
        initializer=init_worker, 
        initargs=(powiaty, pop, global_rail)
    ) as executor:
        futures = {executor.submit(process_city_coverage, city): city for city in cities}
        
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            city = futures[future]
            try:
                res = future.result()
                if res:
                    results.append(res)
                    print(f"  [{i+1}/{len(cities)}] Sukces: {city}")
            except Exception as e:
                print(f"  [{i+1}/{len(cities)}] BŁĄD w {city}: {e}")

    # 3. RAPORT KOŃCOWY
    print("\n" + "="*80)
    print(f"{'MIASTO':15} | {'PRZYST':7} | {'PKP(T/K)':10} | {'POW(B/S)':10} | {'POPULACJA (SMART)':15}")
    print("-" * 80)
    
    df = pd.DataFrame(results).sort_values('city')
    for _, r in df.iterrows():
        pkp_str = f"{r['rail_total']}/{r['rail_kept']}"
        pow_str = f"{r['blind']}/{r['smart']}" if 'blind' in r else f"{r['blind_teryt']}/{r['smart_teryt']}"
        print(f"{r['city'][:15]:15} | {r['urban_stops']:7} | {pkp_str:10} | {pow_str:10} | {r['smart_pop']:,.0f}")

    total_saved = df['saved_teryt'].sum()
    print("="*80)
    print(f"ŁĄCZNIE ZAOSZCZĘDZONO: {total_saved} POWIATÓW (Odrzucone lasy i pustostany PKP).")
    print(f"CAŁKOWITA POPULACJA W STREFACH: {df['smart_pop'].sum():,.0f} osób.")

if __name__ == "__main__":
    start_time = time.time()
    analyze()
    print(f"\nAnaliza ukończona w {time.time() - start_time:.1f} sekund.")
