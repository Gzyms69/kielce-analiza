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

GTFS_SOURCES = {
    # --- WARSZAWA ---
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
    "https://kasmar00.github.io/gtfs-warsaw-custom/feeds/warsaw-ferries/latest.zip": "warszawa",
    "https://cdn.zbiorkom.live/gtfs/pkp-km.zip": "warszawa",
    "https://cdn.zbiorkom.live/gtfs/pkp-wkd.zip": "warszawa",

    # --- KRAKOW ---
    "https://cdn.zbiorkom.live/gtfs/krakow-bus.zip": "krakow",
    "https://cdn.zbiorkom.live/gtfs/krakow-tram.zip": "krakow",
    "https://cdn.zbiorkom.live/gtfs/krakow-mobilis.zip": "krakow",
    "https://cdn.zbiorkom.live/gtfs/pkp-kml.zip": "krakow",

    # --- TROJMIASTO ---
    "https://cdn.zbiorkom.live/gtfs/tricity-gdansk.zip": "trojmiasto",
    "https://cdn.zbiorkom.live/gtfs/tricity-gdynia.zip": "trojmiasto",
    "https://mkuran.pl/gtfs/wejherowo.zip": "trojmiasto",
    "https://cdn.zbiorkom.live/gtfs/pkp-skmt.zip": "trojmiasto",
    "https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/30e783e4-2bec-4a7d-bb22-ee3e3b26ca96/download/gtfsgoogle.zip": "trojmiasto",

    # --- GZM ---
    "https://mkuran.pl/gtfs/gzm.zip": "gzm",
    "https://cdn.zbiorkom.live/gtfs/rybnik.zip": "gzm",
    "https://cdn.zbiorkom.live/gtfs/rybnik-jastrzebie.zip": "gzm",
    "https://cdn.zbiorkom.live/gtfs/pkp-ks.zip": "gzm",
    "https://koleje-ks.pl/gtfs/2025-2026.zip": "gzm",

    # --- WROCLAW ---
    "https://cdn.zbiorkom.live/gtfs/wroclaw.zip": "wroclaw",
    "https://cdn.zbiorkom.live/gtfs/wroclaw-olesnica.zip": "wroclaw",
    "https://cdn.zbiorkom.live/gtfs/wroclaw-polbus.zip": "wroclaw",
    "https://cdn.zbiorkom.live/gtfs/wroclaw-siechnice.zip": "wroclaw",
    "https://cdn.zbiorkom.live/gtfs/pkp-kd.zip": "wroclaw",

    # --- POZNAN ---
    "https://cdn.zbiorkom.live/gtfs/poznan.zip": "poznan",
    "https://cdn.zbiorkom.live/gtfs/poznan-pks.zip": "poznan",
    "https://cdn.zbiorkom.live/gtfs/poznan-kombus.zip": "poznan",
    "https://cdn.zbiorkom.live/gtfs/poznan-sroda.zip": "poznan",
    "https://cdn.zbiorkom.live/gtfs/pkp-kw.zip": "poznan",

    # --- LODZ ---
    "https://cdn.zbiorkom.live/gtfs/lodz.zip": "lodz",
    "https://cdn.zbiorkom.live/gtfs/lodz-lka.zip": "lodz",
    "https://cdn.zbiorkom.live/gtfs/tribus.zip": "lodz",
    "https://cdn.zbiorkom.live/gtfs/pkp-lka.zip": "lodz",

    # --- SZCZECIN ---
    "https://cdn.zbiorkom.live/gtfs/szczecin.zip": "szczecin",
    "https://cdn.zbiorkom.live/gtfs/szczecin-goleniow.zip": "szczecin",

    # --- BIALYSTOK ---
    "https://cdn.zbiorkom.live/gtfs/bialystok.zip": "bialystok",
    "https://cdn.zbiorkom.live/gtfs/bialystok-nova.zip": "bialystok",
    "https://cdn.zbiorkom.live/gtfs/bialystok-turosn.zip": "bialystok",
    "https://cdn.zbiorkom.live/gtfs/bialystok-wschod.zip": "bialystok",
    "http://komunikacja.bialystok.pl/cms/File/download/gtfs/google_transit.zip": "bialystok",

    # --- INNE ---
    "https://mkuran.pl/gtfs/rzeszow.zip": "rzeszow",
    "https://cdn.zbiorkom.live/gtfs/rzeszow-pks.zip": "rzeszow",
    "https://mkuran.pl/gtfs/lublin.zip": "lublin",
    "https://mkuran.pl/gtfs/kielce.zip": "kielce",
    "https://mkuran.pl/gtfs/bydgoszcz.zip": "bydgoszcz",
    "https://cdn.zbiorkom.live/gtfs/pkp-ar.zip": "bydgoszcz",
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

    # --- NOWE MIASTA (>100k mieszkancow) ---
    "https://cdn.zbiorkom.live/gtfs/bielsko-biala.zip": "bielsko-biala",
    "https://www.mzk.zgora.pl/storage/website/dla_deweloperow_yyvw6.zip": "zielona-gora",
    "https://cdn.zbiorkom.live/gtfs/plock.zip": "plock",
    "https://cdn.zbiorkom.live/gtfs/walbrzych.zip": "walbrzych",
    "https://cdn.zbiorkom.live/gtfs/wloclawek.zip": "wloclawek",
    "https://cdn.zbiorkom.live/gtfs/tarnow.zip": "tarnow",
    "https://cdn.zbiorkom.live/gtfs/koszalin.zip": "koszalin",
    "https://cdn.zbiorkom.live/gtfs/kalisz.zip": "kalisz",
    "https://cdn.zbiorkom.live/gtfs/grudziadz.zip": "grudziadz",
    "https://cdn.zbiorkom.live/gtfs/slupsk.zip": "slupsk",

    # --- OSRODKI REGIONALNE (50k-90k) ---
    "https://cdn.zbiorkom.live/gtfs/siedlce.zip": "siedlce",
    "https://cdn.zbiorkom.live/gtfs/nowy-sacz.zip": "nowy-sacz",
    "https://cdn.zbiorkom.live/gtfs/jelenia-gora.zip": "jelenia-gora",
    "https://cdn.zbiorkom.live/gtfs/konin.zip": "konin",
    "https://cdn.zbiorkom.live/gtfs/pila.zip": "pila",
    "https://cdn.zbiorkom.live/gtfs/inowroclaw.zip": "inowroclaw",
    "https://cdn.zbiorkom.live/gtfs/ostrow-wlkp.zip": "ostrow-wlkp",
    "https://cdn.zbiorkom.live/gtfs/gniezno.zip": "gniezno",
    "https://cdn.zbiorkom.live/gtfs/stargard.zip": "stargard",
    "https://cdn.zbiorkom.live/gtfs/glogow.zip": "glogow",

    # --- SCIANA WSCHODNIA I POLUDNIOWO-WSCHODNIA ---
    "https://cdn.zbiorkom.live/gtfs/zamosc.zip": "zamosc",
    "https://cdn.zbiorkom.live/gtfs/chelm.zip": "chelm",
    "https://cdn.zbiorkom.live/gtfs/biala-podlaska.zip": "biala-podlaska",
    "https://cdn.zbiorkom.live/gtfs/mielec.zip": "mielec",
    "https://cdn.zbiorkom.live/gtfs/stalowa-wola.zip": "stalowa-wola",
    "https://cdn.zbiorkom.live/gtfs/tarnobrzeg.zip": "tarnobrzeg",

    # --- ZAGLEBIE MIEDZIOWE I ZACHOD ---
    "https://cdn.zbiorkom.live/gtfs/lubin.zip": "lubin",
    "https://cdn.zbiorkom.live/gtfs/boleslawiec.zip": "boleslawiec",
    
    # --- KOLEJ KRAJOWA / OGÓLNA (ARCHITEKTURA WYSPOWA) ---
    "https://mkuran.pl/gtfs/polish_trains.zip": "rail"
}

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
            zip_buffer = io.BytesIO(r.content)
            
            with zipfile.ZipFile(zip_buffer) as z:
                z.extractall(target_dir)
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
