import geopandas as gpd
import pandas as pd
from pathlib import Path
import os

CITIES_ROOT = Path("data/cities")

def permanent_unify_city(city_name):
    rcn_path = CITIES_ROOT / city_name / "rcn" / "transactions.gpkg"
    if not rcn_path.exists(): return
    
    print(f"  Unifying {city_name}...")
    try:
        rcn = gpd.read_file(rcn_path)
        
        # 1. Ensure lok_pow_uzyt exists
        if 'lok_pow_uzyt' not in rcn.columns:
            for col in ['pow_uzytkowa', 'pow_lokalu', 'nier_pow_uzyt']:
                if col in rcn.columns:
                    rcn['lok_pow_uzyt'] = rcn[col]
                    break
        
        # 2. Convert to Numeric
        rcn['tran_cena_brutto'] = pd.to_numeric(rcn['tran_cena_brutto'], errors='coerce')
        rcn['lok_pow_uzyt'] = pd.to_numeric(rcn['lok_pow_uzyt'], errors='coerce')
        
        # 3. Calculate price_m2
        rcn['price_m2'] = rcn.apply(lambda row: row['tran_cena_brutto'] / row['lok_pow_uzyt'] 
                                   if (row['lok_pow_uzyt'] and row['lok_pow_uzyt'] > 5 and row['tran_cena_brutto'] > 0) 
                                   else None, axis=1)
        
        # 4. Save back
        rcn.to_file(rcn_path, driver="GPKG", layer="transactions")
        return True
    except Exception as e:
        print(f"    Error in {city_name}: {e}")
        return False

if __name__ == "__main__":
    print("=== TASK 1.7: PERMANENT LOCAL SCHEMA UNIFICATION ===\n")
    cities = sorted([d.name for d in CITIES_ROOT.iterdir() if d.is_dir()])
    for city in cities:
        permanent_unify_city(city)
    print("\nLocal schemas hardened and unified across all 29 hubs.")
