import subprocess
import json
from pathlib import Path
import time
import os

CITIES_ROOT = Path("data/cities")
WFS_URL = "https://mapy.geoportal.gov.pl/wss/service/rcn"
DATE_START = "2025-01-01"

def fetch_rcn_ogr():
    print("=== START RCN HARVESTER 3.2 (Production Scale) ===\n")
    
    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    for city_dir in cities:
        city = city_dir.name
        targets_file = city_dir / "rcn_targets.json"
        rcn_dir = city_dir / "rcn"
        output_gpkg = rcn_dir / "transactions.gpkg"
        
        if not targets_file.exists(): continue
        
        # Jeśli baza już istnieje i ma sensowny rozmiar, omijamy (Checkpointing)
        if output_gpkg.exists() and output_gpkg.stat().st_size > 1_000_000 and city not in ["lodz", "suwalki"]:
            # print(f"[SKIP] {city}")
            continue

        with open(targets_file, "r") as f:
            teryt_list = json.load(f)
            
        print(f"\n--- Aglomeracja: {city.upper()} ({len(teryt_list)} powiaty) ---")
        
        for teryt in teryt_list:
            if len(teryt) != 4: continue
            
            print(f"  [WFS] Pobieranie {teryt}...", end=" ", flush=True)
            
            # Filtr OGC (teryt + data)
            where_clause = f"teryt LIKE '{teryt}%' AND dok_data >= '{DATE_START}'"
            
            try:
                subprocess.run([
                    "ogr2ogr",
                    "-f", "GPKG",
                    "-update", "-append",
                    str(output_gpkg),
                    f"WFS:{WFS_URL}",
                    "ms:lokale",
                    "-where", where_clause,
                    "-nln", "transactions",
                    "--config", "GDAL_HTTP_TIMEOUT", "60",
                    "--config", "OGR_WFS_PAGING_ALLOWED", "YES",
                    "--config", "OGR_WFS_PAGE_SIZE", "2000"
                ], check=True, capture_output=True)
                print("OK")
            except subprocess.CalledProcessError as e:
                err = e.stderr.decode()
                if "0 features" in err or "returned empty" in err:
                    print("EMPTY")
                else:
                    print(f"ERR: {err[:50]}...")
            
            time.sleep(1.2) # Bezpieczeństwo serwera GUGiK

if __name__ == "__main__":
    fetch_rcn_ogr()
