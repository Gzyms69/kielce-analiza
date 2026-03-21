import requests
import re
from datetime import datetime, timedelta

# --- CONFIG ---
WARSAW_TERYT = "1465"
WFS_URL = "https://mapy.geoportal.gov.pl/wss/service/rcn"
date_limit = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')

def get_true_count():
    print(f"=== SPRAWDZANIE REALNEJ LICZBY TRANSAKCJI (Warszawa, od {date_limit}) ===")
    
    # Prosimy serwer tylko o liczbę trafień (resultType=hits)
    params = {
        "service": "WFS",
        "version": "2.0.0",
        "request": "GetFeature",
        "typenames": "ms:lokale",
        "resultType": "hits",
        "CQL_FILTER": f"teryt = '{WARSAW_TERYT}' AND dok_data >= '{date_limit}'"
    }
    
    try:
        r = requests.get(WFS_URL, params=params, timeout=30)
        r.raise_for_status()
        
        # Szukamy atrybutu numberMatched w odpowiedzi XML
        match = re.search(r'numberMatched="(\d+)"', r.text)
        if match:
            total = int(match.group(1))
            print(f"  Faktyczna liczba transakcji w Warszawie z ostatniego roku: {total}")
            print(f"  Wymaga to pobrania {total // 5000 + 1} paczek danych.")
        else:
            print("  BŁĄD: Serwer nie zwrócił atrybutu numberMatched.")
            print(f"  Odpowiedź: {r.text[:500]}")
            
    except Exception as e:
        print(f"  [BŁĄD] {e}")

if __name__ == "__main__":
    get_true_count()
