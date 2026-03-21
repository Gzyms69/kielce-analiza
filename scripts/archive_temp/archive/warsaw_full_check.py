import requests
import time
import re

# --- CONFIG ---
WARSAW_PREFIX = "1465"
WFS_URL = "https://mapy.geoportal.gov.pl/wss/service/rcn"
DATE_START = "2025-01-01"

def warsaw_check():
    print(f"=== WERYFIKACJA TOTALNA: Warszawa ({WARSAW_PREFIX}*) od {DATE_START} ===")
    
    # Budujemy filtr OGC XML dla WFS 1.1.0
    filter_xml = f"""<ogc:Filter xmlns:ogc='http://www.opengis.net/ogc'>
        <ogc:And>
            <ogc:PropertyIsLike wildCard='*' singleChar='.' escapeChar='!'>
                <ogc:PropertyName>teryt</ogc:PropertyName>
                <ogc:Literal>{WARSAW_PREFIX}*</ogc:Literal>
            </ogc:PropertyIsLike>
            <ogc:PropertyIsGreaterThanOrEqualTo>
                <ogc:PropertyName>dok_data</ogc:PropertyName>
                <ogc:Literal>{DATE_START}</ogc:Literal>
            </ogc:PropertyIsGreaterThanOrEqualTo>
        </ogc:And>
    </ogc:Filter>"""

    params = {
        "service": "WFS",
        "version": "1.1.0",
        "request": "GetFeature",
        "typename": "ms:lokale",
        "filter": filter_xml,
        "resultType": "hits" # Najpierw pytamy o liczbe
    }

    try:
        # 1. Sprawdzamy liczbę trafień
        r_hits = requests.get(WFS_URL, params=params, timeout=30)
        match = re.search(r'numberOfFeatures="(\d+)"', r_hits.text)
        if not match:
            # WFS 1.1.0 moze uzywac innego atrybutu
            match = re.search(r'numberMatched="(\d+)"', r_hits.text)
            
        total = int(match.group(1)) if match else "Nieznana"
        print(f"  Znaleziono transakcji: {total}")

        if total != "Nieznana" and total > 0:
            # 2. Pobieramy pierwszą paczkę danych do inspekcji
            params["resultType"] = "results"
            params["count"] = 10
            r_data = requests.get(WFS_URL, params=params, timeout=30)
            
            # Ekstrakcja dat i terytów z paczki dla pewności
            dates = re.findall(r'<ms:dok_data>(.*?)</ms:dok_data>', r_data.text)
            teryt_codes = re.findall(r'<ms:teryt>(.*?)</ms:teryt>', r_data.text)
            prices = re.findall(r'<ms:tran_cena_brutto>(.*?)</ms:tran_cena_brutto>', r_data.text)

            print("\n  PRÓBKA DANYCH (10 pierwszych):")
            for d, t, p in zip(dates, teryt_codes, prices):
                print(f"    Data: {d} | TERYT: {t} | Cena: {p} zł")
            
            # FINALNA WALIDACJA
            wrong_date = [d for d in dates if d < DATE_START]
            wrong_teryt = [t for t in teryt_codes if not t.startswith(WARSAW_PREFIX)]
            
            if not wrong_date and not wrong_teryt:
                print("\n[POTWIERDZONO] Filtry działają w 100% poprawnie.")
            else:
                print("\n[BŁĄD] Filtry nadal przepuszczają śmieci!")
                if wrong_date: print(f"    Błędne daty: {wrong_date[:3]}")
                if wrong_teryt: print(f"    Błędne TERYT: {wrong_teryt[:3]}")

    except Exception as e:
        print(f"  [BŁĄD] {e}")

if __name__ == "__main__":
    warsaw_check()
