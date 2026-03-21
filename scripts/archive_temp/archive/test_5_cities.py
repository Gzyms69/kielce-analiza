import requests
import re
import os
import geopandas as gpd
from pathlib import Path
import time

# --- CONFIG ---
TEST_CITIES = {
    "1465": "Warszawa",
    "1261": "Kraków",
    "2661": "Kielce",
    "1463": "Radom",
    "2063": "Suwałki"
}
OUTPUT_DIR = Path("data/raw/rcn")
WFS_URL = "https://mapy.geoportal.gov.pl/wss/service/rcn"
DATE_START = "2025-01-01"
PAGE_SIZE = 5000

def download_and_merge(teryt_code, city_name):
    print(f"\n--- POBIERANIE: {city_name} ({teryt_code}) ---")
    dest_path = OUTPUT_DIR / f"{teryt_code}.gml"
    
    all_features = []
    start_index = 0
    
    # Nagłówek XML dla poprawnego GML 3.1.1
    header = """<?xml version="1.0" encoding="UTF-8" ?>
<wfs:FeatureCollection xmlns:ms="http://mapserver.gis.umn.edu/mapserver" xmlns:gml="http://www.opengis.net/gml" xmlns:wfs="http://www.opengis.net/wfs" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
"""
    footer = "</wfs:FeatureCollection>"

    while True:
        filter_xml = f"""<ogc:Filter xmlns:ogc='http://www.opengis.net/ogc'>
            <ogc:And>
                <ogc:PropertyIsLike wildCard='*' singleChar='.' escapeChar='!'>
                    <ogc:PropertyName>teryt</ogc:PropertyName>
                    <ogc:Literal>{teryt_code}*</ogc:Literal>
                </ogc:PropertyIsLike>
                <ogc:PropertyIsGreaterThanOrEqualTo>
                    <ogc:PropertyName>dok_data</ogc:PropertyName>
                    <ogc:Literal>{DATE_START}</ogc:Literal>
                </ogc:PropertyIsGreaterThanOrEqualTo>
            </ogc:And>
        </ogc:Filter>"""

        params = {
            "service": "WFS",
            "version": "1.1.0",
            "request": "GetFeature",
            "typename": "ms:lokale",
            "filter": filter_xml,
            "count": PAGE_SIZE,
            "startIndex": start_index
        }

        try:
            r = requests.get(WFS_URL, params=params, timeout=60)
            r.raise_for_status()
            
            # Ekstrakcja tylko elementów <gml:featureMember>... </gml:featureMember>
            # Używamy re.DOTALL aby łapać znaki nowej linii wewnątrz tagów
            features = re.findall(r'<gml:featureMember>.*?</gml:featureMember>', r.text, re.DOTALL)
            
            if not features:
                print(f"  Brak więcej danych.")
                break
            
            all_features.extend(features)
            print(f"  Paczka {start_index // PAGE_SIZE + 1}: pobrano {len(features)} obiektów.")
            
            if len(features) < PAGE_SIZE:
                break
                
            start_index += PAGE_SIZE
            time.sleep(1)
            
        except Exception as e:
            print(f"  [ERROR] {e}")
            break

    if all_features:
        # Składamy poprawny plik GML
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(header)
            f.write("\n".join(all_features))
            f.write(footer)
        
        size_mb = dest_path.stat().st_size / (1024*1024)
        print(f"[SUCCESS] Zapisano {len(all_features)} transakcji. Rozmiar: {size_mb:.2f} MB")
        
        # WERYFIKACJA ODCZYTU
        try:
            print(f"  Testowanie odczytu przez GeoPandas...")
            test_gdf = gpd.read_file(dest_path)
            print(f"  [OK] GeoPandas wczytał {len(test_gdf)} rekordów poprawnie.")
        except Exception as ge_err:
            print(f"  [CRITICAL ERROR] Plik jest uszkodzony dla GeoPandas: {ge_err}")
    else:
        print(f"[EMPTY] Brak danych dla {city_name}.")

if __name__ == "__main__":
    for code, name in TEST_CITIES.items():
        download_and_merge(code, name)
