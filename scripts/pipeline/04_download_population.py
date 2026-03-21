import requests
import zipfile
import io
import os
import sys
from pathlib import Path
import urllib3

# Wyłączamy ostrzeżenia SSL dla źródeł rządowych
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Zweryfikowany link bezpośredni dostarczony przez użytkownika
DIRECT_DATA_URL = "https://geo.stat.gov.pl/atom-web/download/?fileId=73995564fe6126cc9d8eafd0c7fe822f&name=NSP2021_TOT_GRID250m_GPKG.zip"

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def download_population():
    dest_dir = get_data_dir() / "poland" / "population"
    dest_dir.mkdir(parents=True, exist_ok=True)
    target_path = dest_dir / "nsp2021_grid250m.gpkg"
    
    if target_path.exists() and target_path.stat().st_size > 1_000_000_000:
        print(f"Siatka populacji już istnieje w: {target_path}")
        return

    print(f"Pobieranie zweryfikowanej siatki populacji NSP 2021 (format GPKG)...")
    print(f"Źródło: {DIRECT_DATA_URL}")
    
    try:
        # Pobieranie paczki danych
        r = requests.get(DIRECT_DATA_URL, verify=False, stream=True, timeout=600)
        r.raise_for_status()
        
        print("Pobieranie na dysk (streaming)...")
        tmp_zip = dest_dir / "__nsp_download.zip"
        with open(tmp_zip, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print("Rozpakowywanie...")
        with zipfile.ZipFile(tmp_zip) as z:
            # Szukamy głównego pliku GPKG wewnątrz ZIP
            gpkg_names = [n for n in z.namelist() if n.endswith('.gpkg')]
            if gpkg_names:
                # Wybieramy najwiekszy plik lub pierwszy pasujący
                gpkg_name = gpkg_names[0]
                z.extract(gpkg_name, path=dest_dir)
                
                old_path = dest_dir / gpkg_name
                if old_path != target_path:
                    if target_path.exists(): os.remove(target_path)
                    os.rename(str(old_path), str(target_path))
                
                print(f"SUKCES! Siatka populacji zapisana w: {target_path}")
            else:
                print(f"BŁĄD: Nie znaleziono pliku .gpkg wewnątrz pobranej paczki ZIP.", file=sys.stderr)
                sys.exit(1)
        
        # Usun plik tymczasowy
        if tmp_zip.exists():
            tmp_zip.unlink()

    except Exception as e:
        print(f"BŁĄD KRYTYCZNY podczas pobierania populacji: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    download_population()
