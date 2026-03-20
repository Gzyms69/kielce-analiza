import subprocess
import geopandas as gpd
from pathlib import Path
import time
import os
import argparse
import sys

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def get_allowed_cities():
    cities_env = os.environ.get("PIPELINE_CITIES")
    if cities_env:
        return [c.strip() for c in cities_env.split(',')]
    return None

PBF_SOURCE = get_data_dir() / "poland" / "osm" / "poland-latest.osm.pbf"
CITIES_ROOT = get_data_dir() / "cities"
OSMCONF = Path("config/osmconf.ini")

def extract_city_infrastructure(city_dir, force=False):
    city_name = city_dir.name
    spatial_dir = city_dir / "02_spatial"
    
    # 02_spatial is the Hub 2.0 standard
    zone_file = city_dir / "transport_zone.gpkg"
    output_gpkg = spatial_dir / "infrastructure.gpkg"
    temp_pbf = spatial_dir / "temp_extract.pbf"
    temp_geojson = spatial_dir / "zone.geojson"
        
    if not zone_file.exists():
        print(f"[SKIP] {city_name}: Brak poligonu tnącego (transport_zone.gpkg)")
        return
        
    if output_gpkg.exists() and not force:
        print(f"[SKIP] {city_name}: Infrastruktura już istnieje. Użyj --force aby nadpisać.")
        return

    print(f"\n--- EKSTRAKCJA INFRASTRUKTURY (OSM SCALPEL): {city_name.upper()} ---")
    start_time = time.time()
    
    try:
        spatial_dir.mkdir(parents=True, exist_ok=True)
        
        # 1. Konwersja wykrojnika do GeoJSON (wymagane przez osmium extract -p)
        print(f"  [1/3] Przygotowanie poligonu tnącego...")
        zone_gdf = gpd.read_file(zone_file)
        zone_gdf.to_file(temp_geojson, driver='GeoJSON')
        
        # 2. OSMIUM: Szybkie wycinanie po POLIGONIE (zamiast BBOX)
        print(f"  [2/3] Osmium: Precyzyjne cięcie poligonem...")
        subprocess.run([
            "osmium", "extract",
            "-p", str(temp_geojson),
            str(PBF_SOURCE),
            "-o", str(temp_pbf),
            "--overwrite"
        ], check=True, capture_output=True)
        
        # 3. OGR2OGR: Błyskawiczna konwersja gotowego wycinka
        print(f"  [3/3] OGR2OGR: Generowanie bazy GPKG...")
        os.environ["OSM_CONFIG_FILE"] = str(OSMCONF)
        
        subprocess.run([
            "ogr2ogr", "-f", "GPKG", str(output_gpkg), str(temp_pbf),
            "-gt", "65536", 
            "-nlt", "PROMOTE_TO_MULTI",
            "-lco", "GEOMETRY_NAME=geometry",
            "-skipfailures"
        ], check=True, capture_output=True)
        
        # Czyszczenie
        for f in [temp_pbf, temp_geojson]:
            if f.exists(): f.unlink()
        
        duration = time.time() - start_time
        size = output_gpkg.stat().st_size / (1024*1024)
        print(f"  [OK] Sukces! Czas: {duration:.1f}s | Rozmiar: {size:.1f} MB")
        
    except subprocess.CalledProcessError as e:
        print(f"  [ERR] Błąd procesu zewnętrznego: {e.stderr.decode() if e.stderr else str(e)}")
    except Exception as e:
        print(f"  [ERR] Błąd krytyczny: {e}")

def main():
    parser = argparse.ArgumentParser(description="Ekstrakcja infrastruktury OSM dla aglomeracji.")
    parser.add_argument("--city", help="Nazwa konkretnego miasta do przetworzenia")
    parser.add_argument("--force", action="store_true", help="Nadpisz istniejące pliki")
    args = parser.parse_args()

    if not PBF_SOURCE.exists():
        print(f"BŁĄD: Brak źródłowego pliku PBF: {PBF_SOURCE}")
        sys.exit(1)

    if not OSMCONF.exists():
        print(f"BŁĄD: Brak pliku konfiguracyjnego: {OSMCONF}")
        sys.exit(1)

    allowed_cities = get_allowed_cities()

    if args.city:
        city_dir = CITIES_ROOT / args.city.lower()
        if city_dir.exists():
            if not allowed_cities or args.city.lower() in allowed_cities:
                extract_city_infrastructure(city_dir, force=args.force)
        else:
            print(f"BŁĄD: Nie znaleziono folderu dla miasta: {args.city}")
    else:
        print("=== URUCHAMIANIE EKSTRAKCJI NARODOWEJ (Idempotent) ===")
        if CITIES_ROOT.exists():
            cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
            for city_dir in cities:
                if allowed_cities and city_dir.name not in allowed_cities:
                    continue
                extract_city_infrastructure(city_dir, force=args.force)

if __name__ == "__main__":
    main()
