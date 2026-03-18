import requests
import pandas as pd
from pathlib import Path
import concurrent.futures
import os
import time
import re
from datetime import datetime

# --- CONFIG ---
TERYT_LIST_CSV = "reports/counties_to_fetch.csv"
OUTPUT_DIR = Path("data/raw/rcn")
LOG_FILE = Path("logs/fetch_rcn.log")
WFS_URL = "https://mapy.geoportal.gov.pl/wss/service/rcn"
DATE_START = "2025-01-01"
PAGE_SIZE = 5000
MAX_THREADS = 10

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(message)

def fetch_county(teryt_code, county_name):
    final_path = OUTPUT_DIR / f"{teryt_code}.gml"
    
    # Check if already exists
    if final_path.exists() and final_path.stat().st_size > 1000:
        return f"[SKIP] {county_name} ({teryt_code})"

    log(f"[START] Pobieranie: {county_name} ({teryt_code})...")
    
    all_content = []
    start_index = 0
    
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
            
            # Simple check for records
            count = r.text.count("<ms:lokale")
            if count == 0:
                break
            
            all_content.append(r.text)
            
            if count < PAGE_SIZE:
                break
                
            start_index += PAGE_SIZE
            time.sleep(0.5) # Oddech
            
        except Exception as e:
            log(f"[ERROR] {county_name} ({teryt_code}) na indeksie {start_index}: {e}")
            return f"[FAILED] {county_name}"

    if all_content:
        # Save aggregated pages
        with open(final_path, "w", encoding="utf-8") as f:
            f.write("\n".join(all_content))
        log(f"[SUCCESS] {county_name} ({teryt_code}) - pobrano {len(all_content)} paczek.")
        return f"[OK] {county_name}"
    else:
        log(f"[EMPTY] {county_name} ({teryt_code}) - brak danych w tym okresie.")
        return f"[EMPTY] {county_name}"

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(TERYT_LIST_CSV)
    df['teryt_code'] = df['teryt_code'].astype(str).str.zfill(4)
    
    log(f"Rozpoczynam masową ingestję dla {len(df)} powiatów.")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = {executor.submit(fetch_county, row['teryt_code'], row['county_name']): row for _, row in df.iterrows()}
        for future in concurrent.futures.as_completed(futures):
            future.result()

    # Final DevLog update
    with open("devlog.md", "a") as f:
        f.write(f"\n### 18. Pełna ingestja RCN (Polska)\n- **Działanie:** Uruchomienie `fetch_rcn_final.py` dla 355 powiatów z filtrem daty >= 2025.\n- **Uzasadnienie:** Budowa kompletnej bazy danych nieruchomości dla całego obszaru transportowego kraju.\n")

if __name__ == "__main__":
    main()
