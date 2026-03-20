import geopandas as gpd
import pandas as pd
from pathlib import Path
import os

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def get_allowed_cities():
    cities_env = os.environ.get("PIPELINE_CITIES")
    if cities_env:
        return [c.strip() for c in cities_env.split(',')]
    return None

def permanent_unify_city(city_name, data_dir):
    # KOREKTA: Zawsze szukamy w 02_spatial (standard Hub 2.0)
    rcn_path = data_dir / "cities" / city_name / "02_spatial" / "transactions.gpkg"
    
    if not rcn_path.exists():
        # Fallback dla starszych testów
        rcn_path = data_dir / "cities" / city_name / "rcn" / "transactions.gpkg"
        
    if not rcn_path.exists():
        print(f"    [SKIP] Nie znaleziono bazy transakcji dla {city_name} (szukano w 02_spatial i rcn/)")
        return False
    
    print(f"  Unifying {city_name} ({rcn_path.relative_to(data_dir)})...")
    try:
        rcn = gpd.read_file(rcn_path)
        if rcn.empty:
            print("    [EMPTY] Baza jest pusta.")
            return True
            
        # 1. Ensure lok_pow_uzyt exists
        mapped = False
        if 'lok_pow_uzyt' not in rcn.columns:
            # Mapujemy wszystkie znane nazwy kolumn powierzchniowych na nasz standard
            for col in ['pow_uzytkowa', 'pow_lokalu', 'nier_pow_uzyt', 'm2', 'powUzytkowaLokalu']:
                if col in rcn.columns:
                    rcn['lok_pow_uzyt'] = rcn[col]
                    print(f"    [MAP] Mapowanie kolumny {col} -> lok_pow_uzyt")
                    mapped = True
                    break
        else:
            mapped = True
        
        if not mapped:
            print(f"    [ERR] Brak kolumny powierzchniowej w {city_name}. Kolumny: {rcn.columns.tolist()}")
            return False

        # 2. Convert to Numeric
        rcn['tran_cena_brutto'] = pd.to_numeric(rcn['tran_cena_brutto'], errors='coerce')
        rcn['lok_pow_uzyt'] = pd.to_numeric(rcn['lok_pow_uzyt'], errors='coerce')
        
        # 3. Calculate price_m2 (VECTORIZED)
        mask = (rcn['lok_pow_uzyt'] > 5) & (rcn['tran_cena_brutto'] > 0)
        rcn['price_m2'] = None
        rcn.loc[mask, 'price_m2'] = rcn.loc[mask, 'tran_cena_brutto'] / rcn.loc[mask, 'lok_pow_uzyt']
        
        # 4. Save back
        rcn.to_file(rcn_path, driver="GPKG", layer="transactions")
        print(f"    [OK] Zapisano price_m2 dla {len(rcn[mask])} rekordów.")
        return True
    except Exception as e:
        print(f"    Error in {city_name}: {e}")
        return False

if __name__ == "__main__":
    print("=== TASK 1.7: PERMANENT LOCAL SCHEMA UNIFICATION ===\n")
    data_dir = get_data_dir()
    allowed_cities = get_allowed_cities()
    
    cities_root = data_dir / "cities"
    if not cities_root.exists(): exit(0)
    
    cities = sorted([d.name for d in cities_root.iterdir() if d.is_dir()])
    for city in cities:
        if allowed_cities and city not in allowed_cities:
            continue
        permanent_unify_city(city, data_dir)
    print("\nLocal schemas hardened and unified.")
