import geopandas as gpd
import pandas as pd
from lxml import etree
from pathlib import Path
import os
import sys
from shapely.geometry import Point, Polygon

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def get_allowed_cities():
    cities_env = os.environ.get("PIPELINE_CITIES")
    if cities_env:
        return [c.strip() for c in cities_env.split(',')]
    return None

def clean_ref(ref):
    if not ref: return None
    return ref.split('/')[-1].replace('#', '')

def fix_suwalki_centroid():
    allowed_cities = get_allowed_cities()
    if allowed_cities and "suwalki" not in allowed_cities:
        return

    print("--- FIXING SUWAŁKI: STREAMING PARSER & M2 MAPPING ---")
    data_dir = get_data_dir().resolve()
    city_dir = data_dir / "cities" / "suwalki" / "rcn"
    
    gml_files = list(city_dir.glob("**/*.gml"))
    if not gml_files:
        print(f"  [SKIP] Brak plików GML dla Suwałk w {city_dir}")
        return

    gml_path = gml_files[0]
    print(f"  Przetwarzanie strumieniowe pliku: {gml_path.name}")

    ns = {
        'rcn': 'urn:gugik:specyfikacje:gmlas:rejestrcennieruchomosci:1.0',
        'gml': 'http://www.opengis.net/gml/3.2',
        'xlink': 'http://www.w3.org/1999/xlink'
    }

    geo_map = {}
    docs = {}
    lokale_m2 = {}
    niers = {}
    transactions = []

    # STREAMING PARSE: Zapobiega wyciekom pamięci i przyspiesza proces
    context = etree.iterparse(str(gml_path), events=('end',), tag=(
        '{urn:gugik:specyfikacje:gmlas:rejestrcennieruchomosci:1.0}RCN_Budynek',
        '{urn:gugik:specyfikacje:gmlas:rejestrcennieruchomosci:1.0}RCN_Dzialka',
        '{urn:gugik:specyfikacje:gmlas:rejestrcennieruchomosci:1.0}RCN_Dokument',
        '{urn:gugik:specyfikacje:gmlas:rejestrcennieruchomosci:1.0}RCN_Lokal',
        '{urn:gugik:specyfikacje:gmlas:rejestrcennieruchomosci:1.0}RCN_Nieruchomosc',
        '{urn:gugik:specyfikacje:gmlas:rejestrcennieruchomosci:1.0}RCN_Transakcja'
    ))

    for event, elem in context:
        tag = elem.tag.split('}')[-1]
        gml_id = elem.get('{http://www.opengis.net/gml/3.2}id')

        if tag in ['RCN_Budynek', 'RCN_Dzialka']:
            pos = elem.xpath('.//gml:pos/text()', namespaces=ns) or elem.xpath('.//gml:posList/text()', namespaces=ns)
            if pos:
                coords = [float(x) for x in pos[0].split()]
                if len(coords) >= 2:
                    if len(coords) == 2: geom = Point(coords[0], coords[1])
                    else:
                        it = iter(coords)
                        poly_pts = list(zip(it, it))
                        if len(poly_pts) >= 3: geom = Polygon(poly_pts).centroid
                        else: geom = Point(poly_pts[0])
                    geo_map[gml_id] = geom

        elif tag == 'RCN_Dokument':
            date_text = elem.xpath('./rcn:dataSporzadzeniaDokumentu/text()', namespaces=ns)
            if date_text: docs[gml_id] = date_text[0]

        elif tag == 'RCN_Lokal':
            m2 = elem.xpath('./rcn:powUzytkowaLokalu/text()', namespaces=ns)
            if m2: lokale_m2[gml_id] = float(m2[0])

        elif tag == 'RCN_Nieruchomosc':
            l_ref = clean_ref(elem.xpath('./rcn:lokal/@xlink:href', namespaces=ns)[0]) if elem.xpath('./rcn:lokal/@xlink:href', namespaces=ns) else None
            parents = [clean_ref(p) for p in elem.xpath('./rcn:budynek/@xlink:href', namespaces=ns) + elem.xpath('./rcn:dzialka/@xlink:href', namespaces=ns)]
            niers[gml_id] = {'l_ref': l_ref, 'parents': parents}

        elif tag == 'RCN_Transakcja':
            price = elem.xpath('./rcn:cenaTransakcjiBrutto/text()', namespaces=ns)
            d_ref = elem.xpath('./rcn:podstawaPrawna/@xlink:href', namespaces=ns)
            n_refs = elem.xpath('./rcn:nieruchomosc/@xlink:href', namespaces=ns)
            
            transactions.append({
                'price': float(price[0]) if price else 0,
                'doc_id': clean_ref(d_ref[0]) if d_ref else None,
                'nier_ids': [clean_ref(nr) for nr in n_refs]
            })

        elem.clear()
        while elem.getprevious() is not None:
            del elem.getparent()[0]

    print(f"  Wstępnie zmapowano {len(geo_map)} obiektów i {len(transactions)} transakcji.")

    # 2. ŁĄCZENIE DANYCH
    final_features = []
    for t in transactions:
        final_date = docs.get(t['doc_id'])
        for n_id in t['nier_ids']:
            if n_id in niers:
                l_id = niers[n_id]['l_ref']
                m2_val = lokale_m2.get(l_id)
                for p_id in niers[n_id]['parents']:
                    if p_id in geo_map:
                        final_features.append({
                            'tran_cena_brutto': t['price'],
                            'dok_data': final_date,
                            'geometry': geo_map[p_id],
                            'lok_pow_uzyt': m2_val
                        })
                        break

    if final_features:
        gdf = gpd.GeoDataFrame(final_features, crs="EPSG:2180")
        gdf['dok_data'] = pd.to_datetime(gdf['dok_data'], errors='coerce')
        gdf = gdf[gdf['dok_data'] >= '2025-01-01']
        
        out_file = data_dir / "cities" / "suwalki" / "02_spatial" / "transactions.gpkg"
        out_file.parent.mkdir(parents=True, exist_ok=True)
        
        # KOREKTA: Twarde nadpisywanie. Żadnego append, które niszczyło bazę.
        if out_file.exists():
            os.remove(out_file)
            
        gdf.to_file(out_file, driver="GPKG", layer="transactions")
        print(f"  [SUKCES] Zapisano {len(gdf)} rekordów dla Suwałk w 02_spatial.")
    else:
        print("  [UWAGA] Brak kompletnych transakcji do zapisu.")

if __name__ == "__main__":
    fix_suwalki_centroid()
