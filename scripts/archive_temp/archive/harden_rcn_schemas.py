import sqlite3
from pathlib import Path
import pandas as pd
import geopandas as gpd

CITIES_ROOT = Path("data/cities")

def harden_city_schema(city_name):
    gpkg_path = CITIES_ROOT / city_name / "rcn" / "transactions.gpkg"
    if not gpkg_path.exists(): return
    
    print(f"  Hardening {city_name}...")
    try:
        # Wczytujemy wszystko do GeoPandas (to najbezpieczniejszy sposób na zmianę typów)
        gdf = gpd.read_file(gpkg_path)
        
        # Konwersja kolumny ceny na numeryczną
        if 'tran_cena_brutto' in gdf.columns:
            gdf['tran_cena_brutto'] = pd.to_numeric(gdf['tran_cena_brutto'], errors='coerce')
            # Usuwamy rekordy bez ceny
            gdf = gdf.dropna(subset=['tran_cena_brutto'])
            
        # Zapisujemy z powrotem, wymuszając nadpisanie i czysty schemat
        gdf.to_file(gpkg_path, driver="GPKG", layer="transactions")
        return True
    except Exception as e:
        print(f"    Error hardening {city_name}: {e}")
        return False

def main():
    print("=== TASK 1.2: RCN SCHEMA HARDENING (TEXT -> REAL) ===\n")
    cities = sorted([d.name for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    success_count = 0
    for city in cities:
        if harden_city_schema(city):
            success_count += 1
            
    print(f"\nDone. Hardened {success_count} / {len(cities)} hubs.")

if __name__ == "__main__":
    main()
