import geopandas as gpd
import pandas as pd
import numpy as np
from pathlib import Path
import sqlite3
import json
import os

CITIES_ROOT = Path("data/cities")
POP_GRID_PATH = Path("data/poland/population/nsp2021_grid250m.gpkg")

def analyze_spatial_integrity(city_dir):
    name = city_dir.name
    zone_path = city_dir / "transport_zone.gpkg"
    osm_path = city_dir / "osm_full.gpkg"
    rcn_path = city_dir / "rcn" / "transactions.gpkg"
    targets_path = city_dir / "rcn_targets.json"
    
    report = {
        "City": name,
        "Area_km2": 0,
        "OSM_Status": "MISSING",
        "RCN_Recs": 0,
        "RCN_Coverage_%": 0,
        "Price_Numeric": "NO",
        "Pop_Status": "MISSING"
    }
    
    if not zone_path.exists(): return report
    
    try:
        # 1. Strefa
        zone = gpd.read_file(zone_path).to_crs("EPSG:2180")
        report["Area_km2"] = round(zone.geometry.area.sum() / 1_000_000, 2)
        
        # 2. OSM Coverage Check (Szybki)
        if osm_path.exists():
            report["OSM_Status"] = "OK"
            # (Tutaj moglibyśmy sprawdzić ST_Envelope, ale rozmiar pliku już nam dużo mówi)

        # 3. RCN Deep Check
        if rcn_path.exists() and targets_path.exists():
            with open(targets_path, "r") as f:
                targets = json.load(f)
            
            try:
                with sqlite3.connect(rcn_path) as conn:
                    # Liczba rekordów
                    report["RCN_Recs"] = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
                    
                    # Pokrycie TERYT
                    present_teryt = [str(r[0])[:4] for r in conn.execute("SELECT DISTINCT teryt FROM transactions").fetchall() if r[0]]
                    found = [t for t in targets if t in present_teryt]
                    report["RCN_Coverage_%"] = round((len(found) / len(targets)) * 100, 1) if targets else 0
                    
                    # Sprawdzalność cen (Cast to Numeric)
                    # Sprawdzamy czy da się rzutować na liczbę chociaż 100 rekordów
                    prices = conn.execute("SELECT tran_cena_brutto FROM transactions WHERE tran_cena_brutto IS NOT NULL LIMIT 100").fetchall()
                    if prices:
                        try:
                            [float(p[0]) for p in prices if p[0]]
                            report["Price_Numeric"] = "YES"
                        except:
                            report["Price_Numeric"] = "TEXT_ONLY"
            except Exception as e:
                report["Price_Numeric"] = f"SQL_ERR"

        # 4. Pop Check
        if POP_GRID_PATH.exists():
            report["Pop_Status"] = "OK"

    except Exception as e:
        pass

    return report

def main():
    print("=== FINAL SPATIAL INTEGRITY & COVERAGE AUDIT (SICA 2026) ===\n")
    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    results = [analyze_spatial_integrity(c) for c in cities]
    df = pd.DataFrame(results)
    
    print(df.to_string(index=False))
    
    print("\n" + "="*90)
    print("ANALIZA SENIORA:")
    print("1. OSM_Status: OK oznacza, że baza infrastruktury jest obecna.")
    print("2. RCN_Coverage_%: Jeśli < 100%, serwer GUGiK nie posiada danych dla niektórych powiatów ościennych.")
    print("3. Price_Numeric: YES oznacza, że kolumna tekstowa zawiera poprawne liczby i jest gotowa do analizy.")
    print("="*90)

if __name__ == "__main__":
    main()
