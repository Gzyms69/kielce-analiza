import requests
import json
from pathlib import Path
import time
import os

CITIES_ROOT = Path("data/cities")
WFS_URL = "https://mapy.geoportal.gov.pl/wss/service/rcn"
DATE_START = "2025-01-01"

def fetch_rcn_v2():
    print("=== START RCN HARVESTER 2.0 (Verified Targets) ===\n")
    
    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    for city_dir in cities:
        city = city_dir.name
        targets_file = city_dir / "rcn_targets.json"
        rcn_dir = city_dir / "rcn"
        rcn_dir.mkdir(parents=True, exist_ok=True)
        
        if not targets_file.exists():
            print(f"[SKIP] {city}: Brak rcn_targets.json")
            continue
            
        with open(targets_file, "r") as f:
            teryt_list = json.load(f)
            
        print(f"\n--- Aglomeracja: {city.upper()} ({len(teryt_list)} powiaty) ---")
        
        for teryt in teryt_list:
            output_file = rcn_dir / f"rcn_{teryt}.gml"
            
            # Checkpoint: skip if exists and not empty
            if output_file.exists() and output_file.stat().st_size > 1000:
                print(f"  [SKIP] {teryt} (już pobrano)")
                continue
                
            print(f"  [GET] {teryt}...")
            all_content = []
            start_index = 0
            page_size = 3000 # Optymalny rozmiar strony dla GUGiK
            
            while True:
                # Filtr OGC XML - precyzyjny dla powiatu i daty
                filter_xml = f"""<ogc:Filter xmlns:ogc='http://www.opengis.net/ogc'>
                    <ogc:And>
                        <ogc:PropertyIsLike wildCard='*' singleChar='.' escapeChar='!'>
                            <ogc:PropertyName>teryt</ogc:PropertyName>
                            <ogc:Literal>{teryt}*</ogc:Literal>
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
                    "count": page_size,
                    "startIndex": start_index
                }
                
                try:
                    r = requests.get(WFS_URL, params=params, timeout=60)
                    r.raise_for_status()
                    
                    # Liczymy rekordy w odpowiedzi
                    count = r.text.count("<ms:lokale")
                    
                    if count == 0:
                        break
                        
                    all_content.append(r.text)
                    if count < page_size:
                        break # Ostatnia strona
                        
                    start_index += page_size
                    time.sleep(1.0) # Bezpieczeństwo serwera
                    
                except Exception as e:
                    print(f"    [ERR] Błąd połączenia dla {teryt}: {e}")
                    # Jeśli serwer nas zablokował, czekamy dłużej
                    if "429" in str(e) or "503" in str(e):
                        print("    [!!!] Serwer GUGiK zgłasza przeciążenie. Pauza 30s...")
                        time.sleep(30)
                    break
            
            if all_content:
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write("\n".join(all_content))
                print(f"    [OK] Zapisano {teryt}")
            else:
                print(f"    [EMPTY] Brak danych WFS dla {teryt}")
            
            # Przerwa między powiatami
            time.sleep(1.5)

if __name__ == "__main__":
    fetch_rcn_v2()
