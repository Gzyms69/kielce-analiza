import json
import geopandas as gpd
from pathlib import Path

CITIES_ROOT = Path("data/cities")
CONFIG_OUTPUT = Path("extract_config.json")

def prepare_bbox_config():
    print("Inżynieryjne przygotowanie BBOX (Kwadraty tnące - Low RAM)...")
    extracts = []
    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    for city_dir in cities:
        city_name = city_dir.name
        zone_file = city_dir / "transport_zone.gpkg"
        output_pbf = f"data/cities/{city_name}/osm_bbox.pbf"
        
        if not zone_file.exists(): continue
            
        try:
            # Wczytujemy precyzyjną granicę tylko po to, by wyciągnąć 4 skrajne punkty (BBOX)
            gdf = gpd.read_file(zone_file)
            # bounds: [minx, miny, maxx, maxy] (EPSG:4326 to WGS84 - stopnie)
            minx, miny, maxx, maxy = gdf.total_bounds
            
            # Wpis do konfiguracji Osmium (żądamy tylko kwadratu)
            extracts.append({
                "output": output_pbf,
                "description": city_name,
                "bbox": [minx, miny, maxx, maxy]
            })
        except Exception as e:
            print(f"  [ERR] {city_name}: {e}")

    with open(CONFIG_OUTPUT, "w") as f:
        json.dump({"extracts": extracts}, f, indent=2)
    print(f"Konfiguracja BBOX gotowa: {len(extracts)} miast. Koszt RAM = ~0.")

if __name__ == "__main__":
    prepare_bbox_config()
