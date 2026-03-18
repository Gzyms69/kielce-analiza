import geopandas as gpd
import json
from pathlib import Path

POWIATY_PATH = Path("data/poland/admin/powiaty.json")
CITIES_ROOT = Path("data/cities")

def identify_targets():
    print("=== IDENTYFIKACJA POWIATÓW DLA RCN (Spatial Join) ===")
    
    if not POWIATY_PATH.exists():
        print(f"BŁĄD: Nie znaleziono pliku {POWIATY_PATH}")
        return

    # Wczytujemy granice powiatów i rzutujemy na układ metryczny
    print("Wczytywanie granic powiatów...")
    powiaty = gpd.read_file(POWIATY_PATH).to_crs("EPSG:2180")
    
    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    for city_dir in cities:
        city_name = city_dir.name
        zone_path = city_dir / "transport_zone.gpkg"
        
        if not zone_path.exists():
            continue
            
        try:
            # Wczytujemy wykrojnik miasta
            zone = gpd.read_file(zone_path).to_crs("EPSG:2180")
            
            # Znajdujemy powiaty, które przecinają się z naszym miastem
            # Używamy unary_union dla pewności, że sprawdzamy cały obszar
            intersecting = powiaty[powiaty.intersects(zone.union_all())]
            
            # Wyciągamy kody TERYT (zakładamy standardową nazwę kolumny JPT_KOD_JE)
            # Jeśli kolumna nazywa się inaczej, skrypt spróbuje ją znaleźć
            teryt_col = 'JPT_KOD_JE' if 'JPT_KOD_JE' in intersecting.columns else intersecting.columns[0]
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
