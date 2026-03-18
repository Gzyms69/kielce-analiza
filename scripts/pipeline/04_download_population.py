import requests
import xml.etree.ElementTree as ET
import zipfile
import io
import os
from pathlib import Path
import urllib3

# Wyłączamy ostrzeżenia SSL dla bezpiecznych, znanych źródeł rządowych
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ATOM_MAIN_URL = "https://geo.stat.gov.pl/atom-web/atom/GRID"
DEST_DIR = Path("data/poland/population")
NS = {'atom': 'http://www.w3.org/2005/Atom'}

def recover():
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    print("KROK 1: Analiza głównego feedu ATOM GUS...")
    
    try:
        # Pobieramy feed główny
        r = requests.get(ATOM_MAIN_URL, verify=False, timeout=30)
        r.raise_for_status()
        root = ET.fromstring(r.content)
        
        sub_feed_url = None
        for entry in root.findall('atom:entry', NS):
            title = entry.find('atom:title', NS).text
            # Szukamy zasobu 32250 (NSP 2021)
            if "NSP 2021" in title and "250m" in title:
                sub_feed_url = entry.find('atom:link', NS).attrib['href']
                print(f"  Znaleziono sub-feed dla: {title}")
                break
        
        if not sub_feed_url:
            print("  BŁĄD: Nie znaleziono sub-feedu dla NSP 2021 250m.")
            return

        print("KROK 2: Analiza sub-feedu w poszukiwaniu formatu GPKG...")
        r_sub = requests.get(sub_feed_url, verify=False, timeout=30)
        r_sub.raise_for_status()
        sub_root = ET.fromstring(r_sub.content)
        
        data_url = None
        for entry in sub_root.findall('atom:entry', NS):
            entry_title = entry.find('atom:title', NS).text
            # Szukamy konkretnie paczki GPKG 250m
            if "250m" in entry_title and "GPKG" in entry_title:
                data_url = entry.find('atom:link', NS).attrib['href']
                print(f"  Znaleziono bezpośredni link do danych: {data_url}")
                break
        
        if not data_url:
            print("  BŁĄD: Nie znaleziono pliku GPKG w sub-feedzie.")
            return

        print(f"KROK 3: Pobieranie paczki danych (ok. 170MB)...")
        r_file = requests.get(data_url, verify=False, stream=True, timeout=300)
        r_file.raise_for_status()
        
        with zipfile.ZipFile(io.BytesIO(r_file.content)) as z:
            gpkg_names = [n for n in z.namelist() if n.endswith('.gpkg')]
            if gpkg_names:
                gpkg_name = gpkg_names[0]
                z.extract(gpkg_name, path=DEST_DIR)
                
                old_path = DEST_DIR / gpkg_name
                new_path = DEST_DIR / "nsp2021_grid250m.gpkg"
                
                if old_path != new_path:
                    if new_path.exists(): os.remove(new_path)
                    os.rename(str(old_path), str(new_path))
                
                print(f"SUKCES! Siatka populacji odzyskana i zapisana w: {new_path}")
            else:
                print("BŁĄD: Brak pliku .gpkg wewnątrz ZIP.")

    except Exception as e:
        print(f"BŁĄD KRYTYCZNY: {e}")

if __name__ == "__main__":
    recover()
