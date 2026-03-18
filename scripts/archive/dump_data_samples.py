import pandas as pd
from pathlib import Path
import sqlite3
import subprocess
import json

def get_gpkg_sample(path, layer, n=5):
    if not Path(path).exists(): return "FILE MISSING"
    try:
        with sqlite3.connect(path) as conn:
            cols = pd.read_sql_query(f"PRAGMA table_info({layer})", conn)
            # Pobieramy dane, ale pomijamy kolumny binarne (geometrię)
            data = pd.read_sql_query(f"SELECT * FROM {layer} LIMIT {n}", conn)
            # Konwersja wszystkiego na string dla bezpiecznego JSONa
            data_clean = data.applymap(lambda x: str(x) if isinstance(x, bytes) else x)
            return {"columns": cols[['name', 'type']].to_dict(), "sample": data_clean.to_dict()}
    except Exception as e:
        return f"ERROR: {e}"

def get_gml_sample(path, tag, n=1):
    if not Path(path).exists(): return "FILE MISSING"
    try:
        cmd = f"grep -A 20 '{tag}' '{path}' | head -n 40"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout
    except:
        return "ERROR"

def main():
    report = {}
    print("=== COLLECTING DATA DNA SAMPLES (v2) ===")
    
    # 1. RCN Warszawa
    report["RCN_WFS_Warszawa"] = get_gpkg_sample("data/cities/warszawa/rcn/transactions.gpkg", "transactions", n=3)
    
    # 2. RCN Łódź ZIP
    report["RCN_ZIP_Lodz_Transakcja"] = get_gml_sample("data/cities/lodz/rcn/2025.gml", "RCN_Transakcja")
    report["RCN_ZIP_Lodz_Dokument"] = get_gml_sample("data/cities/lodz/rcn/2025.gml", "RCN_Dokument")
    
    # 3. RCN Suwałki ZIP
    report["RCN_ZIP_Suwalki_Lokal"] = get_gml_sample("data/cities/suwalki/rcn/rcn_2063.gml", "RCN_Lokal")
    
    # 4. OSM Metadata (Kraków)
    report["OSM_Krakow_Multipolygons"] = get_gpkg_sample("data/cities/krakow/osm_full.gpkg", "multipolygons", n=1)
    
    # 5. GTFS Stops (Kielce)
    report["GTFS_Kielce_Stops"] = get_gpkg_sample("data/cities/kielce/smart_stops.gpkg", "smart_stops", n=1)

    with open("data_dna_dump.json", "w", encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print("\nDNA Dump v2 saved. Proceeding to final report.")

if __name__ == "__main__":
    main()
