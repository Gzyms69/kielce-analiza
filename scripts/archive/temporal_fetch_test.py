import requests
import time
from datetime import datetime, timedelta

# --- CONFIG ---
TEST_TERYT = "1465" # Warszawa
WFS_URL = "https://mapy.geoportal.gov.pl/wss/service/rcn"
PAGE_SIZE = 5000

# Obliczamy datę rok wstecz
date_limit = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')

def temporal_test():
    print(f"=== TEST FILTRA CZASOWEGO: Warszawa ({TEST_TERYT}) | Po dacie: {date_limit} ===")
    
    params = {
        "service": "WFS",
        "version": "2.0.0",
        "request": "GetFeature",
        "typenames": "ms:lokale",
        "srsname": "EPSG:2180",
        # Łączymy filtry: TERYT + DATA
        "CQL_FILTER": f"teryt = '{TEST_TERYT}' AND dok_data >= '{date_limit}'",
        "count": PAGE_SIZE
    }
    
    try:
        start_time = time.time()
        r = requests.get(WFS_URL, params=params, timeout=60)
        r.raise_for_status()
        
        count = r.text.count("<ms:lokale")
        size_mb = len(r.content) / (1024 * 1024)
        elapsed = time.time() - start_time
        
        print(f"  Wynik: {count} rekordów z ostatniego roku.")
        print(f"  Rozmiar: {size_mb:.2f} MB")
        print(f"  Czas: {elapsed:.2f}s")
        
        # Jeśli count == PAGE_SIZE, oznacza to że nadal jest więcej niż 5000, ale to już skala do opanowania
        
    except Exception as e:
        print(f"  [BŁĄD] {e}")

if __name__ == "__main__":
    temporal_test()
