import geopandas as gpd
import pandas as pd
from pathlib import Path
import sqlite3

def test_combination():
    city_dir = Path("data/cities/lodz")
    # Używamy przystanków jako wzorca (są w WGS84)
    stops = gpd.read_file(city_dir / "smart_stops.gpkg").to_crs("EPSG:2180")
    stops_buffer = stops.buffer(5000).unary_union # Bufor 5km wokół miasta
    
    db_path = city_dir / "rcn" / "transactions.gpkg"
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query("SELECT easting, northing, tran_cena_brutto, lok_pow_uzyt, dok_data FROM transactions", conn)
    
    combos = [
        ("EPSG:2178", "XY"), ("EPSG:2178", "YX"),
        ("EPSG:2177", "XY"), ("EPSG:2177", "YX"),
        ("EPSG:2180", "XY"), ("EPSG:2180", "YX")
    ]
    
    for crs, order in combos:
        try:
            if order == "XY":
                gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.easting, df.northing), crs=crs)
            else:
                gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.northing, df.easting), crs=crs)
                
            gdf_1992 = gdf.to_crs("EPSG:2180")
            hits = gdf_1992[gdf_1992.intersects(stops_buffer)].shape[0]
            print(f"Combo {crs} {order} -> Hits: {hits}")
            
            if hits > 1000:
                print(f"!!! REAL WORKING COMBO FOUND: {crs} {order} !!!")
                gdf_1992.to_file(db_path, driver="GPKG", layer="transactions")
                return
        except: continue

if __name__ == "__main__":
    test_combination()
