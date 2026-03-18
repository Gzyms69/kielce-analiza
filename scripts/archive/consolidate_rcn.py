import geopandas as gpd
import pandas as pd
from pathlib import Path
import os

CITIES_ROOT = Path("data/cities")

def consolidate_city_rcn(city_dir):
    city_name = city_dir.name
    rcn_dir = city_dir / "rcn"
    output_gpkg = city_dir / "rcn" / "transactions.gpkg"
    
    if not rcn_dir.exists():
        return None
        
    gml_files = list(rcn_dir.glob("*.gml"))
    if not gml_files:
        return None
        
    print(f"Konsolidacja {city_name.upper()} ({len(gml_files)} plików)...")
    
    all_data = []
    for gml in gml_files:
        try:
            # Czytamy GML za pomocą GDAL
            gdf = gpd.read_file(gml)
            if not gdf.empty:
                all_data.append(gdf)
        except Exception as e:
            # print(f"  [!] Błąd czytania {gml.name}: {e}")
            pass
            
    if not all_data:
        print(f"  [-] {city_name}: Brak danych do konsolidacji.")
        return 0
        
    # Łączymy wszystkie powiaty danej aglomeracji
    final_gdf = pd.concat(all_data, ignore_index=True)
    
    # Zapisujemy do GPKG
    final_gdf.to_file(output_gpkg, driver="GPKG")
    
    # Opcjonalnie usuwamy surowe GML, żeby zachować porządek (zostawiam na razie)
    # for gml in gml_files: gml.unlink()
    
    return len(final_gdf)

def main():
    print("=== KONSOLIDACJA I AUDYT ILOSCIOWY RCN ===\n")
    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    summary = []
    for city_dir in cities:
        count = consolidate_city_rcn(city_dir)
        if count is not None:
            summary.append({"city": city_dir.name, "count": count})
            print(f"  [OK] {city_dir.name.ljust(15)} | Rekordów: {count:,}".replace(',', ' '))

    print("\n" + "="*40)
    total = sum([s['count'] for s in summary])
    print(f"TOTAL RCN HARVESTED: {total:,}".replace(',', ' '))
    print("="*40)

if __name__ == "__main__":
    main()
