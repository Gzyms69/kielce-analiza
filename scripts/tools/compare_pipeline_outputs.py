import geopandas as gpd
import pandas as pd
import json
from pathlib import Path
import os

def get_stats(base_path, city):
    spatial_dir = Path(base_path) / "cities" / city / "02_spatial"
    config_dir = Path(base_path) / "cities" / city / "03_config"
    
    stats = {
        "stops": 0,
        "poi": 0,
        "buildings": 0,
        "transactions": 0,
        "avg_price": 0,
        "population": 0
    }
    
    # 1. Stops
    p = spatial_dir / "stops.gpkg"
    if p.exists(): stats["stops"] = len(gpd.read_file(p))
    
    # 2. Infra
    p = spatial_dir / "infrastructure.gpkg"
    if p.exists():
        try:
            stats["poi"] = len(gpd.read_file(p, layer="points"))
            stats["buildings"] = len(gpd.read_file(p, layer="multipolygons"))
        except: pass
        
    # 3. RCN
    p = spatial_dir / "transactions.gpkg"
    if p.exists():
        try:
            gdf = gpd.read_file(p)
            stats["transactions"] = len(gdf)
            if 'price_m2' in gdf.columns:
                # Wymuszamy numeric by nie dostać 0 przez błędny typ str
                prices = pd.to_numeric(gdf['price_m2'], errors='coerce')
                stats["avg_price"] = prices.mean()
        except: pass
        
    # 4. Pop
    p = spatial_dir / "population_250m.gpkg"
    if p.exists():
        try:
            gdf = gpd.read_file(p)
            stats["population"] = gdf['TOT'].sum() if 'TOT' in gdf.columns else 0
        except: pass
        
    return stats

def run_comparison():
    cities = ["kielce", "warszawa"]
    results = []
    
    print("\n=== ARCHITECTURAL DELTA AUDIT (BASELINE vs TESTBED) ===\n")
    
    for city in cities:
        print(f"Analizuję: {city.upper()}...")
        old = get_stats("data", city)
        new = get_stats("test-pipeline", city)
        
        for key in old.keys():
            diff = new[key] - old[key]
            pct = (diff / old[key] * 100) if old[key] != 0 else 0
            results.append({
                "City": city,
                "Metric": key,
                "Baseline (Old)": round(old[key], 1),
                "Testbed (New)": round(new[key], 1),
                "Delta": round(diff, 1),
                "Delta %": f"{pct:+.1f}%"
            })

    df = pd.DataFrame(results)
    
    # Wyświetlanie sformatowane
    for city in cities:
        print(f"\n--- {city.upper()} ---")
        city_df = df[df['City'] == city][['Metric', 'Baseline (Old)', 'Testbed (New)', 'Delta', 'Delta %']]
        print(city_df.to_string(index=False))

    print("\n" + "="*80)
    print("INTERPRETACJA INŻYNIERYJNA:")
    print("1. STOPS Delta < 0: Sukces Smart Cut (wycięto pociągi w lasach).")
    print("2. POI/BUILDINGS Delta: Jeśli bliska 0%, nowa metoda Osmium jest stabilna.")
    print("3. POPULATION Delta: Wskazuje na zmianę zasięgu terytorialnego (nowe BBOXy).")
    print("4. AVG_PRICE Delta: Powinna być 0% (ta sama metoda obliczeń).")
    print("="*80)

if __name__ == "__main__":
    run_comparison()
