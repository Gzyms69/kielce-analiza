import requests
import xml.etree.ElementTree as ET
import urllib3

urllib3.disable_warnings()

def check_wms_raw():
    url = "https://mapy.geoportal.gov.pl/wss/service/PZGIK/RCN/WMS/PobieranieRCN?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities"
    r = requests.get(url, verify=False)
    
    # Zapisujemy do pliku, żeby podejrzeć strukturę, jeśli parser znowu zawiedzie
    with open("wms_capabilities.xml", "w", encoding="utf-8") as f:
        f.write(r.text)
        
    xml_str = r.text.replace(' xmlns="http://www.opengis.net/wms"', '')
    root = ET.fromstring(xml_str)
    
    print("Wszystkie znalezione nazwy warstw (Name):")
    # Szukamy absolutnie wszystkich tagów Name w całym dokumencie
    for name in root.iter('Name'):
        print(f"  - {name.text}")
        
if __name__ == "__main__":
    check_wms_raw()
