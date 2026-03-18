import sqlite3
import pandas as pd
import geopandas as gpd
from pathlib import Path

# --- CONFIG ---
DB_PATH = "data/database/transport_metrics.db"
STOPS_GPKG = "data/processed/kielce_stops.gpkg"
GRID_GPKG = "data/processed/kielce_analytical_grid.gpkg"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Tabela Miast
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            lat REAL,
            lon REAL
        )
    ''')

    # 2. Tabela Przystanków (Z metrykami przestrzennymi i ekonomicznymi)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stops (
            stop_id INTEGER PRIMARY KEY,
            city_id INTEGER,
            name TEXT,
            lat REAL,
            lon REAL,
            population_250m INTEGER,
            price_m2_median REAL,
            frequency_per_hour INTEGER,
            FOREIGN KEY (city_id) REFERENCES cities(id)
        )
    ''')

    # 3. Tabela Relacji (Analiza Dubli i Barier)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stop_relations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_id INTEGER,
            stop_a_id INTEGER,
            stop_b_id INTEGER,
            dist_straight REAL,
            dist_network REAL,
            detour_factor REAL,
            overlap_lines_count INTEGER,
            FOREIGN KEY (city_id) REFERENCES cities(id),
            FOREIGN KEY (stop_a_id) REFERENCES stops(stop_id),
            FOREIGN KEY (stop_b_id) REFERENCES stops(stop_id)
        )
    ''')

    conn.commit()
    conn.close()
    print(f"Baza danych SQL zainicjalizowana w: {DB_PATH}")

if __name__ == "__main__":
    init_db()
