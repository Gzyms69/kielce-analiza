import requests
import zipfile
import os
import io
from pathlib import Path

# --- CONFIG ---
GTFS_ROOT = Path("data/raw/gtfs")

# KOMPLETNA LISTA FEEDS (mkuran.pl + zbiorkom.live)
# Struktura: "Folder/Nazwa" -> "URL"
FEEDS = {
    # --- METROPOLIA WARSZAWSKA ---
    "warsaw/ztm": "https://mkuran.pl/gtfs/warsaw.zip",
    "warsaw/wkd": "https://mkuran.pl/gtfs/wkd.zip",
    "warsaw/lomianki": "https://cdn.zbiorkom.live/gtfs/warsaw-lomianki.zip",
    "warsaw/pruszkow": "https://cdn.zbiorkom.live/gtfs/warsaw-pruszkow.zip",
    "warsaw/otwock": "https://cdn.zbiorkom.live/gtfs/warsaw-otwock.zip",
    "warsaw/minsk": "https://cdn.zbiorkom.live/gtfs/warsaw-minsk.zip",
    "warsaw/zabki": "https://cdn.zbiorkom.live/gtfs/warsaw-zabki.zip",
    "warsaw/radzymin": "https://cdn.zbiorkom.live/gtfs/warsaw-radzymin.zip",
    "warsaw/sochaczew": "https://cdn.zbiorkom.live/gtfs/warsaw-sochaczew.zip",
    "warsaw/gpa": "https://cdn.zbiorkom.live/gtfs/warsaw-gpa.zip",
    "warsaw/dabrowka": "https://cdn.zbiorkom.live/gtfs/warsaw-dabrowka.zip",

    # --- METROPOLIA KRAKOWSKA ---
    "krakow/bus": "https://cdn.zbiorkom.live/gtfs/krakow-bus.zip",
    "krakow/tram": "https://cdn.zbiorkom.live/gtfs/krakow-tram.zip",
    "krakow/mobilis": "https://cdn.zbiorkom.live/gtfs/krakow-mobilis.zip",

    # --- METROPOLIA WROCŁAWSKA ---
    "wroclaw/ztp": "https://cdn.zbiorkom.live/gtfs/wroclaw.zip",
    "wroclaw/polbus": "https://cdn.zbiorkom.live/gtfs/wroclaw-polbus.zip",
    "wroclaw/olesnica": "https://cdn.zbiorkom.live/gtfs/wroclaw-olesnica.zip",
    "wroclaw/siechnice": "https://cdn.zbiorkom.live/gtfs/wroclaw-siechnice.zip",

    # --- METROPOLIA POZNAŃSKA ---
    "poznan/ztm": "https://cdn.zbiorkom.live/gtfs/poznan.zip",
    "poznan/pks": "https://cdn.zbiorkom.live/gtfs/poznan-pks.zip",
    "poznan/kombus": "https://cdn.zbiorkom.live/gtfs/poznan-kombus.zip",
    "poznan/sroda": "https://cdn.zbiorkom.live/gtfs/poznan-sroda.zip",

    # --- AGALOMERACJA ŚLĄSKA ---
    "gzm-metropolia": "https://mkuran.pl/gtfs/gzm.zip",
    "rybnik": "https://cdn.zbiorkom.live/gtfs/rybnik.zip",
    "rybnik-jastrzebie": "https://cdn.zbiorkom.live/gtfs/rybnik-jastrzebie.zip",

    # --- TRÓJMIASTO ---
    "tricity/gdansk": "https://cdn.zbiorkom.live/gtfs/tricity-gdansk.zip",
    "tricity/gdynia": "https://cdn.zbiorkom.live/gtfs/tricity-gdynia.zip",
    "wejherowo": "https://mkuran.pl/gtfs/wejherowo.zip",

    # --- INNE DUŻE I ŚREDNIE MIASTA ---
    "lodz": "https://cdn.zbiorkom.live/gtfs/lodz.zip",
    "lodz/lka": "https://cdn.zbiorkom.live/gtfs/lodz-lka.zip",
    "szczecin": "https://cdn.zbiorkom.live/gtfs/szczecin.zip",
    "szczecin/goleniow": "https://cdn.zbiorkom.live/gtfs/szczecin-goleniow.zip",
    "bydgoszcz": "https://mkuran.pl/gtfs/bydgoszcz.zip",
    "lublin": "https://mkuran.pl/gtfs/lublin.zip",
    "bialystok": "https://cdn.zbiorkom.live/gtfs/bialystok.zip",
    "bialystok/nova": "https://cdn.zbiorkom.live/gtfs/bialystok-nova.zip",
    "bialystok/turosn": "https://cdn.zbiorkom.live/gtfs/bialystok-turosn.zip",
    "bialystok/wschod": "https://cdn.zbiorkom.live/gtfs/bialystok-wschod.zip",
    "rzeszow": "https://mkuran.pl/gtfs/rzeszow.zip",
    "rzeszow/pks": "https://cdn.zbiorkom.live/gtfs/rzeszow-pks.zip",
    "radom": "https://mkuran.pl/gtfs/radom.zip",
    "torun": "https://mkuran.pl/gtfs/torun.zip",
    "kielce": "https://mkuran.pl/gtfs/kielce.zip",
    "olsztyn": "https://cdn.zbiorkom.live/gtfs/olsztyn.zip",
    "czestochowa": "https://cdn.zbiorkom.live/gtfs/czestochowa.zip",
    "opole": "https://cdn.zbiorkom.live/gtfs/opole.zip",
    "gorzow": "https://mkuran.pl/gtfs/gorzow_wlkp.zip",
    "legnica": "https://cdn.zbiorkom.live/gtfs/legnica.zip",
    "leszno": "https://cdn.zbiorkom.live/gtfs/leszno.zip",
    "elblag": "https://mkuran.pl/gtfs/elblag.zip",
    "elk": "https://mkuran.pl/gtfs/elk.zip",
    "swinoujscie": "https://mkuran.pl/gtfs/swinoujscie.zip",
    "lomza": "https://mkuran.pl/gtfs/lomza.zip",
    "suwalki": "https://cdn.zbiorkom.live/gtfs/suwalki.zip",
    "kutno": "https://cdn.zbiorkom.live/gtfs/kutno.zip",
    "przemysl": "https://cdn.zbiorkom.live/gtfs/przemysl.zip",
    "gizycko": "https://mkuran.pl/gtfs/gizycko.zip",
    "tribus": "https://cdn.zbiorkom.live/gtfs/tribus.zip",

    # --- KOLEJ ---
    "rail/polish-trains": "https://mkuran.pl/gtfs/polish_trains.zip",
    "rail/pkp-ic": "https://cdn.zbiorkom.live/gtfs/pkp-ic.zip",
    "rail/pkp-pr": "https://cdn.zbiorkom.live/gtfs/pkp-pr.zip",
    "rail/pkp-skmt": "https://cdn.zbiorkom.live/gtfs/pkp-skmt.zip"
}

def sync_gtfs(name, url):
    dest_dir = GTFS_ROOT / name
    if dest_dir.exists() and any(dest_dir.iterdir()):
        # print(f"[SKIP] {name} już istnieje.")
        return

    print(f"[FETCH] Pobieranie GTFS: {name}...")
    try:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        
        with zipfile.ZipFile(io.BytesIO(r.content)) as z:
            os.makedirs(dest_dir, exist_ok=True)
            z.extractall(dest_dir)
            print(f"[SUCCESS] {name} rozpakowany.")
            
    except Exception as e:
        print(f"[ERROR] Błąd przy {name}: {e}")

if __name__ == "__main__":
    GTFS_ROOT.mkdir(parents=True, exist_ok=True)
    for name, url in FEEDS.items():
        sync_gtfs(name, url)
