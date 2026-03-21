import pandas as pd
import geopandas as gpd
import gtfs_kit as gk
from pathlib import Path
import zipfile

RAW_DATA_DIR = Path("data/raw")

def inspect_gpkg():
    print("\n--- [NSP 2021 Siatka 250m (.gpkg inside zip)] ---")
    zip_path = RAW_DATA_DIR / "NSP2021_TOT_GRID250m_GPKG.zip"
    with zipfile.ZipFile(zip_path, 'r') as z:
        gpkg_name = [f for f in z.namelist() if f.endswith('.gpkg')][0]
        print(f"File found in zip: {gpkg_name}")
        # GeoPandas reads directly from zip with the zip:// prefix
        gdf = gpd.read_file(f"zip://{zip_path}!{gpkg_name}")
        print(f"CRS: {gdf.crs}")
        print("\nINFO:")
        gdf.info()
        print("\nHEAD(3):")
        print(gdf.head(3))

def inspect_gml():
    print("\n--- [RCN Rejestr Cen Nieruchomości (.gml)] ---")
    gml_path = RAW_DATA_DIR / "rcn.gml"
    # GML loading can be slow or fail if complex, try to load at least first rows
    gdf = gpd.read_file(gml_path)
    print(f"CRS: {gdf.crs}")
    print("\nINFO:")
    gdf.info()
    print("\nHEAD(3):")
    print(gdf.head(3))

def inspect_gtfs():
    print("\n--- [Przystanki GTFS (stops.txt)] ---")
    stops_path = RAW_DATA_DIR / "bus/stops.txt"
    df = pd.read_csv(stops_path)
    print("\nINFO:")
    df.info()
    print("\nHEAD(3):")
    print(df.head(3))

try:
    inspect_gpkg()
except Exception as e:
    print(f"Error inspecting GPKG: {e}")

try:
    inspect_gml()
except Exception as e:
    print(f"Error inspecting GML: {e}")

try:
    inspect_gtfs()
except Exception as e:
    print(f"Error inspecting GTFS: {e}")
