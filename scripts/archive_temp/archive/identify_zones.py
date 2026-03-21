import geopandas as gpd
import pandas as pd
from pathlib import Path

# --- CONFIG ---
STOPS_GPKG = "data/processed/all_stops_poland.gpkg"
POWIATY_JSON = "data/raw/admin/powiaty.json"
OUTPUT_CSV = "reports/counties_to_fetch.csv"

def identify_zones():
    print("Wczytywanie 85k przystanków...")
    stops = gpd.read_file(STOPS_GPKG)
    
    print("Wczytywanie granic powiatów...")
    counties = gpd.read_file(POWIATY_JSON)
    
    # Upewniamy się że układy się zgadzają
    # powiaty.json z GitHub zazwyczaj jest w WGS84 (EPSG:4326)
    if counties.crs is None:
        counties.set_crs("EPSG:4326", inplace=True)
    
    counties = counties.to_crs(stops.crs)
    
    print("Wykonuję Spatial Join (Przystanki x Powiaty)...")
    # SJOIN: Każdy przystanek dostaje kod i nazwę powiatu
    joined = gpd.sjoin(stops, counties[['JPT_KOD_JE', 'JPT_NAZWA_', 'geometry']], how="inner", predicate="within")
    
    # Agregacja do unikalnych powiatów
    target_counties = (
        joined.groupby(['JPT_KOD_JE', 'JPT_NAZWA_'])
        .size()
        .reset_index(name='stop_count')
        .sort_values('stop_count', ascending=False)
    )
    
    # Mapowanie nazw kolumn na czytelniejsze
    target_counties.columns = ['teryt_code', 'county_name', 'stop_count']
    
    print(f"Zidentyfikowano {len(target_counties)} powiatów z aktywną komunikacją miejską.")
    print(target_counties.head(10))
    
    # Zapisujemy listę
    target_counties.to_csv(OUTPUT_CSV, index=False)
    print(f"Lista zapisana w: {OUTPUT_CSV}")

    # Aktualizacja DevLog
    with open("devlog.md", "a") as f:
        f.write(f"\n### 14. Precyzyjna identyfikacja powiatów TERYT\n- **Działanie:** Wykonanie lokalnego Spatial Join na 85k przystankach i oficjalnych granicach powiatów.\n- **Uzasadnienie:** Wykryto {len(target_counties)} powiatów, przez które faktycznie przebiegają linie komunikacyjne. To jest nasza lista zakupowa dla WFS RCN.\n")

if __name__ == "__main__":
    identify_zones()
