import geopandas as gpd
import json
import os
from pathlib import Path

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def get_allowed_cities():
    cities_env = os.environ.get("PIPELINE_CITIES")
    if cities_env:
        return [c.strip() for c in cities_env.split(',')]
    return None

def identify_targets():
    print("=== IDENTYFIKACJA POWIATÓW DLA RCN (Spatial Join) ===")
    POWIATY_PATH = get_data_dir() / "poland" / "admin" / "powiaty.json"
    CITIES_ROOT = get_data_dir() / "cities"
    
    if not POWIATY_PATH.exists():
        print(f"BŁĄD: Nie znaleziono pliku {POWIATY_PATH}")
        return

    # Wczytujemy granice powiatów i rzutujemy na układ metryczny
    print("Wczytywanie granic powiatów...")
    powiaty = gpd.read_file(POWIATY_PATH).to_crs("EPSG:2180")
    
    if not CITIES_ROOT.exists():
        print("Brak folderu cities.")
        return

    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    allowed_cities = get_allowed_cities()
    
    for city_dir in cities:
        city_name = city_dir.name
        
        if allowed_cities and city_name not in allowed_cities:
            continue
            
        zone_path = city_dir / "transport_zone.gpkg"
        
        if not zone_path.exists():
            print(f"[SKIP] {city_name}: brak transport_zone.gpkg")
            continue
            
        try:
            # Wczytujemy wykrojnik miasta
            zone = gpd.read_file(zone_path).to_crs("EPSG:2180")
            
            # Znajdujemy powiaty, które przecinają się z naszym miastem
            # Używamy unary_union dla pewności, że sprawdzamy cały obszar
            intersecting = powiaty[powiaty.intersects(zone.union_all())]
            
            # Wyciagamy kody TERYT - szukamy kolumny zawierajacej kody administracyjne
            teryt_col = None
            teryt_candidates = ['JPT_KOD_JE', 'jpt_kod_je', 'TERYT', 'teryt', 'KOD_TERYT', 'kod']
            for candidate in teryt_candidates:
                if candidate in intersecting.columns:
                    teryt_col = candidate
                    break
            
            if teryt_col is None:
                # Heurystyka: szukaj kolumny z 4-cyfrowymi kodami
                for col in intersecting.columns:
                    if col == 'geometry':
                        continue
                    sample_vals = intersecting[col].dropna().head(5).astype(str)
                    if len(sample_vals) > 0 and sample_vals.str.match(r'^\d{4}$').all():
                        teryt_col = col
                        break
            
            if teryt_col is None:
                print(f"[CRITICAL] {city_name}: Nie znaleziono kolumny TERYT! Kolumny: {intersecting.columns.tolist()}")
                continue
            
            teryt_list = sorted(intersecting[teryt_col].tolist())
            
            # Zapisujemy listę do pliku JSON w folderze miasta
            output_path = city_dir / "rcn_targets.json"
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(teryt_list, f, indent=2)
                
            print(f"[OK] {city_name.ljust(15)} | Powiaty: {len(teryt_list)} | TERYT: {', '.join(teryt_list)}")
            
        except Exception as e:
            print(f"[ERR] {city_name}: {e}")

if __name__ == "__main__":
    identify_targets()
