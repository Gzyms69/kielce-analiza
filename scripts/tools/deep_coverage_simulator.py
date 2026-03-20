import pandas as pd
import geopandas as gpd
from pathlib import Path
from shapely.ops import unary_union
import warnings
import json
import time
import concurrent.futures
import re
import unicodedata

warnings.filterwarnings("ignore")

ROOT_DIR = Path("data")
CITIES_ROOT = ROOT_DIR / "cities"
POWIATY_PATH = ROOT_DIR / "poland" / "admin" / "powiaty.json"
POP_PATH = ROOT_DIR / "poland" / "population" / "nsp2021_grid250m.gpkg"

RAIL_KEYWORDS = ['pkp', 'kolej', 'rail', 'lka', 'wkd', 'skm']

def normalize_name(name):
    n = str(name).lower()
    n = ''.join(c for c in unicodedata.normalize('NFD', n) if unicodedata.category(c) != 'Mn')
    n = re.sub(r'glown[ya]', '', n)
    n = re.sub(r'osobow[ya]', '', n)
    return re.sub(r'[^a-z0-9]', '', n)

def process_city_coverage(args):
    city_dir, global_rail_gdf, powiaty, pop = args
    city_name = city_dir.name
    
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
            if 'stop_lat' not in df.columns or 'stop_lon' not in df.columns: continue
            
            gdf = gpd.GeoDataFrame(
                df[['stop_id', 'stop_name', 'stop_lat', 'stop_lon']],
                geometry=gpd.points_from_xy(df.stop_lon, df.stop_lat),
                crs="EPSG:4326"
            ).to_crs("EPSG:2180")
            gdf['source'] = source_dir.name
            
            if any(k in source_dir.name.lower() for k in RAIL_KEYWORDS):
                rail_stops.append(gdf)
            else:
                urban_stops.append(gdf)
        except: pass
        
    if not urban_stops:
        return None
        
    if not global_rail_gdf.empty:
        rail_stops.append(global_rail_gdf)
        
    # 1. SCENARIUSZ: BEZ WYCINANIA (BLIND)
    all_stops_list = urban_stops + rail_stops
    all_stops_gdf = pd.concat(all_stops_list, ignore_index=True) if all_stops_list else None
    
    blind_teryt = []
    blind_pop = 0
    t_col = 'JPT_KOD_JE' if 'JPT_KOD_JE' in powiaty.columns else powiaty.columns[0]

    if all_stops_gdf is not None and not all_stops_gdf.empty:
        blind_zone = all_stops_gdf.geometry.buffer(1500).unary_union
        intersecting_blind = powiaty[powiaty.intersects(blind_zone)]
        blind_teryt = sorted(intersecting_blind[t_col].tolist())
        pop_in_blind = pop[pop.intersects(blind_zone)]
        blind_pop = pop_in_blind['TOT'].sum()

    # 2. SCENARIUSZ: NOWA INTELIGENTNA LOGIKA (SMART CUT)
    smart_teryt = []
    smart_pop = 0
    urban_count = 0
    rail_total_count = 0
    rail_kept_count = 0
    
    if urban_stops:
        urban_gdf = pd.concat(urban_stops, ignore_index=True)
        urban_count = len(urban_gdf)
        urban_footprint = urban_gdf.geometry.buffer(3000).unary_union
        
        filtered_rail = []
        if rail_stops:
            all_rail_gdf = pd.concat(rail_stops, ignore_index=True)
            rail_total_count = len(all_rail_gdf)
            valid_rail = all_rail_gdf[all_rail_gdf.geometry.intersects(urban_footprint)]
            if not valid_rail.empty:
                filtered_rail.append(valid_rail)
                rail_kept_count = len(valid_rail)
        
        final_stops = [urban_gdf] + filtered_rail
        final_gdf = pd.concat(final_stops, ignore_index=True)
        
        smart_zone = final_gdf.geometry.buffer(1500).unary_union
        
        intersecting_smart = powiaty[powiaty.intersects(smart_zone)]
        smart_teryt = sorted(intersecting_smart[t_col].tolist())
        
        pop_in_smart = pop[pop.intersects(smart_zone)]
        smart_pop = pop_in_smart['TOT'].sum()
        
    return {
        "city": city_name,
        "urban_stops": urban_count,
        "rail_total": rail_total_count,
        "rail_kept": rail_kept_count,
        "rail_cut": rail_total_count - rail_kept_count,
        "blind_teryt_count": len(blind_teryt),
        "smart_teryt_count": len(smart_teryt),
        "blind_pop": blind_pop,
        "smart_pop": smart_pop,
        "teryt_saved": len(blind_teryt) - len(smart_teryt)
    }

def analyze():
    print("=== DEEP COVERAGE SIMULATOR (RÓWNOLEGŁY) ===")
    
    if not POWIATY_PATH.exists():
        print("Brak powiaty.json")
        return
        
    print("Ładowanie granic powiatów...")
    powiaty = gpd.read_file(POWIATY_PATH).to_crs("EPSG:2180")
    
    print("Ładowanie siatki populacji (tylko centroidy)...")
    try:
        pop = gpd.read_file(POP_PATH)
        if 'TOT' not in pop.columns:
            pop['TOT'] = pop.get('TOT', 0)
        pop = pop.to_crs("EPSG:2180")
        pop.geometry = pop.centroid
    except Exception as e:
        print(f"Błąd ładowania populacji: {e}")
        return

    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    print("Ładowanie globalnej sieci kolejowej (IC, PR)...")
    global_rail_gdfs = []
    global_rail_root = CITIES_ROOT / "rail" / "gtfs"
    if global_rail_root.exists():
        for source_dir in global_rail_root.iterdir():
            if not source_dir.is_dir(): continue
            stops_file = source_dir / "stops.txt"
            if not stops_file.exists(): continue
            try:
                df = pd.read_csv(stops_file)
                if 'stop_lat' not in df.columns or 'stop_lon' not in df.columns: continue
                gdf = gpd.GeoDataFrame(
                    df[['stop_id', 'stop_name', 'stop_lat', 'stop_lon']],
                    geometry=gpd.points_from_xy(df.stop_lon, df.stop_lat),
                    crs="EPSG:4326"
                ).to_crs("EPSG:2180")
                gdf['source'] = source_dir.name
                global_rail_gdfs.append(gdf)
            except: pass
            
    if global_rail_gdfs:
        all_rail = pd.concat(global_rail_gdfs, ignore_index=True)
        all_rail['norm_name'] = all_rail['stop_name'].apply(normalize_name)
        all_rail['lat_grid'] = all_rail['stop_lat'].round(2)
        all_rail['lon_grid'] = all_rail['stop_lon'].round(2)
        global_rail_gdf = all_rail.drop_duplicates(subset=['norm_name', 'lat_grid', 'lon_grid'])
        print(f"  Gotowe. Załadowano {len(global_rail_gdf)} zdeduplikowanych stacji krajowych.")
    else:
        global_rail_gdf = gpd.GeoDataFrame()
        print("  Brak stacji krajowych.")
        
    print(f"Uruchamianie wielowątkowej analizy dla {len(cities)} miast...")
    
    # Przygotowanie argumentów dla workera
    args_list = []
    for city_dir in cities:
        if city_dir.name == "rail": continue
        args_list.append((city_dir, global_rail_gdf, powiaty, pop))
        
    results = []
    import multiprocessing
    # Używamy ProcessPoolExecutor dla pełnego zrównoleglenia (CPU-bound zadania Shapely)
    # Wykorzystujemy wszystkie dostępne rdzenie
    workers = multiprocessing.cpu_count()
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        for res in executor.map(process_city_coverage, args_list):
            if res:
                results.append(res)
                print(f"  [OK] Zakończono symulację dla: {res['city']}")

    print("\n\n=== RAPORT Z PRZETWARZANIA GTFS (PODSUMOWANIE) ===")
    df = pd.DataFrame(results).sort_values('city')
    
    total_blind_teryt = df['blind_teryt_count'].sum()
    total_smart_teryt = df['smart_teryt_count'].sum()
    total_rail_cut = df['rail_cut'].sum()
    total_pop_smart = df['smart_pop'].sum()
    
    for _, r in df.iterrows():
        print(f"[{r['city'].upper()}]")
        print(f"  Przystanki miejskie: {r['urban_stops']} | PKP łącznie: {r['rail_total']} | PKP odrzucone (lasy): {r['rail_cut']}")
        print(f"  TERYT (Powiaty) -> Byłoby bez wycinania: {r['blind_teryt_count']} | JEST po cięciu: {r['smart_teryt_count']} (Uratowano {r['teryt_saved']} powiatów)")
        print(f"  Populacja objęta strefą: {r['smart_pop']:,.0f} mieszkańców")
        print("-" * 60)
        
    print(f"\n[GLOBALNE PODSUMOWANIE]")
    print(f"Całkowita liczba powiatów RCN bez odcinania kolei: {total_blind_teryt}")
    print(f"Całkowita liczba powiatów RCN Z INTELEGIENTNYM CIĘCIEM: {total_smart_teryt}")
    print(f"Różnica: Odrzucono {total_blind_teryt - total_smart_teryt} śmieciowych powiatów.")
    print(f"Odcięto {total_rail_cut} bezużytecznych stacji kolejowych na odludziach.")
    print(f"Całkowita populacja objęta ostatecznymi strefami transportowymi (w 29 aglomeracjach): {total_pop_smart:,.0f} ludzi.")

if __name__ == "__main__":
    start = time.time()
    analyze()
    print(f"\nCzas analizy: {time.time() - start:.1f}s")
