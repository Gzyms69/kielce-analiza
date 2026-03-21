import requests
import re

def debug_wfs():
    urls = [
        'https://mapy.geoportal.gov.pl/wss/service/rcn',
        'https://polska.geoportal.gov.pl/wss/service/PZGIK/RCN/WFS/CenyTransakcyjne'
    ]
    
    for url in urls:
        print(f"\n--- Analiza: {url} ---")
        try:
            r = requests.get(url + "?service=WFS&request=GetCapabilities", timeout=20)
            # Szukamy wszystkich nazw warstw w tagach <Name>
            layers = re.findall(r'<Name>(.*?)</Name>', r.text)
            print(f"Dostępne warstwy ({len(layers)}):")
            # Wypisujemy warstwy związane z lokalami
            for l in layers:
                if 'lokal' in l.lower() or 'transak' in l.lower():
                    print(f"  - {l}")
        except Exception as e:
            print(f"Błąd: {e}")

if __name__ == "__main__":
    debug_wfs()
