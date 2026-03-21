import geopandas as gpd
from pathlib import Path
from shapely.ops import unary_union

CITIES_ROOT = Path("data/cities")
STOPS_ALL = Path("data/poland/admin/all_stops.gpkg")

def generate_cutters():
    print("Wczytywanie bazy przystanków...")
    stops = gpd.read_file(STOPS_ALL)
    
    cities = stops['city'].unique()
    print(f"Generowanie wykrojników dla {len(cities)} aglomeracji...")

    for city in cities:
        print(f"  Przetwarzanie: {city}...", end=" ", flush=True)
        city_dir = CITIES_ROOT / city
        output_path = city_dir / "transport_zone.gpkg"
        
        if output_path.exists():
            print("POMINIĘTO (Istnieje)")
            continue

        # Wyciągamy przystanki dla miasta i rzutujemy na metry (EPSG:2180) dla równego bufora
        city_stops = stops[stops['city'] == city].to_crs("EPSG:2180")
        
        # Tworzymy bufory i łączymy je w jeden kształt
        buffer_zone = city_stops.geometry.buffer(1500)
        merged_poly = unary_union(buffer_zone)
        
        # Upraszczamy kształt (margines błędu 10m), aby przyspieszyć cięcie PBF
        simplified_poly = merged_poly.simplify(10)
        
        # Zapisujemy jako WGS84 (wymagane przez Osmium/GDAL)
        cutter = gpd.GeoDataFrame(geometry=[simplified_poly], crs="EPSG:2180").to_crs("EPSG:4326")
        cutter.to_file(output_path, driver="GPKG")
        print("GOTOWE")

if __name__ == "__main__":
    generate_cutters()
