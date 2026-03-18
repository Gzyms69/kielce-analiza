import subprocess
import concurrent.futures
from pathlib import Path
import time

# Mapa brakujących powiatów z audytu
MISSING_MAP = {
    "bialystok": ["2002"],
    "bydgoszcz": ["0461"],
    "elk": ["2806"],
    "gizycko": ["2806", "2819"],
    "gzm": ["2415"],
    "lodz": ["1021"],
    "olsztyn": ["2806"],
    "opole": ["1609"],
    "poznan": ["3014"],
    "szczecin": ["3204", "3211"],
    "trojmiasto": ["2210"],
    "warszawa": ["1434"],
    "wroclaw": ["0202", "1606"]
}

WFS_URL = "https://mapy.geoportal.gov.pl/wss/service/rcn"
DATE_START = "2025-01-01"

def download_missing_teryt(city, teryt):
    output_gpkg = Path(f"data/cities/{city}/rcn/transactions.gpkg")
    where_clause = f"teryt LIKE '{teryt}%' AND dok_data >= '{DATE_START}'"
    
    print(f"  [START] {city}: {teryt}...")
    try:
        subprocess.run([
            "ogr2ogr", "-f", "GPKG", "-update", "-append",
            str(output_gpkg), f"WFS:{WFS_URL}", "ms:lokale",
            "-where", where_clause, "-nln", "transactions",
            "--config", "GDAL_HTTP_TIMEOUT", "60",
            "--config", "OGR_WFS_PAGING_ALLOWED", "YES"
        ], check=True, capture_output=True)
        return f"[OK] {city}: {teryt}"
    except Exception as e:
        return f"[EMPTY/ERR] {city}: {teryt}"

def main():
    print("=== CHIRURGICZNE DOPOBIERANIE BRAKUJĄCYCH POWIATÓW ===\n")
    tasks = []
    for city, teryts in MISSING_MAP.items():
        for teryt in teryts:
            tasks.append((city, teryt))
            
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(download_missing_teryt, c, t) for c, t in tasks]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    main()
