import requests
import pandas as pd
from pathlib import Path
import concurrent.futures
import os
import time
import random

# --- CONFIG ---
TERYT_LIST_CSV = "reports/counties_to_fetch.csv"
OUTPUT_DIR = Path("data/raw/rcn")
PROXIES_FILE = "scripts/proxies.txt"
WFS_URL = "https://mapy.geoportal.gov.pl/wss/service/rcn"
MAX_THREADS = 15  # Zwiększamy, bo mamy dużo proxy
TIMEOUT = 45

def get_proxies():
    if not os.path.exists(PROXIES_FILE):
        return []
    with open(PROXIES_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def fetch_county_rcn(teryt_code, county_name, proxy_pool):
    dest_path = OUTPUT_DIR / f"{teryt_code}.json"
    if dest_path.exists() and dest_path.stat().st_size > 100:
        return f"[SKIP] {county_name} ({teryt_code})"

    # Parametry WFS (KOMPLEKSOWE - brak propertyName = pobierz wszystko)
    params = {
        "service": "WFS",
        "request": "GetFeature",
        "version": "2.0.0",
        "typeNames": "ms:RCN_Lokal",
        "outputFormat": "application/json",
        "CQL_FILTER": f"idLokalu LIKE '{teryt_code}%'",
        "maxFeatures": 20000 # Zapas dla dużych powiatów
    }

    # Próby (Retry mechanism)
    for attempt in range(3):
        proxy = None
        if proxy_pool:
            p_addr = random.choice(proxy_pool)
            # Obsługujemy zarówno HTTP jak i SOCKS (uproszczenie)
            proxy = {"http": f"http://{p_addr}", "https": f"http://{p_addr}"}

        try:
            r = requests.get(WFS_URL, params=params, proxies=proxy, timeout=TIMEOUT)
            r.raise_for_status()
            
            # Walidacja czy to nie jest pusta odpowiedź
            if len(r.content) < 500:
                return f"[EMPTY] {county_name} ({teryt_code}) - brak transakcji w WFS"

            with open(dest_path, "wb") as f:
                f.write(r.content)
            
            return f"[SUCCESS] {county_name} ({teryt_code}) - {len(r.content)/1024:.1f} KB"
        
        except Exception as e:
            if attempt == 2:
                return f"[FAILED] {county_name} ({teryt_code}) po 3 próbach: {e}"
            time.sleep(1)

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(TERYT_LIST_CSV)
    df['teryt_code'] = df['teryt_code'].astype(str).str.zfill(4)
    
    proxies = get_proxies()
    print(f"Start: {len(df)} powiatów, {len(proxies)} proxy, {MAX_THREADS} wątków.")

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = {
            executor.submit(fetch_county_rcn, row['teryt_code'], row['county_name'], proxies): row 
            for _, row in df.iterrows()
        }
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    main()
