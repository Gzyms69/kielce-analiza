import requests
import zipfile
import io
from pathlib import Path
import os

RECOVERY = {
    "2063": ("suwalki", "https://rcn.geoforum.pl/download.php?teryt=2063"),
    "1061": ("lodz", "https://rcn.geoforum.pl/download.php?teryt=1061")
}

def download_geoforum():
    print("=== START GEOFURUM RECOVERY ===\n")
    
    for teryt, (city, url) in RECOVERY.items():
        print(f"Pobieranie: {city.upper()} ({teryt})...")
        target_dir = Path(f"data/cities/{city}/rcn")
        target_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            # Używamy allow_redirects=True, aby obsłużyć zewnętrzne portale
            r = requests.get(url, allow_redirects=True, timeout=60)
            r.raise_for_status()
            
            content_type = r.headers.get('Content-Type', '')
            
            if 'zip' in content_type or r.content[:2] == b'PK':
                print(f"  [+] Wykryto archiwum ZIP. Rozpakowuję...")
                with zipfile.ZipFile(io.BytesIO(r.content)) as z:
                    for member in z.namelist():
                        if member.endswith('.gml'):
                            # Zapisujemy jako rcn_{teryt}.gml dla spójności
                            filename = f"rcn_{teryt}.gml"
                            with open(target_dir / filename, "wb") as f:
                                f.write(z.read(member))
                            print(f"  [OK] Wypakowano i ujednolicono: {filename}")
            elif 'xml' in content_type or 'gml' in content_type:
                print(f"  [+] Wykryto bezpośredni plik GML. Zapisuję...")
                filename = f"rcn_{teryt}.gml"
                with open(target_dir / filename, "wb") as f:
                    f.write(r.content)
                print(f"  [OK] Zapisano: {filename}")
            else:
                print(f"  [!] Nieoczekiwany typ danych: {content_type}. Prawdopodobnie wymagana interwencja na stronie.")
                if "lodz" in city:
                    print(f"  [INFO] Link dla Łodzi prowadzi do portalu zewnętrznego: {r.url}")
                    
        except Exception as e:
            print(f"  [ERR] {city}: {e}")

    print("\nCzyszczenie duplikatów i starych plików...")
    # Usuwamy pliki bez prefiksu 'rcn_', które mogły zostać z poprzednich sesji
    for city_folder in Path("data/cities").iterdir():
        rcn_dir = city_folder / "rcn"
        if rcn_dir.exists():
            for f in rcn_dir.glob("*.gml"):
                if not f.name.startswith("rcn_"):
                    f.unlink()
                    print(f"  [-] Usunięto duplikat: {f.name} w {city_folder.name}")

    print("\nUruchamiam finalną konsolidację...")
    os.system("python3 scripts/core/consolidate_rcn.py")

if __name__ == "__main__":
    download_geoforum()
