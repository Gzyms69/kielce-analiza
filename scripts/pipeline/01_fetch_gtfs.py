import os
import requests
import zipfile
import io
import time
import concurrent.futures
from pathlib import Path
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
    "https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/30e783e4-2bec-4a7d-bb22-ee3e3b26ca96/download/gtfsgoogle.zip": "trojmiasto",

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
    "https://mkuran.pl/gtfs/gorzow_wlkp.zip": "gorzow",
    
    "https://mkuran.pl/gtfs/elk.zip": "elk",
    "https://mkuran.pl/gtfs/elblag.zip": "elblag",
    "https://mkuran.pl/gtfs/lomza.zip": "lomza",
    "https://mkuran.pl/gtfs/swinoujscie.zip": "swinoujscie",
    "https://mkuran.pl/gtfs/gizycko.zip": "gizycko",
    "https://cdn.zbiorkom.live/gtfs/suwalki.zip": "suwalki",
    "https://cdn.zbiorkom.live/gtfs/kutno.zip": "kutno",
    "https://cdn.zbiorkom.live/gtfs/legnica.zip": "legnica",
    "https://cdn.zbiorkom.live/gtfs/leszno.zip": "leszno",
    "https://cdn.zbiorkom.live/gtfs/przemysl.zip": "przemysl",
    
    # --- DODATKOWE LOKALNE ---
    "https://cdn.zbiorkom.live/gtfs/tribus.zip": "lodz",
    "https://kasmar00.github.io/gtfs-warsaw-custom/feeds/warsaw-ferries/latest.zip": "warszawa",
    "http://komunikacja.bialystok.pl/cms/File/download/gtfs/google_transit.zip": "bialystok",
    
    # --- KOLEJ REGIONALNA ---
    "https://cdn.zbiorkom.live/gtfs/pkp-kd.zip": "wroclaw",   # Koleje Dolnośląskie
    "https://cdn.zbiorkom.live/gtfs/pkp-ks.zip": "gzm",       # Koleje Śląskie (zbiorkom)
    "https://koleje-ks.pl/gtfs/2025-2026.zip": "gzm",         # Koleje Śląskie (oficjalne)
    "https://cdn.zbiorkom.live/gtfs/pkp-km.zip": "warszawa",  # Koleje Mazowieckie
    "https://cdn.zbiorkom.live/gtfs/pkp-kml.zip": "krakow",   # Koleje Małopolskie
    "https://cdn.zbiorkom.live/gtfs/pkp-kw.zip": "poznan",    # Koleje Wielkopolskie
    "https://cdn.zbiorkom.live/gtfs/pkp-lka.zip": "lodz",     # ŁKA
    "https://cdn.zbiorkom.live/gtfs/pkp-ar.zip": "bydgoszcz", # Arriva
    "https://cdn.zbiorkom.live/gtfs/pkp-wkd.zip": "warszawa", # WKD
    
    # --- KOLEJ KRAJOWA / OGÓLNA ---
    "https://mkuran.pl/gtfs/polish_trains.zip": "rail"
}

def get_cities_root():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data")) / "cities"

def get_allowed_cities():
    cities_env = os.environ.get("PIPELINE_CITIES")
    if cities_env:
        return [c.strip() for c in cities_env.split(',')]
    return None

def fetch_worker(url, city, cities_root):
    filename = url.split('/')[-1]
        
    target_dir = cities_root / city / "gtfs" / filename.replace('.zip', '')
    target_dir.mkdir(parents=True, exist_ok=True)
    
    if (target_dir / "stops.txt").exists():
        return f"[POMINIĘTO] {city}/{filename} (już jest)"

    max_retries = 3
    for attempt in range(max_retries):
        try:
            r = requests.get(url, stream=True, timeout=30, verify=False)
            r.raise_for_status()
            zip_buffer = io.BytesIO(r.content)
            
            with zipfile.ZipFile(zip_buffer) as z:
                z.extractall(target_dir)
            return f"[SUKCES] {city}/{filename}"
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                return f"[BŁĄD] {city}/{filename}: {e}"

def fetch_all():
    print("=== PRAWDZIWY RÓWNOLEGŁY GTFS DOWNLOADER (Self-Healing) ===")
    cities_root = get_cities_root()
    allowed_cities = get_allowed_cities()
    
    tasks = []
    for url, city in GTFS_SOURCES.items():
        if allowed_cities and city not in allowed_cities:
            continue
        tasks.append((url, city))
        
    print(f"Ilość paczek do pobrania: {len(tasks)}")
    
    if not tasks:
        print("Brak zadań. Sprawdź filtry miast.")
        return

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(fetch_worker, url, city, cities_root) for url, city in tasks]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    fetch_all()
