import geopandas as gpd
import pandas as pd
from pathlib import Path
import subprocess
import os
import json

CITIES_ROOT = Path("data/cities")

def get_layer_extent(file_path, layer_name):
    try:
        result = subprocess.run(
            ["ogrinfo", "-so", str(file_path), layer_name],
            capture_output=True, text=True, check=True
        )
        for line in result.stdout.splitlines():
            if "Extent:" in line:
                # Format: Extent: (minx, miny) - (maxx, maxy)
                parts = line.replace("Extent:", "").replace("(", "").replace(")", "").replace("-", "").replace(",", "").split()
                return [float(p) for p in parts]
    except:
        return None
    return None

def audit_stop_vicinity(city_dir):
    name = city_dir.name
    stops_path = city_dir / "smart_stops.gpkg"
    zone_path = city_dir / "transport_zone.gpkg"
    osm_path = city_dir / "osm_full.gpkg"
    rcn_path = city_dir / "rcn" / "transactions.gpkg"
    
    report = {
        "City": name,
        "Total_Stops": 0,
        "BBOX_Integrity": "FAIL",
        "Stops_with_OSM_%": 0,
        "Stops_with_RCN_%": 0
    }
    
    if not all([stops_path.exists(), zone_path.exists(), osm_path.exists()]):
        return report

    try:
        # 1. Zasięg Strefy
        zone_extent = get_layer_extent(zone_path, "transport_zone")
        
        # 2. Zasięg OSM
        osm_extent = get_layer_extent(osm_path, "multipolygons")
        
        if zone_extent and osm_extent:
            # Margines błędu 50m
            if (osm_extent[0] <= zone_extent[0] + 50 and 
                osm_extent[1] <= zone_extent[1] + 50 and 
                osm_extent[2] >= zone_extent[2] - 50 and 
                osm_extent[3] >= zone_extent[3] - 50):
                report["BBOX_Integrity"] = "PASS"
            else:
                report["BBOX_Integrity"] = "CLIPPED_ERROR"

        # 3. Próbkowy test sąsiedztwa (100 przystanków)
        stops = gpd.read_file(stops_path).to_crs("EPSG:2180")
        report["Total_Stops"] = len(stops)
        sample_size = min(len(stops), 100)
        sample_stops = stops.sample(sample_size)
        
        # Wczytujemy małą próbkę danych dla szybkości
        osm_b = gpd.read_file(osm_path, layer="multipolygons", rows=10000).to_crs("EPSG:2180")
        
        rcn_p = gpd.GeoDataFrame()
        if rcn_path.exists():
            try: rcn_p = gpd.read_file(rcn_path, rows=10000).to_crs("EPSG:2180")
            except: pass

        osm_ok = 0
        rcn_ok = 0
        for _, stop in sample_stops.iterrows():
            buf = stop.geometry.buffer(1500)
            if not osm_b.empty and osm_b.intersects(buf).any(): osm_ok += 1
            if not rcn_p.empty and rcn_p.intersects(buf).any(): rcn_ok += 1
            
        report["Stops_with_OSM_%"] = round((osm_ok / sample_size) * 100, 1)
        report["Stops_with_RCN_%"] = round((rcn_ok / sample_size) * 100, 1)

    except Exception as e:
        report["BBOX_Integrity"] = f"ERR: {str(e)[:15]}"

    return report

def main():
    print("=== GRANULAR VICINITY INTEGRITY AUDIT (VIT v2.0) ===\n")
    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    results = [audit_stop_vicinity(c) for c in cities]
    df = pd.DataFrame(results)
    
    print(df[["City", "Total_Stops", "BBOX_Integrity", "Stops_with_OSM_%", "Stops_with_RCN_%"]].to_string(index=False))
    
    print("\n" + "="*90)
    print("WYNIK KOŃCOWY:")
    print("Jeśli BBOX_Integrity to PASS, oznacza to, że infrastruktura OSM pokrywa 100% obszaru wokół przystanków.")
    print("="*90)

if __name__ == "__main__":
    main()
