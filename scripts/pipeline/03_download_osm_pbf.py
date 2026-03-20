import requests
import sys
import os
from pathlib import Path

URL = "https://download.geofabrik.de/europe/poland-latest.osm.pbf"

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def download():
    dest = get_data_dir() / "poland" / "osm" / "poland-latest.osm.pbf"
    dest.parent.mkdir(parents=True, exist_ok=True)
    
    if dest.exists() and dest.stat().st_size > 1_000_000_000:
        print(f"Plik {dest} już istnieje i ma poprawny rozmiar. Pomijam pobieranie.")
        return

    print(f"Rozpoczynam pobieranie: {URL}")
    r = requests.get(URL, stream=True)
    r.raise_for_status()
    
    total_size = int(r.headers.get('content-length', 0))
    downloaded = 0
    
    with open(dest, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024*1024):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                if total_size > 0:
                    done = int(50 * downloaded / total_size)
                    sys.stdout.write(f"\r[{'=' * done}{' ' * (50-done)}] {downloaded/(1024*1024):.1f} MB / {total_size/(1024*1024):.1f} MB")
                    sys.stdout.flush()
    print(f"\nPobieranie zakończone: {dest}")

if __name__ == "__main__":
    download()
