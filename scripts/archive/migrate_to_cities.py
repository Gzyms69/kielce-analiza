import os
import shutil
from pathlib import Path

# --- CONFIG ---
TEMP_GTFS = Path("data/temp_gtfs")
TEMP_RCN = Path("data/temp_rcn")
TEMP_NET = Path("data/temp_network")
CITIES_ROOT = Path("data/cities")

# Mapowanie źródeł do głównych aglomeracji
# Jeśli źródło nie jest tu wymienione, zostanie potraktowane jako osobne miasto
AGLOMERATIONS = {
    "warszawa": ["warsaw", "warsaw/ztm", "warsaw/wkd", "warsaw/gpa", "warsaw/otwock", "warsaw/lomianki", "warsaw/pruszkow", "warsaw/minsk", "warsaw/zabki", "warsaw/radzymin", "warsaw/sochaczew", "warsaw/dabrowka"],
    "krakow": ["krakow", "krakow/bus", "krakow/tram", "krakow/mobilis", "krakow-bus", "krakow-tram", "krakow-mobilis"],
    "wroclaw": ["wroclaw", "wroclaw/ztp", "wroclaw/polbus", "wroclaw/olesnica", "wroclaw/siechnice"],
    "poznan": ["poznan", "poznan/ztm", "poznan/pks", "poznan/kombus", "poznan/sroda"],
    "trojmiasto": ["tricity", "tricity/gdansk", "tricity/gdynia", "tricity-gdansk", "tricity-gdynia", "wejherowo", "sopot"],
    "lodz": ["lodz", "lodz/lka"],
    "szczecin": ["szczecin", "szczecin/goleniow"],
    "bialystok": ["bialystok", "bialystok/nova", "bialystok/turosn", "bialystok/wschod"],
    "rzeszow": ["rzeszow", "rzeszow/pks"],
    "gzm": ["gzm-metropolia", "rybnik", "rybnik-jastrzebie"]
}

def migrate():
    print("Rozpoczynam migrację do struktury City-Centric...")
    CITIES_ROOT.mkdir(parents=True, exist_ok=True)

    # 1. Migracja GTFS
    for item in TEMP_GTFS.glob("**/*"):
        if item.is_dir() and (item / "stops.txt").exists():
            # Znajdujemy do której aglomeracji należy to źródło
            rel_path = str(item.relative_to(TEMP_GTFS))
            target_city = rel_path.split(os.sep)[0] # Domyślnie pierwszy człon
            
            for aglo, sources in AGLOMERATIONS.items():
                if rel_path in sources or any(s in rel_path for s in sources):
                    target_city = aglo
                    break
            
            dest_dir = CITIES_ROOT / target_city / "gtfs" / rel_path.replace(os.sep, "_")
            dest_dir.mkdir(parents=True, exist_ok=True)
            
            # Przenosimy pliki
            for f in item.iterdir():
                if f.is_file():
                    shutil.move(str(f), str(dest_dir / f.name))
            print(f"  [GTFS] {rel_path} -> cities/{target_city}/gtfs/")

    # 2. Migracja RCN (po kodach TERYT)
    # 1465 -> warszawa, 1261 -> krakow, 2661 -> kielce, 1463 -> radom
    rcn_map = {"1465": "warszawa", "1261": "krakow", "2661": "kielce", "1463": "radom"}
    if TEMP_RCN.exists():
        for f in TEMP_RCN.glob("*.gml"):
            teryt = f.stem
            city = rcn_map.get(teryt, f"powiat_{teryt}")
            dest_dir = CITIES_ROOT / city / "rcn"
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(f), str(dest_dir / f.name))
            print(f"  [RCN] {f.name} -> cities/{city}/rcn/")

    # 3. Migracja Network
    if TEMP_NET.exists():
        for f in TEMP_NET.glob("*.graphml"):
            city = f.name.split("_")[0]
            # Mapowanie nazw plików na nazwy aglomeracji
            if city == "warsaw": city = "warszawa"
            
            dest_dir = CITIES_ROOT / city / "network"
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(f), str(dest_dir / f.name))
            print(f"  [NET] {f.name} -> cities/{city}/network/")

    # 4. Cleanup
    shutil.rmtree(TEMP_GTFS, ignore_errors=True)
    shutil.rmtree(TEMP_RCN, ignore_errors=True)
    shutil.rmtree(TEMP_NET, ignore_errors=True)
    print("\nMigracja zakończona. Struktura City-Centric gotowa.")

if __name__ == "__main__":
    migrate()
