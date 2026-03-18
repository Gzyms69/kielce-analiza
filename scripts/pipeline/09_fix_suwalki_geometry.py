import geopandas as gpd
import pandas as pd
from lxml import etree
from pathlib import Path
import os

def clean_ref(ref):
    if not ref: return None
    return ref.split('/')[-1].replace('#', '')

def fix_suwalki_centroid():
    print("--- FIXING SUWAŁKI: CENTROID & M2 MAPPING ---")
    city_dir = Path("data/cities/suwalki/rcn")
    gml_path = city_dir / "rcn_2063.gml"
    
    if not gml_path.exists(): return

    ns = {
        'rcn': 'urn:gugik:specyfikacje:gmlas:rejestrcennieruchomosci:1.0',
        'gml': 'http://www.opengis.net/gml/3.2',
        'xlink': 'http://www.w3.org/1999/xlink'
    }

    try:
        buildings = gpd.read_file(str(gml_path), layer="RCN_Budynek")
        plots = gpd.read_file(str(gml_path), layer="RCN_Dzialka")
        geo_map = {row['gml_id']: row.geometry.centroid for _, row in buildings.iterrows() if row.geometry}
        for _, row in plots.iterrows():
            if row.geometry and row['gml_id'] not in geo_map:
                geo_map[row['gml_id']] = row.geometry.centroid
    except: return

    tree = etree.parse(str(gml_path))
    root = tree.getroot()

    docs = {doc.get('{http://www.opengis.net/gml/3.2}id'): doc.xpath('./rcn:dataSporzadzeniaDokumentu/text()', namespaces=ns)[0] 
            for doc in root.xpath('//rcn:RCN_Dokument', namespaces=ns) if doc.xpath('./rcn:dataSporzadzeniaDokumentu/text()', namespaces=ns)}

    # Map Lokale with M2
    lokale_m2 = {}
    for lok in root.xpath('//rcn:RCN_Lokal', namespaces=ns):
        l_id = lok.get('{http://www.opengis.net/gml/3.2}id')
        m2 = lok.xpath('./rcn:powUzytkowaLokalu/text()', namespaces=ns)
        lokale_m2[l_id] = float(m2[0]) if m2 else None

    # Map Nieruchomosci to Lokale and Parents
    niers = {}
    for nier in root.xpath('//rcn:RCN_Nieruchomosc', namespaces=ns):
        n_id = nier.get('{http://www.opengis.net/gml/3.2}id')
        l_ref = clean_ref(nier.xpath('./rcn:lokal/@xlink:href', namespaces=ns)[0]) if nier.xpath('./rcn:lokal/@xlink:href', namespaces=ns) else None
        parents = [clean_ref(p) for p in nier.xpath('./rcn:budynek/@xlink:href', namespaces=ns) + nier.xpath('./rcn:dzialka/@xlink:href', namespaces=ns)]
        niers[n_id] = {'l_ref': l_ref, 'parents': parents}

    all_features = []
    for trans in root.xpath('//rcn:RCN_Transakcja', namespaces=ns):
        price = trans.xpath('./rcn:cenaTransakcjiBrutto/text()', namespaces=ns)
        d_ref = trans.xpath('./rcn:podstawaPrawna/@xlink:href', namespaces=ns)
        n_refs = trans.xpath('./rcn:nieruchomosc/@xlink:href', namespaces=ns)
        final_date = docs.get(clean_ref(d_ref[0])) if d_ref else None
        
        for nr in n_refs:
            n_id = clean_ref(nr)
            if n_id in niers:
                l_id = niers[n_id]['l_ref']
                m2_val = lokale_m2.get(l_id) if l_id else None
                for p_id in niers[n_id]['parents']:
                    if p_id in geo_map:
                        all_features.append({
                            'tran_cena_brutto': float(price[0]) if price else 0,
                            'dok_data': final_date,
                            'geometry': geo_map[p_id],
                            'lok_pow_uzyt': m2_val
                        })
                        break

    if all_features:
        gdf = gpd.GeoDataFrame(all_features, crs=buildings.crs)
        gdf['dok_data'] = pd.to_datetime(gdf['dok_data'], errors='coerce')
        gdf = gdf[gdf['dok_data'] >= '2025-01-01']
        gdf.to_file(city_dir / "transactions.gpkg", driver="GPKG", layer="transactions")
        print(f"  SUCCESS: Saved {len(gdf)} records with m2 data for Suwałki.")

if __name__ == "__main__":
    fix_suwalki_centroid()
