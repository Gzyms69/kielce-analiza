import subprocess
import os
from pathlib import Path

# --- CONFIG ---
PBF_SOURCE = "data/poland/osm/poland-latest.osm.pbf"
CITIES_ROOT = Path("data/cities")

def extract_all():
    print("Inicjalizacja Wielkiej Ekstrakcji OSM (Full Context Ingestion)...")
    
    if not Path(PBF_SOURCE).exists():
        print(f"BŁĄD: Nie znaleziono pliku źródłowego {PBF_SOURCE}")
        return

    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    for i, city_dir in enumerate(cities, 1):
        city_name = city_dir.name
        zone_file = city_dir / "transport_zone.gpkg"
        output_gpkg = city_dir / "osm_full.gpkg"
        
        if not zone_file.exists():
            continue
            
        if output_gpkg.exists():
            # print(f"  [{i}/{len(cities)}] SKIP: {city_name}")
            continue

        print(f"[{i}/{len(cities)}] Ekstrakcja OSM dla: {city_name}...", flush=True)
        
        try:
            # Używamy ogr2ogr do wycięcia po poligonie (clipsrc)
            # -nlt PROMOTE_TO_MULTI zapewnia spójność typów geometrii
            # -gt 65536 przyspiesza zapis do SQLite
            subprocess.run([
                "ogr2ogr",
                "-f", "GPKG",
                str(output_gpkg),
                PBF_SOURCE,
                "-clipsrc", str(zone_file),
                "-gt", "65536",
                "-nlt", "PROMOTE_TO_MULTI",
                "-oo", "CONFIG_FILE=scripts/osmconf.ini" # Jeśli istnieje, użyjemy go dla lepszych kolumn
            ], check=True, capture_output=True)
            print(f"  [SUCCESS] Utworzono {output_gpkg.name}")
            
        except subprocess.CalledProcessError as e:
            print(f"  [ERROR] {city_name} (Kod: {e.returncode}): {e.stderr.decode().strip()}")
        except Exception as e:
            print(f"  [ERROR] {city_name}: {e}")

if __name__ == "__main__":
    extract_all()
