import subprocess
import os
import concurrent.futures
from pathlib import Path
import geopandas as gpd

# --- CONFIG ---
PBF_SOURCE = "data/poland/osm/poland-latest.osm.pbf"
CITIES_ROOT = Path("data/cities")
MAX_WORKERS = 5

def process_city_turbo(city_dir):
    city_name = city_dir.name
    zone_file = city_dir / "transport_zone.gpkg"
    output_gpkg = city_dir / "osm_full.gpkg"
    temp_pbf = city_dir / "temp_extract.pbf"
    temp_geojson = city_dir / "zone.geojson"
    
    if not zone_file.exists(): return f"[SKIP] {city_name}: Brak transport_zone.gpkg"
    if output_gpkg.exists(): return f"[SKIP] {city_name}: Istnieje"

    try:
        # 1. Konwersja wykrojnika do GeoJSON (wymagane przez osmium extract)
        zone_gdf = gpd.read_file(zone_file)
        zone_gdf.to_file(temp_geojson, driver='GeoJSON')

        # 2. OSMIUM: Szybkie wycinanie po POLIGONIE (zamiast BBOX)
        # To jest tysiące razy szybsze niż wycinanie w GDAL
        subprocess.run([
            "osmium", "extract",
            "-p", str(temp_geojson),
            str(PBF_SOURCE),
            "-o", str(temp_pbf),
            "--overwrite"
        ], check=True, capture_output=True)

        # 3. OGR2OGR: Błyskawiczna konwersja gotowego wycinka
        # Już bez -clipsrc, bo dane są już docięte przez osmium
        subprocess.run([
            "ogr2ogr",
            "-f", "GPKG",
            str(output_gpkg),
            str(temp_pbf),
            "-oo", "CONFIG_FILE=scripts/core/osmconf.ini",
            "-gt", "65536",
            "-nlt", "PROMOTE_TO_MULTI"
        ], check=True, capture_output=True)

        # Sprzątanie
        for f in [temp_pbf, temp_geojson]:
            if f.exists(): f.unlink()
        
        return f"[SUCCESS] {city_name}"

    except subprocess.CalledProcessError as e:
        return f"[ERROR] {city_name}: {e.stderr.decode()}"
    except Exception as e:
        return f"[ERROR] {city_name}: {e}"

if __name__ == "__main__":
    # To jest wersja modułowa, wywoływana przez benchmark lub main
    pass
