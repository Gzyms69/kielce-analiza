import requests
import pandas as pd
import time
from pathlib import Path
import concurrent.futures
import os

# --- CONFIG ---
TERYT_LIST_CSV = "reports/counties_to_fetch.csv"
BENCHMARK_COUNT = 10
WFS_URL = "https://mapy.geoportal.gov.pl/wss/service/rcn"
MAX_THREADS = 5 # Bezpieczny limit dla benchmarku

def benchmark_county(teryt_code, county_name):
    params = {
        "service": "WFS",
        "version": "2.0.0",
        "request": "GetFeature",
        "typenames": "ms:lokale",
        "srsname": "EPSG:2180",
        "CQL_FILTER": f"teryt = '{teryt_code}'",
        "count": 5000 # Prosimy o dużą paczkę, by poczuć obciążenie
    }

    try:
        start_time = time.time()
        r = requests.get(WFS_URL, params=params, timeout=60)
        elapsed = time.time() - start_time
        
        size_mb = len(r.content) / (1024 * 1024)
        
        # Wyciągamy liczbę obiektów prostym grepem, by nie parsować całego XML
        count = r.text.count("<ms:lokale")
        
        return {
            "county": county_name,
            "teryt": teryt_code,
            "time": elapsed,
            "size_mb": size_mb,
            "records": count,
            "speed_rec_sec": count / elapsed if elapsed > 0 else 0
        }
    except Exception as e:
        return {"county": county_name, "error": str(e)}

def main():
    df = pd.read_csv(TERYT_LIST_CSV).head(BENCHMARK_COUNT)
    # TERYT w WFS Geoportalu to 4 cyfry dla powiatu
    df['teryt_code'] = df['teryt_code'].astype(str).str.zfill(4)

    print(f"=== BENCHMARK WFS RCN (Próba {BENCHMARK_COUNT} powiatów) ===")
    
    results = []
    total_start = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = {executor.submit(benchmark_county, row['teryt_code'], row['county_name']): row for _, row in df.iterrows()}
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if "error" in res:
                print(f"[ERR] {res['county']}: {res['error']}")
            else:
                print(f"[OK] {res['county']} ({res['teryt']}): {res['records']} rec, {res['size_mb']:.2f} MB in {res['time']:.2f}s")
                results.append(res)

    total_elapsed = time.time() - total_start
    
    if results:
        res_df = pd.DataFrame(results)
        avg_time = res_df['time'].mean()
        avg_size = res_df['size_mb'].mean()
        
        total_counties = 355
        est_total_hours = (avg_time * total_counties / MAX_THREADS) / 3600
        est_total_gb = (avg_size * total_counties) / 1024

        print("\n--- PODSUMOWANIE ESTYMACJI ---")
        print(f"Średni czas na powiat: {avg_time:.2f}s")
        print(f"Średni rozmiar na powiat: {avg_size:.2f} MB")
        print(f"Estymowany czas dla 355 powiatów ({MAX_THREADS} wątków): {est_total_hours:.2f} h")
        print(f"Estymowany całkowity rozmiar danych: {est_total_gb:.2f} GB")
        
        # Aktualizacja DevLog
        with open("devlog.md", "a") as f:
            f.write(f"\n### 17. Benchmark pobierania RCN\n- **Działanie:** Stress test na 10 powiatach. Estymacja: {est_total_hours:.2f}h pracy, {est_total_gb:.2f}GB danych.\n- **Uzasadnienie:** Potwierdzenie parametrów WFS i planowanie zasobów dyskowych.\n")

if __name__ == "__main__":
    main()
