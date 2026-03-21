import requests
import re
from pathlib import Path

def scrape_proxies():
    print("Scrapowanie darmowych list proxy...")
    sources = [
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt"
    ]
    
    proxy_list = []
    for url in sources:
        try:
            r = requests.get(url, timeout=10)
            proxies = re.findall(r"\d+\.\d+\.\d+\.\d+:\d+", r.text)
            proxy_list.extend(proxies)
            print(f"  Pobrano {len(proxies)} z {url}")
        except:
            print(f"  Błąd źródła: {url}")

    unique_proxies = list(set(proxy_list))
    with open("scripts/proxies.txt", "w") as f:
        f.write("\n".join(unique_proxies))
    
    print(f"Łącznie zebrano {len(unique_proxies)} unikalnych proxy. Zapisano w scripts/proxies.txt")

if __name__ == "__main__":
    scrape_proxies()
