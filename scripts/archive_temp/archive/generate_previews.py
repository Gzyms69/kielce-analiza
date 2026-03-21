import geopandas as gpd
import pandas as pd
import json
from pathlib import Path
import os

CITIES_ROOT = Path("data/cities")

def generate_previews():
    print("Generowanie próbek danych (Previews) dla wszystkich miast...")
    
    for city_dir in sorted(CITIES_ROOT.iterdir()):
        if not city_dir.is_dir(): continue
        
        city = city_dir.name
        preview = {"city": city, "layers": {}}
        
        # 1. Preview OSM
        osm_path = city_dir / "osm_full.gpkg"
        if osm_path.exists():
            try:
                # Sprawdzamy warstwy w GPKG
                import pyogrio
                layers = pyogrio.list_layers(osm_path)
                preview["layers"]["osm"] = {"file_size_mb": round(osm_path.stat().st_size / (1024*1024), 2)}
                
                for layer_name in layers[:, 0]:
                    # Pobieramy 3 rekordy z każdej warstwy OSM
                    gdf = gpd.read_file(osm_path, layer=layer_name, rows=3)
                    preview["layers"]["osm"][layer_name] = {
                        "count": len(gdf),
                        "columns": list(gdf.columns),
                        "sample": gdf.drop(columns='geometry').to_dict(orient='records')
                    }
            except Exception as e:
                preview["layers"]["osm"] = {"error": str(e)}

        # 2. Preview RCN (GML)
        rcn_dir = city_dir / "rcn"
        rcn_files = list(rcn_dir.glob("*.gml"))
        if rcn_files:
            try:
                gdf_rcn = gpd.read_file(rcn_files[0], rows=3)
                preview["layers"]["rcn"] = {
                    "columns": list(gdf_rcn.columns),
                    "sample": gdf_rcn.drop(columns='geometry').to_dict(orient='records')
                }
            except Exception as e:
                preview["layers"]["rcn"] = {"error": str(e)}

        # Zapis podglądu do pliku JSON w folderze miasta
        output_preview = city_dir / "data_preview.json"
        with open(output_preview, "w", encoding="utf-8") as f:
            json.dump(preview, f, indent=2, ensure_ascii=False)
        print(f"  [OK] Preview dla {city}")

if __name__ == "__main__":
    generate_previews()
