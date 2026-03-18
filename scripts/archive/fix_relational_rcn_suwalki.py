import geopandas as gpd
import pandas as pd
from lxml import etree
from pathlib import Path
import os

def clean_ref(ref):
    if not ref: return None
    return ref.split('/')[-1].replace('#', '')

def fix_city_rcn(city_name):
    print(f"--- DIAGNOSTIC JOIN (v4): {city_name.upper()} ---")
    city_dir = Path(f"data/cities/{city_name}/rcn")
    gml_files = list(city_dir.glob("*.gml"))
    
    ns = {
        'rcn': 'urn:gugik:specyfikacje:gmlas:rejestrcennieruchomosci:1.0',
        'gml': 'http://www.opengis.net/gml/3.2',
        'xlink': 'http://www.w3.org/1999/xlink'
    }

    all_features = []
    for gml_path in gml_files:
        print(f"  Parsing {gml_path.name}...")
        try:
            # Używamy iterparse dla ogromnych plików
            context = etree.iterparse(str(gml_path), events=('end',), tag=['{urn:gugik:specyfikacje:gmlas:rejestrcennieruchomosci:1.0}RCN_Dokument', 
                                                                         '{urn:gugik:specyfikacje:gmlas:rejestrcennieruchomosci:1.0}RCN_Lokal', 
                                                                         '{urn:gugik:specyfikacje:gmlas:rejestrcennieruchomosci:1.0}RCN_Nieruchomosc', 
                                                                         '{urn:gugik:specyfikacje:gmlas:rejestrcennieruchomosci:1.0}RCN_Transakcja'])
            
            docs, lokale, niers, trans = {}, {}, {}, []
            
            for event, elem in context:
                gml_id = elem.get('{http://www.opengis.net/gml/3.2}id')
                tag = elem.tag.split('}')[-1]
                
                if tag == 'RCN_Dokument':
                    d = elem.xpath('./rcn:dataSporzadzeniaDokumentu/text()', namespaces=ns)
                    if d: docs[gml_id] = d[0]
                elif tag == 'RCN_Lokal':
                    p = elem.xpath('.//gml:pos/text()', namespaces=ns)
                    if p:
                        c = [float(x) for x in p[0].split()]
                        if len(c) == 2: lokale[gml_id] = (c[1], c[0])
                elif tag == 'RCN_Nieruchomosc':
                    l_ref = elem.xpath('./rcn:lokal/@xlink:href', namespaces=ns)
                    if l_ref: niers[gml_id] = clean_ref(l_ref[0])
                elif tag == 'RCN_Transakcja':
                    c = elem.xpath('./rcn:cenaTransakcjiBrutto/text()', namespaces=ns)
                    d_ref = elem.xpath('./rcn:podstawaPrawna/@xlink:href', namespaces=ns)
                    n_ref = elem.xpath('./rcn:nieruchomosc/@xlink:href', namespaces=ns)
                    trans.append({
                        'cena': float(c[0]) if c else 0,
                        'd_id': clean_ref(d_ref[0]) if d_ref else None,
                        'n_id': clean_ref(n_ref[0]) if n_ref else None
                    })
                elem.clear()
            
            print(f"    Found: Docs={len(docs)}, Lokale={len(lokale)}, Niers={len(niers)}, Trans={len(trans)}")
            
            # Joining
            for t in trans:
                if t['n_id'] in niers:
                    l_id = niers[t['n_id']]
                    if l_id in lokale:
                        all_features.append({
                            'tran_cena_brutto': t['cena'],
                            'dok_data': docs.get(t['d_id']),
                            'lon': lokale[l_id][0],
                            'lat': lokale[l_id][1]
                        })
        except Exception as e:
            print(f"    Error: {e}")

    if all_features:
        df = pd.DataFrame(all_features)
        print(f"    Total joined features: {len(df)}")
        df['dok_data'] = pd.to_datetime(df['dok_data'], errors='coerce')
        df_2025 = df[df['dok_data'] >= '2025-01-01']
        print(f"    Features from 2025+: {len(df_2025)}")
        
        if not df_2025.empty:
            gdf = gpd.GeoDataFrame(df_2025, geometry=gpd.points_from_xy(df_2025.lon, df_2025.lat), crs="EPSG:2180")
            gdf.to_file(city_dir / "transactions.gpkg", driver="GPKG", layer="transactions")
            print(f"    SUCCESS: Saved {len(df_2025)} records.")

if __name__ == "__main__":
    fix_city_rcn("suwalki")
