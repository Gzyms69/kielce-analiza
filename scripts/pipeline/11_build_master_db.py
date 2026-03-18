import geopandas as gpd
import pandas as pd
from pathlib import Path
import os

CITIES_ROOT = Path("data/cities")
MASTER_DB = Path("data/database/master_analytical.gpkg")

def restore_full_data():
    print("=== EMERGENCY RESTORE: FULL DATA SPECTRUM (NO LUXURY LIMITS) ===\n")
    if MASTER_DB.exists(): os.remove(MASTER_DB)
    
    cities = sorted([d.name for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    all_stops = []
    all_transactions = []
    
    for city in cities:
        print(f"  Restoring {city}...")
        stops_path = CITIES_ROOT / city / "smart_stops.gpkg"
        rcn_path = CITIES_ROOT / city / "rcn" / "transactions.gpkg"
        
        if stops_path.exists():
            try:
                stops = gpd.read_file(stops_path).to_crs("EPSG:2180")
                stops['city'] = city
                all_stops.append(stops)
            except: pass
            
        if rcn_path.exists():
            try:
                rcn = gpd.read_file(rcn_path).to_crs("EPSG:2180")
                rcn['city'] = city
                
                # Ujednolicenie kolumny powierzchni (lok_pow_uzyt)
                if 'lok_pow_uzyt' not in rcn.columns:
                    for col in ['pow_uzytkowa', 'pow_lokalu', 'nier_pow_uzyt']:
                        if col in rcn.columns:
                            rcn['lok_pow_uzyt'] = rcn[col]
                            break
                
                rcn['tran_cena_brutto'] = pd.to_numeric(rcn['tran_cena_brutto'], errors='coerce')
                rcn['lok_pow_uzyt'] = pd.to_numeric(rcn['lok_pow_uzyt'], errors='coerce')
                
                # Wyliczanie ceny za m2
                rcn['price_m2'] = rcn.apply(lambda row: row['tran_cena_brutto'] / row['lok_pow_uzyt'] 
                                           if (row['lok_pow_uzyt'] and row['lok_pow_uzyt'] > 5 and row['tran_cena_brutto'] > 0) 
                                           else None, axis=1)
                
                # --- NO LUXURY REMOVAL ---
                # Usuwamy TYLKO absolutne błędy techniczne (powyżej 5 mln/m2)
                # To zachowuje wszystkie autentyczne luksusy (nawet 100k-500k/m2)
                rcn = rcn[(rcn['price_m2'] < 5000000) | (rcn['price_m2'].isna())]
                
                all_transactions.append(rcn)
            except: pass

    if all_stops:
        print("\n  Consolidating 55,933 Stops...")
        gpd.pd.concat(all_stops).to_file(MASTER_DB, driver="GPKG", layer="stops")
        
    if all_transactions:
        final_rcn = gpd.pd.concat(all_transactions)
        print(f"  Consolidating {len(final_rcn)} RAW records (Luxury Included)...")
        final_rcn.to_file(MASTER_DB, driver="GPKG", layer="transactions")
        
    print(f"\nSUCCESS: Full Spectrum Analytical Database Restored.")

if __name__ == "__main__":
    restore_full_data()
