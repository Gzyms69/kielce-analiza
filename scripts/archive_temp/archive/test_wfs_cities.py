import requests

def check_city(teryt, name):
    url = 'https://mapy.geoportal.gov.pl/wss/service/rcn'
    # Dokładny filtr XML z poprzedniego, "działającego" skryptu (bez daty, aby sprawdzić cokolwiek)
    xml = f"""<ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
                <ogc:PropertyIsLike wildCard="*" singleChar="." escapeChar="!">
                    <ogc:PropertyName>teryt</ogc:PropertyName>
                    <ogc:Literal>{teryt}*</ogc:Literal>
                </ogc:PropertyIsLike>
              </ogc:Filter>"""
              
    params = {
        'service': 'WFS',
        'version': '1.1.0',
        'request': 'GetFeature',
        'typename': 'ms:lokale',
        'filter': xml,
        'count': 5
    }
    
    try:
        r = requests.get(url, params=params, timeout=15)
        count = r.text.count("<ms:lokale")
        print(f"{name} ({teryt}): {count} rekordów")
    except Exception as e:
        print(f"{name} ({teryt}): Błąd {e}")

if __name__ == "__main__":
    print("Sprawdzanie dostępności głównych aglomeracji na serwerze WFS...")
    check_city('0264', 'Wrocław')
    check_city('3064', 'Poznań')
    check_city('1061', 'Łódź')
    check_city('2063', 'Suwałki')
