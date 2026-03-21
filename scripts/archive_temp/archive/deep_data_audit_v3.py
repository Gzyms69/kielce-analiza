import os
import json
import sqlite3
import pandas as pd
from pathlib import Path

CITIES_ROOT = Path("data/cities")

def get_sqlite_count(db_path, table_name):
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cur.fetchone()[0]
        conn.close()
        return count
    except:
        return 0

def get_other_tags_sample(db_path, table_name):
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        # Wyciągamy pierwsze 3 niepuste other_tags
        cur.execute(f"SELECT other_tags FROM {table_name} WHERE other_tags IS NOT NULL LIMIT 3")
        rows = cur.fetchall()
        conn.close()
        return [r[0] for r in rows]
    except:
        return []

def audit_all():
    print("=== GLOBALNY AUDYT DANYCH PRZESTRZENNYCH (FAZA 3) ===\n")
    cities = sorted([d for d in CITIES_ROOT.iterdir() if d.is_dir()])
    
    total_stops = 0
    total_osm_size = 0
    
    for city in cities:
        city_name = city.name.upper()
        print(f"[{city_name}]")
        
        # 1. Audyt Przystanków
        stops_db = city / "smart_stops.gpkg"
        if stops_db.exists():
            stops_count = get_sqlite_count(stops_db, "smart_stops")
            total_stops += stops_count
            print(f"  -> Przystanki (Smart Stops): {stops_count:,}".replace(',', ' '))
        else:
            print(f"  -> Przystanki: BRAK PLIKU!")

        # 2. Audyt OSM
        osm_db = city / "osm_full.gpkg"
        if osm_db.exists():
            size_mb = osm_db.stat().st_size / (1024 * 1024)
            total_osm_size += size_mb
            
            pts = get_sqlite_count(osm_db, "points")
            lines = get_sqlite_count(osm_db, "lines")
            polys = get_sqlite_count(osm_db, "multipolygons")
            
            print(f"  -> Baza OSM ({size_mb:.1f} MB):")
            print(f"     * Punkty (drzewa, śmietniki, lampy): {pts:,}".replace(',', ' '))
            print(f"     * Linie (drogi, chodniki):           {lines:,}".replace(',', ' '))
            print(f"     * Poligony (budynki, parki):         {polys:,}".replace(',', ' '))
            
            # Próbka tagów dla udowodnienia "Take Everything"
            if city_name == "WARSZAWA": # Pokażemy próbkę tylko dla Wawy, żeby nie zalać konsoli
                sample = get_other_tags_sample(osm_db, "multipolygons")
                print("     * PRÓBKA 'other_tags' (Dowód pobrania wszystkich atrybutów):")
                for s in sample:
                    # Skracamy do 100 znaków dla czytelności
                    print(f"       - {s[:100]}...")
        else:
            print(f"  -> Baza OSM: BRAK PLIKU!")
        print("-" * 50)
        
    print(f"PODSUMOWANIE GLOBALNE:")
    print(f"Łączna liczba wyselekcjonowanych przystanków: {total_stops:,}".replace(',', ' '))
    print(f"Całkowity rozmiar danych OSM: {total_osm_size:.1f} MB")

if __name__ == "__main__":
    audit_all()
