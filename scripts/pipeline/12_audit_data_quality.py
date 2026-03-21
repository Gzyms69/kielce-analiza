import geopandas as gpd
import pandas as pd
from pathlib import Path
import os
import argparse
import json
import sys

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

EXPECTED_SCHEMAS = {
    "stops": ["stop_id", "stop_name", "geometry"],
    "transactions": ["price_m2", "geometry"],
    "infrastructure": ["geometry"]
}

def check_file(path, expected_cols, label):
    """Zwraca (status, lista_problemow)"""
    issues = []
    
    if not path.exists():
        return "MISSING", [f"{label}: plik nie istnieje"]
    
    try:
        gdf = gpd.read_file(path, rows=100)
    except Exception as e:
        return "CORRUPT", [f"{label}: nie mozna otworzyc - {e}"]
    
    # 1. Sprawdz CRS
    if gdf.crs is None:
        issues.append(f"{label}: brak CRS")
    elif gdf.crs.to_epsg() not in [2180, 4326]:
        issues.append(f"{label}: nietypowy CRS {gdf.crs}")
    
    # 2. Sprawdz kompletnosc kolumn
    for col in expected_cols:
        if col != "geometry" and col not in gdf.columns:
            issues.append(f"{label}: brak kolumny '{col}'")
    
    # 3. Sprawdz puste geometrie
    if 'geometry' in gdf.columns:
        n_empty = gdf.geometry.is_empty.sum()
        n_null = gdf.geometry.isna().sum()
        if n_empty > 0:
            issues.append(f"{label}: {n_empty} pustych geometrii")
        if n_null > 0:
            issues.append(f"{label}: {n_null} nulli w geometry")
    
    # 4. Sprawdz liczbe wierszy
    # Wczytaj pelne dane dla row count
    try:
        full_count = len(gpd.read_file(path, rows=None))
    except Exception:
        full_count = len(gdf)
    
    if full_count == 0:
        issues.append(f"{label}: 0 wierszy!")
    elif label == "STOPS" and full_count < 10:
        issues.append(f"{label}: tylko {full_count} przystankow (podejrzane)")
    elif label == "RCN" and full_count < 5:
        issues.append(f"{label}: tylko {full_count} transakcji (podejrzane)")
    
    # 5. Sprawdz zakresy wartosci (RCN)
    if label == "RCN" and "price_m2" in gdf.columns:
        prices = pd.to_numeric(gdf["price_m2"], errors="coerce")
        n_invalid = prices.isna().sum()
        if n_invalid > 0:
            issues.append(f"{label}: {n_invalid}/{len(gdf)} nieparsowalne price_m2")
        
        valid = prices.dropna()
        if len(valid) > 0:
            if valid.min() <= 0:
                issues.append(f"{label}: price_m2 <= 0 (min={valid.min():.0f})")
            if valid.max() > 500000:
                issues.append(f"{label}: price_m2 > 500k (max={valid.max():.0f})")
    
    status = "PASSED" if not issues else "WARN"
    return status, issues

def audit_city(city_name, data_dir):
    city_dir = data_dir / "cities" / city_name
    spatial_dir = city_dir / "02_spatial"
    
    all_issues = []
    checks = {}
    
    # Stops
    s_stat, s_issues = check_file(spatial_dir / "stops.gpkg", EXPECTED_SCHEMAS["stops"], "STOPS")
    checks["stops"] = s_stat
    all_issues.extend(s_issues)
    
    # Transactions
    r_stat, r_issues = check_file(spatial_dir / "transactions.gpkg", EXPECTED_SCHEMAS["transactions"], "RCN")
    checks["rcn"] = r_stat
    all_issues.extend(r_issues)
    
    # Infrastructure
    o_stat, o_issues = check_file(spatial_dir / "infrastructure.gpkg", EXPECTED_SCHEMAS["infrastructure"], "OSM")
    checks["osm"] = o_stat
    all_issues.extend(o_issues)
    
    # CRS Parity check
    crs_set = set()
    for fname in ["stops.gpkg", "transactions.gpkg"]:
        fpath = spatial_dir / fname
        if fpath.exists():
            try:
                crs = gpd.read_file(fpath, rows=1).crs
                if crs:
                    crs_set.add(crs.to_epsg())
            except Exception:
                pass
    if len(crs_set) > 1:
        all_issues.append(f"CRS PARITY: rozne CRS miedzy plikami: {crs_set}")
    
    # Raport
    status = "FAILED" if any(s in ["MISSING", "CORRUPT"] for s in checks.values()) else (
        "WARN" if all_issues else "PASSED"
    )
    
    for issue in all_issues:
        print(f"  [!] {city_name}: {issue}")
    
    if not all_issues:
        print(f"  [OK] {city_name}: wszystkie walidacje przeszly")
    
    metrics = {
        "city": city_name,
        "status": status,
        "issues": len(all_issues),
        "checks": checks
    }
    print(f"__PIPELINE_METRICS__={json.dumps(metrics)}")
    return not all_issues

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", help="Miasto do audytu", required=True)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    data_dir = get_data_dir()
    audit_city(args.city, data_dir)

if __name__ == "__main__":
    main()
