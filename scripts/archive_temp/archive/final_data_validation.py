import geopandas as gpd
from pathlib import Path
import pandas as pd
import os

CITIES_ROOT = Path("data/cities")

def validate_city_data(city_dir):
    city_name = city_dir.name
    results = {"city": city_name, "status": "PASS", "errors": []}
    
    # 1. Sprawdzenie istnienia kluczowych plików
    required_files = ["transport_zone.gpkg", "smart_stops.gpkg", "osm_full.gpkg"]
    for f in required_files:
        if not (city_dir / f).exists():
            results["status"] = "FAIL"
            results["errors"].append(f"Missing {f}")

    if results["status"] == "FAIL":
        return results

    try:
        # 2. Walidacja powierzchni wykrojnika (Zabezpieczenie przed pociągami)
        zone = gpd.read_file(city_dir / "transport_zone.gpkg")
        # Przeliczamy na układ metryczny (EPSG:2180), aby zmierzyć powierzchnię w km2
        area_km2 = zone.to_crs("EPSG:2180").geometry.area.sum() / 1_000_000
        results["area_km2"] = round(area_km2, 2)
        
        # Limit bezpieczeństwa: 6000 km2 (nawet aglomeracja warszawska jest mniejsza)
        if area_km2 > 6000:
            results["status"] = "FAIL"
            results["errors"].append(f"Area too large ({area_km2:.1f} km2) - possible train plague")

        # 3. Walidacja zawartości OSM
        osm = gpd.read_file(city_dir / "osm_full.gpkg", layer="multipolygons", rows=5)
        if "all_tags" not in osm.columns:
            results["status"] = "FAIL"
            results["errors"].append("OSM missing all_tags column")
            
        # 4. Sprawdzenie CRS
        if zone.crs.to_epsg() != 4326:
            results["status"] = "FAIL"
            results["errors"].append(f"Invalid CRS: {zone.crs.to_epsg()}")

    except Exception as e:
        results["status"] = "FAIL"
        results["errors"].append(str(e))

    return results

def main():
    print("=== OSTATECZNA WERYFIKACJA INTEGRALNOŚCI DANYCH ===\n")
    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    audit_data = []
    for city_dir in cities:
        res = validate_city_data(city_dir)
        audit_data.append(res)
        
        status_str = "[OK]" if res["status"] == "PASS" else "[ERROR]"
        area_str = f"{res.get('area_km2', 0):>8} km2"
        print(f"{status_str} {res['city'].ljust(15)} | Area: {area_str} | Errors: {', '.join(res['errors'])}")

    df = pd.DataFrame(audit_data)
    failed = df[df["status"] == "FAIL"]
    
    print("\n" + "="*50)
    if failed.empty:
        print("WYNIK: 100% DANYCH POPRAWNYCH I ZWERYFIKOWANYCH.")
    else:
        print(f"WYNIK: WYKRYTO BŁĘDY W {len(failed)} AGLOMERACJACH!")
    print("="*50)

if __name__ == "__main__":
    main()
