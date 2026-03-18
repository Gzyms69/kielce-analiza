import geopandas as gpd
import requests
from pathlib import Path

def test_suwalki():
    powiaty_path = Path('data/poland/admin/powiaty.json')
    if not powiaty_path.exists():
        print("Błąd: Brak pliku powiaty.json")
        return

    powiaty = gpd.read_file(powiaty_path)
    # Szukamy zarówno miasta Suwałki jak i powiatu suwalskiego
    targets = powiaty[powiaty['JPT_NAZWA_'].str.contains('Suwałki', case=False)]
    
    url = 'https://mapy.geoportal.gov.pl/wss/service/rcn'
    
    for _, row in targets.iterrows():
        name = row['JPT_NAZWA_']
        minx, miny, maxx, maxy = row.geometry.bounds
        
        print(f"\n--- Test dla: {name} ---")
        
        # Próba 1: BBOX WGS84
        bbox_wgs84 = f"{minx},{miny},{maxx},{maxy},urn:ogc:def:crs:EPSG::4326"
        params = {
            "service": "WFS", "version": "1.1.0", "request": "GetFeature",
            "typename": "ms:lokale", "count": "10", "bbox": bbox_wgs84
        }
        try:
            r = requests.get(url, params=params, timeout=20)
            count = r.text.count("<ms:lokale")
            print(f"  BBOX WGS84 Result: {count} rekordów")
            if count == 0 and "Exception" in r.text:
                print(f"  Błąd serwera: {r.text[:200]}")
        except Exception as e:
            print(f"  Błąd połączenia: {e}")

if __name__ == "__main__":
    test_suwalki()
