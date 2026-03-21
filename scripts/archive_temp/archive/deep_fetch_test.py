import requests
import time
from pathlib import Path

# --- CONFIG ---
TEST_CITIES = {
    "Warszawa": "1465",
    "Kraków": "1261",
    "Wrocław": "0264"
}
WFS_URL = "https://mapy.geoportal.gov.pl/wss/service/rcn"
PAGE_SIZE = 5000

def deep_fetch(city_name, teryt_code):
    print(f"\n=== GŁĘBOKIE POBIERANIE: {city_name} ({teryt_code}) ===")
    total_records = 0
    total_size_mb = 0
    start_index = 0
    page_num = 1
    
    city_start_time = time.time()
    
    while True:
        params = {
            "service": "WFS",
            "version": "2.0.0",
            "request": "GetFeature",
            "typenames": "ms:lokale",
            "srsname": "EPSG:2180",
            "CQL_FILTER": f"teryt = '{teryt_code}'",
            "count": PAGE_SIZE,
            "startIndex": start_index
        }
        
        try:
            r = requests.get(WFS_URL, params=params, timeout=60)
            r.raise_for_status()
            
            # Liczymy obiekty w tej paczce
            count = r.text.count("<ms:lokale")
            if count == 0:
                print(f"  Brak więcej danych (osiągnięto koniec zbioru).")
                break
                
            size_mb = len(r.content) / (1024 * 1024)
            total_records += count
            total_size_mb += size_mb
            
            print(f"  Paczka {page_num}: {count} rekordów, {size_mb:.2f} MB")
            
            if count < PAGE_SIZE:
                print(f"  Ostatnia paczka (mniejsza niż limit).")
                break
                
            start_index += PAGE_SIZE
            page_num += 1
            time.sleep(1) # Oddech dla serwera
            
        except Exception as e:
            print(f"  [BŁĄD] {e}")
            break
            
    elapsed = time.time() - city_start_time
    print(f"PODSUMOWANIE {city_name}: {total_records} rec, {total_size_mb:.2f} MB, {elapsed:.2f}s")
    return {"name": city_name, "records": total_records, "size": total_size_mb, "time": elapsed}

def main():
    results = []
    for name, code in TEST_CITIES.items():
        results.append(deep_fetch(name, code))
        
    print("\n--- NOWA ESTYMACJA DLA POLSKI ---")
    total_test_records = sum(r['records'] for r in results)
    total_test_size = sum(r['size'] for r in results)
    
    # Skalujemy wyniki z 3 metropolii na 355 powiatów
    # Zakładamy, że reszta powiatów ma średnio 1/5 tego co metropolie
    avg_per_metro = total_test_size / 3
    est_full_size_gb = (avg_per_metro * 355 * 0.3) / 1024 # 30% wagi metropolii dla reszty
    
    print(f"Łącznie w 3 miastach: {total_test_records} transakcji.")
    print(f"Łączny rozmiar dla 3 miast: {total_test_size:.2f} MB")
    print(f"Nowa estymacja rozmiaru całej Polski: ~{est_full_size_gb:.2f} GB")

if __name__ == "__main__":
    main()
