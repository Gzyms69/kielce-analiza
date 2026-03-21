import subprocess
import os
from pathlib import Path

def test_kielce_rcn():
    output_gpkg = Path("data/cities/kielce/rcn/test_kielce.gpkg")
    if output_gpkg.exists():
        output_gpkg.unlink()
        
    wfs_url = "https://mapy.geoportal.gov.pl/wss/service/rcn"
    # Używamy poprawnego filtra OGC (dla WFS 1.1.0)
    where_clause = "teryt LIKE '2661%'"
    
    print(f"Testowe pobieranie Kielc (2661) przez OGR...")
    
    cmd = [
        "ogr2ogr",
        "-f", "GPKG",
        str(output_gpkg),
        f"WFS:{wfs_url}",
        "ms:lokale",
        "-where", where_clause,
        "-nln", "transactions",
        # Poprawny sposób ustawienia timeoutu w GDAL
        "--config", "GDAL_HTTP_TIMEOUT", "60",
        "--config", "OGR_WFS_PAGING_ALLOWED", "YES",
        "--config", "OGR_WFS_PAGE_SIZE", "1000"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("[OK] Proces zakończony sukcesem.")
        
        # Sprawdzanie wyniku
        import sqlite3
        conn = sqlite3.connect(output_gpkg)
        count = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
        conn.close()
        
        print(f"Pobrano rekordów: {count}")
        print(f"Rozmiar pliku: {output_gpkg.stat().st_size / (1024*1024):.2f} MB")
        
    except subprocess.CalledProcessError as e:
        print(f"[ERR] Błąd OGR: {e.stderr}")
    except Exception as e:
        print(f"[ERR] Błąd ogólny: {e}")

if __name__ == "__main__":
    test_kielce_rcn()
