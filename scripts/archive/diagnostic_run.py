import requests
import pandas as pd
import time
import os
from pathlib import Path

# --- CONFIG ---
TERYT_LIST_CSV = "reports/counties_to_fetch.csv"
DIAGNOSTIC_DIR = Path("data/raw/rcn_test")
WFS_URL = "https://mapy.geoportal.gov.pl/wss/service/rcn"

def diagnostic_fetch(teryt_code, county_name, use_proxy=False):
    print(f"\n--- TEST: {county_name} ({teryt_code}) | Proxy: {use_proxy} ---")
    
    # Próbujemy najpierw pobrać jeden obiekt, żeby sprawdzić nazwy kolumn i czy filtr działa
    params = {
        "service": "WFS",
        "request": "GetFeature",
        "version": "2.0.0",
        "typeNames": "ms:lokale",
        "outputFormat": "application/json",
        "CQL_FILTER": f"idLokalu LIKE '{teryt_code}%'",
        "maxFeatures": 5
    }

    proxies = None
    if use_proxy:
        if os.path.exists("scripts/proxies.txt"):
            with open("scripts/proxies.txt", "r") as f:
                p_list = [line.strip() for line in f if line.strip()]
                if p_list:
                    p_addr = p_list[0]
                    proxies = {"http": f"http://{p_addr}", "https": f"http://{p_addr}"}
                    print(f"  Używam proxy: {p_addr}")

    try:
        start = time.time()
        r = requests.get(WFS_URL, params=params, proxies=proxies, timeout=30)
        elapsed = time.time() - start
        
        print(f"  Status Code: {r.status_code}")
        
        if r.status_code == 200:
            try:
                data = r.json()
                features = data.get('features', [])
                print(f"  Sukces! Pobrano {len(features)} obiektów.")
                if features:
                    # Pokazujemy przykładowe ID, żeby sprawdzić strukturę TERYT
                    print(f"  Przykładowe ID: {features[0].get('properties', {}).get('idLokalu')}")
                return True
            except:
                print("  BŁĄD: Serwer zwrócił XML zamiast JSON (prawdopodobnie Exception Report)")
                print(f"  Treść: {r.text[:300]}")
                return False
        else:
            print(f"  BŁĄD HTTP: {r.status_code}")
            return False

    except Exception as e:
        print(f"  BŁĄD POŁĄCZENIA: {e}")
        return False

def main():
    DIAGNOSTIC_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(TERYT_LIST_CSV).head(3) # Test na 3 powiatach
    df['teryt_code'] = df['teryt_code'].astype(str).str.zfill(4)

    print("=== ROZPOCZYNAM POPRAWIONĄ DIAGNOSTYKĘ (Warstwa ms:lokale) ===")
    
    for _, row in df.iterrows():
        diagnostic_fetch(row['teryt_code'], row['county_name'], use_proxy=False)
        time.sleep(1)

if __name__ == "__main__":
    main()
