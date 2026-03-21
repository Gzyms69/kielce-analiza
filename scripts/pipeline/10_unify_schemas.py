import geopandas as gpd
import pandas as pd
from pathlib import Path
import os
import argparse
import json
import tempfile

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def permanent_unify_city(city_name, data_dir):
    rcn_path = data_dir / "cities" / city_name / "02_spatial" / "transactions.gpkg"
    
    if not rcn_path.exists():
        print(f"    [SKIP] Nie znaleziono bazy transakcji dla {city_name}.")
        return False
    
    try:
        rcn = gpd.read_file(rcn_path)
        if rcn.empty:
            print("    [EMPTY] Baza jest pusta.")
            return True
            
        mapped = False
        if 'lok_pow_uzyt' not in rcn.columns:
            for col in ['pow_uzytkowa', 'pow_lokalu', 'nier_pow_uzyt', 'm2', 'powUzytkowaLokalu']:
                if col in rcn.columns:
                    rcn['lok_pow_uzyt'] = rcn[col]
                    mapped = True
                    break
        else:
            mapped = True
        
        if not mapped:
            print(f"    [ERR] Brak kolumny powierzchniowej w {city_name}.")
            return False

        rcn['tran_cena_brutto'] = pd.to_numeric(rcn['tran_cena_brutto'], errors='coerce')
        rcn['lok_pow_uzyt'] = pd.to_numeric(rcn['lok_pow_uzyt'], errors='coerce')
        
        mask = (rcn['lok_pow_uzyt'] > 5) & (rcn['tran_cena_brutto'] > 0)
        rcn['price_m2'] = pd.NA # Inicjalizacja jako NA (numeric-friendly)
        rcn.loc[mask, 'price_m2'] = rcn.loc[mask, 'tran_cena_brutto'] / rcn.loc[mask, 'lok_pow_uzyt']
        
        # KRYTYCZNA POPRAWKA: Wymuszamy typ numeryczny (float) przed zapisem
        rcn['price_m2'] = pd.to_numeric(rcn['price_m2'], errors='coerce')
        valid_prices = rcn.loc[rcn['price_m2'].notna(), 'price_m2']
        
        avg_price = 0
        median_price = 0
        min_allowed = 0
        max_allowed = 0
        
        if not valid_prices.empty:
            # 1. Obliczamy twardą medianę z całości
            median_price = valid_prices.median()
            
            # 2. Dynamiczny Filtr Outlierów v7.8:
            # Usuwamy tylko absolutne absurdy (np. błędy urzędnika rzędu milionów/miliardów zł/m2)
            # Dopuszczamy ceny do 30-krotności mediany (np. 10k * 30 = 300k/m2)
            # Pozwala to zachować 100% luksusowych dzielnic przy jednoczesnym usunięciu śmieci.
            max_allowed = median_price * 30
            min_allowed = 500 # Poniżej 500 PLN/m2 to zazwyczaj błędy lub darowizny
            
            trimmed_prices = valid_prices[(valid_prices >= min_allowed) & (valid_prices <= max_allowed)]
            avg_price = trimmed_prices.mean()
        
        # ATOMIC WRITE: Zapis do pliku tymczasowego, potem atomowy rename
        tmp_fd, tmp_path = tempfile.mkstemp(suffix='.gpkg', dir=rcn_path.parent)
        os.close(tmp_fd)
        try:
            rcn.to_file(tmp_path, driver="GPKG", layer="transactions")
            os.replace(tmp_path, rcn_path)
        except Exception:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
            raise
        
        # POPRAWKA P2-3: Zapis zagregowanych statystyk do osobnego pliku
        stats_path = rcn_path.parent / "rcn_stats.json"
        with open(stats_path, "w", encoding="utf-8") as f:
            json.dump({
                "city": city_name,
                "total": len(rcn),
                "valid": len(valid_prices),
                "median_price_m2": round(median_price, 2),
                "trimmed_mean_m2": round(avg_price, 2),
                "min_valid": round(min_allowed, 2) if not valid_prices.empty else 0,
                "max_allowed": round(max_allowed, 2) if not valid_prices.empty else 0
            }, f, indent=2)
        
        metrics = {
            "city": city_name,
            "trans_total": len(rcn),
            "trans_valid": len(valid_prices),
            "avg_price_m2": round(avg_price, 0),
            "median_price_m2": round(median_price, 0)
        }
        print(f"__PIPELINE_METRICS__={json.dumps(metrics)}")
        return True
    except Exception as e:
        print(f"    [ERR] {city_name}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", help="Miasto do unifikacji", required=True)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    data_dir = get_data_dir()
    permanent_unify_city(args.city, data_dir)

if __name__ == "__main__":
    main()
