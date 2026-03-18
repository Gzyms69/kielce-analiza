import geopandas as gpd
import pandas as pd
from pathlib import Path
from shapely.ops import nearest_points
import os

CITIES_ROOT = Path("data/cities")
POP_PATH = Path("data/poland/population/nsp2021_grid250m.gpkg")
SAMPLE_REPORT = Path("reports/city_data_samples.txt")

def get_samples(city_name, pop_grid):
    city_dir = CITIES_ROOT / city_name
    stops_path = city_dir / "smart_stops.gpkg"
    rcn_path = city_dir / "rcn" / "transactions.gpkg"
    osm_path = city_dir / "osm_full.gpkg"
    
    if not stops_path.exists(): return f"CITY: {city_name} - MISSING STOPS\n"
    
    output = [f"CITY: {city_name.upper()}", "="*50]
    
    try:
        stops = gpd.read_file(stops_path).to_crs("EPSG:2180").head(5)
        rcn = gpd.read_file(rcn_path).to_crs("EPSG:2180") if rcn_path.exists() else None
        osm = gpd.read_file(osm_path, layer="points").to_crs("EPSG:2180") if osm_path.exists() else None
        
        for idx, stop in stops.iterrows():
            output.append(f"\n[SAMPLE {idx+1}] STOP: {stop.get('stop_name', 'Unknown')} ({stop.get('stop_id', 'N/A')})")
            output.append(f"  Coords (2180): {stop.geometry.x:.2f}, {stop.geometry.y:.2f}")
            
            # Population
            pop_val = "N/A"
            if pop_grid is not None:
                point_in_pop = pop_grid[pop_grid.intersects(stop.geometry.buffer(250))]
                if not point_in_pop.empty:
                    pop_val = point_in_pop.iloc[0].get('tot', '0')
            output.append(f"  Population (250m cell): {pop_val}")
            
            # Nearest RCN
            if rcn is not None:
                output.append("  Nearest Transactions (RCN):")
                rcn['dist'] = rcn.distance(stop.geometry)
                near_rcn = rcn.sort_values('dist').head(3)
                for _, r in near_rcn.iterrows():
                    output.append(f"    - {r['dist']:.0f}m away: {r.get('price_m2', 0):.0f} PLN/m2 (Total: {r.get('tran_cena_brutto', 0):.0f} PLN, Area: {r.get('lok_pow_uzyt', 0)} m2)")
            
            # Nearest POI
            if osm is not None:
                output.append("  Nearest Infrastructure (OSM):")
                osm['dist'] = osm.distance(stop.geometry)
                near_osm = osm.sort_values('dist').head(3)
                for _, o in near_osm.iterrows():
                    tags = o.get('other_tags', '')
                    output.append(f"    - {o['dist']:.0f}m away: POI ID {o.get('osm_id', 'N/A')} (Tags: {tags[:100]}...)")
            
            output.append("-" * 20)
            
    except Exception as e:
        output.append(f"  ERROR DURING SAMPLING: {e}")
        
    return "\n".join(output) + "\n\n"

def run_sampling():
    print("=== STARTING DATA SAMPLING ATLAS ===")
    cities = sorted([d.name for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    print("  Loading National Population Grid (slow)...")
    try:
        pop_grid = gpd.read_file(POP_PATH).to_crs("EPSG:2180")
    except:
        pop_grid = None
        print("  WARNING: Population grid not found or unreadable.")

    with open(SAMPLE_REPORT, "w") as f:
        f.write("NATIONAL DATA ATLAS: 5-STOP SAMPLE PER CITY\n")
        f.write("All metrics in EPSG:2180 (Poland 1992 Standard)\n")
        f.write("-" * 60 + "\n\n")
        
        for city in cities:
            print(f"  Sampling {city}...")
            f.write(get_samples(city, pop_grid))
            
    print(f"Sampling complete: {SAMPLE_REPORT}")

if __name__ == "__main__":
    run_sampling()
