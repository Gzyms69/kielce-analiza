import requests
import zipfile
import io
from pathlib import Path
import geopandas as gpd
import pandas as pd

# Konfiguracja odzyskiwania (Powiaty, które zawiodły w WFS)
RECOVERY_TARGETS = {
    "1061": "lodz",
    "2063": "suwalki"
}

BASE_URL = "https://opendata.geoportal.gov.pl/rcn"

def recover_missing():
    print("=== START RCN RECOVERY (ZIP Packages) ===\n")
    
    for teryt, city in RECOVERY_TARGETS.items():
        print(f"Odzyskiwanie: {city.upper()} (TERYT: {teryt})...")
        url = f"{BASE_URL}/{teryt}.zip"
        target_dir = Path(f"data/cities/{city}/rcn")
        target_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            r = requests.get(url, timeout=60)
            if r.status_code == 404:
                # Czasami URL ma inny format lub plik nie istnieje
                print(f"  [!] Brak paczki na serwerze OpenData dla {teryt}")
                continue
            r.raise_for_status()
            
            # Wypakowanie GML-a z ZIP-a
            with zipfile.ZipFile(io.BytesIO(r.content)) as z:
                # Szukamy plików .gml w archiwum
                gml_files = [f for f in z.namelist() if f.endswith('.gml')]
                for gml in gml_files:
                    z.extract(gml, target_dir)
                    print(f"  [OK] Wypakowano: {gml}")
                    
        except Exception as e:
            print(f"  [ERR] {teryt}: {e}")

    print("\nPonowna konsolidacja po odzyskaniu...")
    # Wywołujemy nasz skrypt konsolidujący
    import subprocess
    subprocess.run(["python3", "scripts/core/consolidate_rcn.py"])

if __name__ == "__main__":
    recover_missing()
