import geopandas as gpd
import pandas as pd
import json
from pathlib import Path

def dry_run_rcn_targets():
    print("=== WERYFIKACJA 'DRY RUN': POKRYCIE RCN (TERYT) ===\n")
    
    test_cities_root = Path("test-pipeline/cities")
    original_cities_root = Path("data/cities")
    powiaty_path = Path("test-pipeline/poland/admin/powiaty.json")
    
    if not powiaty_path.exists():
        print(f"BŁĄD: Brak pliku powiatów: {powiaty_path}")
        return
        
    powiaty = gpd.read_file(powiaty_path).to_crs("EPSG:2180")
    
    print(f"{'MIASTO':15} | {'NOWE TERYT (Z symulacji poligonu)':35} | {'STARE TERYT (Root)':35} | {'RÓŻNICA'}")
    print("-" * 105)
    
    all_targets = set()
    total_old = 0
    total_new = 0

    for city_dir in sorted(test_cities_root.iterdir()):
        if not city_dir.is_dir(): continue
        city = city_dir.name
        
        zone_path = city_dir / "transport_zone.gpkg"
        
        # 1. Symulacja Nowych TERYT
        new_teryt_list = []
        if zone_path.exists():
            try:
                zone = gpd.read_file(zone_path).to_crs("EPSG:2180")
                intersecting = powiaty[powiaty.intersects(zone.union_all())]
                teryt_col = 'JPT_KOD_JE' if 'JPT_KOD_JE' in intersecting.columns else intersecting.columns[0]
                new_teryt_list = sorted(intersecting[teryt_col].tolist())
                all_targets.update(new_teryt_list)
            except Exception as e:
                new_teryt_list = [f"ERR: {e}"]
        else:
            new_teryt_list = ["BRAK STREFY"]

        # 2. Pobranie Starych TERYT z Root
        old_teryt_list = []
        old_target_file = original_cities_root / city / "rcn_targets.json"
        if old_target_file.exists():
            try:
                with open(old_target_file, "r") as f:
                    old_teryt_list = sorted(json.load(f))
            except:
                pass
                
        # 3. Porównanie
        total_new += len(new_teryt_list) if "ERR" not in str(new_teryt_list) and "BRAK" not in str(new_teryt_list) else 0
        total_old += len(old_teryt_list)
        
        new_str = ",".join(new_teryt_list)
        old_str = ",".join(old_teryt_list)
        
        diff = ""
        if new_str == old_str:
            diff = "IDENTYCZNE"
        else:
            added = set(new_teryt_list) - set(old_teryt_list)
            removed = set(old_teryt_list) - set(new_teryt_list)
            if added: diff += f"+{','.join(added)} "
            if removed: diff += f"-{','.join(removed)}"
            
        print(f"{city[:14]:15} | {new_str[:35]:35} | {old_str[:35]:35} | {diff}")

    print("-" * 105)
    print(f"PODSUMOWANIE:")
    print(f"Suma przypisań miasto-powiat w Starym Systemie: {total_old}")
    print(f"Suma przypisań miasto-powiat w Nowym Systemie: {total_new}")
    print(f"Łączna unikalna liczba TERYT (powiatów) do pobrania z Geoportalu: {len(all_targets)}")
    
    # Próbka TERYTów, by sprawdzić czy nie ma śmieci (np. cała Polska)
    print(f"\nLista unikalnych TERYT do pobrania:\n{sorted(list(all_targets))}")

if __name__ == "__main__":
    dry_run_rcn_targets()