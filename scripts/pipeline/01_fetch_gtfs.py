import os
import requests
import zipfile
import io
import time
import concurrent.futures
from pathlib import Path
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Zaladowanie zrodel GTFS z pliku konfiguracyjnego (zamiast hardcoded dict)
_CONFIG_PATH = Path(__file__).resolve().parent.parent.parent / "config" / "gtfs_sources.json"
with open(_CONFIG_PATH, "r", encoding="utf-8") as _f:
    GTFS_SOURCES = json.load(_f)


def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def get_allowed_cities():
    cities_env = os.environ.get("PIPELINE_CITIES")
    if cities_env:
        return [c.strip() for c in cities_env.split(',')]
    return None

def fetch_worker(url, city, data_dir):
    filename = url.split('/')[-1]
    
    # TWARDA ZASADA WYSPOWA: Kolej krajowa ma swój globalny folder!
    if city == "rail":
        target_dir = data_dir / "poland" / "gtfs_national" / filename.replace('.zip', '')
    else:
        target_dir = data_dir / "cities" / city / "gtfs" / filename.replace('.zip', '')
        
    target_dir.mkdir(parents=True, exist_ok=True)
    
    if (target_dir / "stops.txt").exists():
        return f"[POMINIĘTO] {city}/{filename} (już jest)", True

    max_retries = 3
    for attempt in range(max_retries):
        try:
            r = requests.get(url, stream=True, timeout=30, verify=False)
            r.raise_for_status()
            # Zapis streamu na dysk zamiast r.content (fix OOM dla duzych ZIP)
            tmp_zip = target_dir / "__download.zip"
            with open(tmp_zip, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            with zipfile.ZipFile(tmp_zip) as z:
                z.extractall(target_dir)
            tmp_zip.unlink()
            return f"[SUKCES] {city}/{filename}", True
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                return f"[BŁĄD] {city}/{filename}: {e}", False

def fetch_all():
    print("=== PRAWDZIWY RÓWNOLEGŁY GTFS DOWNLOADER (Self-Healing) ===")
    data_dir = get_data_dir()
    allowed_cities = get_allowed_cities()
    
    tasks = []
    for url, city in GTFS_SOURCES.items():
        # KRYTYCZNE: Kolej krajowa pobierana jest ZAWSZE, żeby nie było błędu z "zagubionymi stacjami PKP"
        if city != "rail" and allowed_cities and city not in allowed_cities:
            continue
        tasks.append((url, city))
        
    print(f"Ilość paczek do pobrania: {len(tasks)}")
    if not tasks:
        print("Brak zadań. Sprawdź filtry miast.")
        return

    success_count = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(fetch_worker, url, city, data_dir) for url, city in tasks]
        for future in concurrent.futures.as_completed(futures):
            msg, ok = future.result()
            if ok: success_count += 1
            print(msg)

    # Handshake Metrykowy dla Orkiestratora
    print(f"__PIPELINE_METRICS__={json.dumps({'step': '01', 'total_feeds': len(tasks), 'success': success_count})}")

if __name__ == "__main__":
    fetch_all()
