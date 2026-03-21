import pandas as pd
import geopandas as gpd
from pathlib import Path
import zipfile
import sys
import io
import pyogrio

RAW_DATA_DIR = Path("data/raw")
REPORT_FILE = Path("data_report.txt")

# Funkcja pomocnicza do przechwytywania df.info() do stringa
def get_df_info(df):
    buffer = io.StringIO()
    df.info(buf=buffer)
    return buffer.getvalue()

with open(REPORT_FILE, "w", encoding="utf-8") as f:
    f.write("=== RAPORT INSPEKCJI DANYCH - KIELCE ANALIZA ===\n\n")

    # 1. NSP 2021 (GPKG)
    try:
        f.write("--- [1] NSP 2021 Siatka 250m --- \n")
        zip_path = RAW_DATA_DIR / "NSP2021_TOT_GRID250m_GPKG.zip"
        with zipfile.ZipFile(zip_path, 'r') as z:
            gpkg_name = [name for name in z.namelist() if name.endswith('.gpkg')][0]
            f.write(f"Plik wewnątrz zip: {gpkg_name}\n")
            gdf_nsp = gpd.read_file(f"zip://{zip_path}!{gpkg_name}")
            f.write(f"CRS: {gdf_nsp.crs}\n")
            f.write("\nINFO:\n")
            f.write(get_df_info(gdf_nsp))
            f.write("\nHEAD(3):\n")
            f.write(gdf_nsp.head(3).to_string())
            f.write("\n\n")
    except Exception as e:
        f.write(f"BŁĄD NSP: {e}\n\n")

    # 2. RCN (GML) - Inspekcja wszystkich warstw
    try:
        f.write("--- [2] RCN Rejestr Cen Nieruchomości (Wszystkie warstwy) --- \n")
        gml_path = RAW_DATA_DIR / "rcn.gml"
        layers = pyogrio.list_layers(gml_path)
        f.write(f"Znalezione warstwy w GML: {layers[:, 0]}\n\n")

        for layer_name in layers[:, 0]:
            f.write(f">> WARSTWA: {layer_name}\n")
            try:
                # Wczytujemy pierwsze 100 wierszy dla szybkości inspekcji
                gdf_layer = gpd.read_file(gml_path, layer=layer_name, rows=100)
                if hasattr(gdf_layer, 'crs'):
                    f.write(f"   CRS: {gdf_layer.crs}\n")
                else:
                    f.write("   CRS: Brak (prawdopodobnie tabela atrybutów)\n")
                
                f.write("   INFO:\n")
                f.write(get_df_info(gdf_layer))
                f.write("   HEAD(3):\n")
                f.write(gdf_layer.head(3).to_string())
            except Exception as layer_e:
                f.write(f"   Błąd wczytywania warstwy {layer_name}: {layer_e}\n")
            f.write("\n" + "="*50 + "\n")
    except Exception as e:
        f.write(f"BŁĄD GML: {e}\n\n")

    # 3. GTFS (STOPS)
    try:
        f.write("--- [3] GTFS Przystanki (stops.txt) --- \n")
        stops_path = RAW_DATA_DIR / "bus/stops.txt"
        df_stops = pd.read_csv(stops_path)
        f.write("INFO:\n")
        f.write(get_df_info(df_stops))
        f.write("\nHEAD(3):\n")
        f.write(df_stops.head(3).to_string())
        f.write("\n\n")
    except Exception as e:
        f.write(f"BŁĄD GTFS: {e}\n\n")

print(f"Inspekcja zakończona. Wyniki zapisano w: {REPORT_FILE}")
