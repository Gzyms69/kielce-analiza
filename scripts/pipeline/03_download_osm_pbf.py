import requests
import sys
from pathlib import Path

URL = "https://download.geofabrik.de/europe/poland-latest.osm.pbf"
DEST = Path("data/poland/osm/poland-latest.osm.pbf")

def download():
    DEST.parent.mkdir(parents=True, exist_ok=True)
    if DEST.exists():
        print(f"Plik {DEST} już istnieje. Pomijam pobieranie.")
        return

    print(f"Rozpoczynam pobieranie: {URL}")
    r = requests.get(URL, stream=True)
    r.raise_for_status()
    
    total_size = int(r.headers.get('content-length', 0))
    downloaded = 0
    
    with open(DEST, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024*1024):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                done = int(50 * downloaded / total_size)
                sys.stdout.write(f"\r[{'=' * done}{' ' * (50-done)}] {downloaded/(1024*1024):.1f} MB / {total_size/(1024*1024):.1f} MB")
                sys.stdout.flush()
    print("\nPobieranie zakończone.")

if __name__ == "__main__":
    download()
