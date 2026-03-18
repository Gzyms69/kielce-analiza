import os
import requests
import zipfile
import io
import concurrent.futures
from pathlib import Path

GTFS_SOURCES = {
    "https://mkuran.pl/gtfs/warsaw.zip": "warszawa",
    "https://mkuran.pl/gtfs/wkd.zip": "warszawa", 
    "https://cdn.zbiorkom.live/gtfs/warsaw.zip": "warszawa",
    "https://cdn.zbiorkom.live/gtfs/warsaw-gpa.zip": "warszawa",
    "https://cdn.zbiorkom.live/gtfs/warsaw-lomianki.zip": "warszawa",
    "https://cdn.zbiorkom.live/gtfs/warsaw-minsk.zip": "warszawa",
    "https://cdn.zbiorkom.live/gtfs/warsaw-otwock.zip": "warszawa",
    "https://cdn.zbiorkom.live/gtfs/warsaw-pruszkow.zip": "warszawa",
    "https://cdn.zbiorkom.live/gtfs/warsaw-radzymin.zip": "warszawa",
    "https://cdn.zbiorkom.live/gtfs/warsaw-sochaczew.zip": "warszawa",
    "https://cdn.zbiorkom.live/gtfs/warsaw-sulejowek.zip": "warszawa",
    "https://cdn.zbiorkom.live/gtfs/warsaw-zabki.zip": "warszawa",
    "https://cdn.zbiorkom.live/gtfs/warsaw-dabrowka.zip": "warszawa",
    "https://cdn.zbiorkom.live/gtfs/pkp-skmw.zip": "warszawa",

    "https://cdn.zbiorkom.live/gtfs/krakow-bus.zip": "krakow",
    "https://cdn.zbiorkom.live/gtfs/krakow-tram.zip": "krakow",
    "https://cdn.zbiorkom.live/gtfs/krakow-mobilis.zip": "krakow",

    "https://cdn.zbiorkom.live/gtfs/tricity-gdansk.zip": "trojmiasto",
    "https://cdn.zbiorkom.live/gtfs/tricity-gdynia.zip": "trojmiasto",
    "https://mkuran.pl/gtfs/wejherowo.zip": "trojmiasto",
    "https://cdn.zbiorkom.live/gtfs/pkp-skmt.zip": "trojmiasto",

    "https://mkuran.pl/gtfs/gzm.zip": "gzm",
    "https://cdn.zbiorkom.live/gtfs/rybnik.zip": "gzm",
    "https://cdn.zbiorkom.live/gtfs/rybnik-jastrzebie.zip": "gzm",

    "https://cdn.zbiorkom.live/gtfs/wroclaw.zip": "wroclaw",
    "https://cdn.zbiorkom.live/gtfs/wroclaw-olesnica.zip": "wroclaw",
    "https://cdn.zbiorkom.live/gtfs/wroclaw-polbus.zip": "wroclaw",
    "https://cdn.zbiorkom.live/gtfs/wroclaw-siechnice.zip": "wroclaw",

    "https://cdn.zbiorkom.live/gtfs/poznan.zip": "poznan",
    "https://cdn.zbiorkom.live/gtfs/poznan-pks.zip": "poznan",
    "https://cdn.zbiorkom.live/gtfs/poznan-kombus.zip": "poznan",
    "https://cdn.zbiorkom.live/gtfs/poznan-sroda.zip": "poznan",

    "https://cdn.zbiorkom.live/gtfs/lodz.zip": "lodz",
    "https://cdn.zbiorkom.live/gtfs/lodz-lka.zip": "lodz",

    "https://cdn.zbiorkom.live/gtfs/szczecin.zip": "szczecin",
    "https://cdn.zbiorkom.live/gtfs/szczecin-goleniow.zip": "szczecin",

    "https://mkuran.pl/gtfs/rzeszow.zip": "rzeszow",
    "https://cdn.zbiorkom.live/gtfs/rzeszow-pks.zip": "rzeszow",

    "https://cdn.zbiorkom.live/gtfs/bialystok.zip": "bialystok",
    "https://cdn.zbiorkom.live/gtfs/bialystok-nova.zip": "bialystok",
    "https://cdn.zbiorkom.live/gtfs/bialystok-turosn.zip": "bialystok",
    "https://cdn.zbiorkom.live/gtfs/bialystok-wschod.zip": "bialystok",

    "https://mkuran.pl/gtfs/lublin.zip": "lublin",
    "https://mkuran.pl/gtfs/kielce.zip": "kielce",
    "https://mkuran.pl/gtfs/bydgoszcz.zip": "bydgoszcz",
    "https://mkuran.pl/gtfs/radom.zip": "radom",
    "https://mkuran.pl/gtfs/torun.zip": "torun",
    "https://cdn.zbiorkom.live/gtfs/olsztyn.zip": "olsztyn",
    "https://cdn.zbiorkom.live/gtfs/opole.zip": "opole",
    "https://cdn.zbiorkom.live/gtfs/czestochowa.zip": "czestochowa",
    "https://cdn.zbiorkom.live/gtfs/gorzow.zip": "gorzow",
    
    "https://mkuran.pl/gtfs/elk.zip": "elk",
    "https://mkuran.pl/gtfs/elblag.zip": "elblag",
    "https://mkuran.pl/gtfs/lomza.zip": "lomza",
    "https://mkuran.pl/gtfs/swinoujscie.zip": "swinoujscie",
    "https://mkuran.pl/gtfs/gizycko.zip": "gizycko",
    "https://cdn.zbiorkom.live/gtfs/suwalki.zip": "suwalki",
    "https://cdn.zbiorkom.live/gtfs/kutno.zip": "kutno",
    "https://cdn.zbiorkom.live/gtfs/legnica.zip": "legnica",
    "https://cdn.zbiorkom.live/gtfs/leszno.zip": "leszno",
    "https://cdn.zbiorkom.live/gtfs/przemysl.zip": "przemysl"
}

BLACKLIST = [
    "polish_trains", "pkp-ic", "pkp-pr", "pkp-ar", "pkp-km", 
    "pkp-kml", "pkp-ks", "pkp-kw", "pkp-kd", "pkp-rj", "rail"
]

CITIES_ROOT = Path("data/cities")

def fetch_worker(url, city):
    filename = url.split('/')[-1]
    if any(b in filename for b in BLACKLIST):
        return f"[CZARNA LISTA] {filename}"
        
    target_dir = CITIES_ROOT / city / "gtfs" / filename.replace('.zip', '')
    target_dir.mkdir(parents=True, exist_ok=True)
    
    if (target_dir / "stops.txt").exists():
        return f"[POMINIĘTO] {city}/{filename} (już jest)"

    try:
        r = requests.get(url, stream=True, timeout=30)
        r.raise_for_status()
        zip_buffer = io.BytesIO(r.content)
        
        with zipfile.ZipFile(zip_buffer) as z:
            z.extractall(target_dir)
        return f"[SUKCES] {city}/{filename}"
    except Exception as e:
        return f"[BŁĄD] {city}/{filename}: {e}"

def fetch_all():
    print("=== PRAWDZIWY RÓWNOLEGŁY GTFS DOWNLOADER ===")
    tasks = list(GTFS_SOURCES.items())
    print(f"Ilość paczek do pobrania: {len(tasks)}")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(fetch_worker, url, city) for url, city in tasks]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    fetch_all()
