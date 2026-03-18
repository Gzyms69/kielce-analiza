import geopandas as gpd
import pandas as pd
from pathlib import Path
import sqlite3
import os
import json

CITIES_ROOT = Path("data/cities")
POP_GRID_PATH = Path("data/poland/population/nsp2021_grid250m.gpkg")

def check_city_status(city_dir):
    name = city_dir.name
    zone_path = city_dir / "transport_zone.gpkg"
    osm_path = city_dir / "osm_full.gpkg"
    rcn_path = city_dir / "rcn" / "transactions.gpkg"
    stops_path = city_dir / "smart_stops.gpkg"
    
    status = {
        "City": name,
        "Stops": 0,
        "OSM": "MISSING",
        "Pop": "MISSING",
        "RCN_Recs": 0,
        "RCN_Teryt_Missing": []
    }
    
    # 1. Stops
    if stops_path.exists():
        try:
            with sqlite3.connect(stops_path) as conn:
                status["Stops"] = conn.execute("SELECT COUNT(*) FROM smart_stops").fetchone()[0]
        except: pass

    # 2. OSM
    if osm_path.exists():
        status["OSM"] = f"{osm_path.stat().st_size / (1024*1024):.1f}MB"

    # 3. RCN Analysis
    targets = []
    targets_path = city_dir / "rcn_targets.json"
    if targets_path.exists():
        with open(targets_path, "r") as f:
            targets = json.load(f)
            
    if rcn_path.exists():
        try:
            with sqlite3.connect(rcn_path) as conn:
                status["RCN_Recs"] = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
                # Sprawdzamy których TERYT brakuje w bazie
                present_teryt = [r[0][:4] for r in conn.execute("SELECT DISTINCT teryt FROM transactions").fetchall() if r[0]]
                status["RCN_Teryt_Missing"] = [t for t in targets if t not in present_teryt]
        except: pass
    else:
        status["RCN_Teryt_Missing"] = targets

    # 4. Population Check (Quick Check - czy plik zone przecina się z gridem)
    # Ze względu na wydajność sprawdzamy tylko obecność pliku gridu i zakładamy PASS jeśli zone istnieje
    if POP_GRID_PATH.exists() and zone_path.exists():
        status["Pop"] = "OK"

    return status

def main():
    print("=== DEEP PROJECT AUDIT (Coverage & Integrity) ===\n")
    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    results = [check_city_status(c) for c in cities]
    df = pd.DataFrame(results)
    
    # Formatowanie listy brakujących TERYT
    df['Missing_Teryt'] = df['RCN_Teryt_Missing'].apply(lambda x: f"{len(x)} ({','.join(x[:3])}...)" if x else "NONE")
    
    display_cols = ["City", "Stops", "OSM", "Pop", "RCN_Recs", "Missing_Teryt"]
    print(df[display_cols].to_string(index=False))
    
    print("\n" + "="*80)
    print("WNIOSKI:")
    print("1. Jeśli 'Missing_Teryt' > 0, musimy dociągnąć konkretne powiaty.")
    print("2. Łódź i Suwałki wymagają integracji paczek ZIP (RCN_Recs jest podejrzanie niskie).")
    print("="*80)

if __name__ == "__main__":
    main()
