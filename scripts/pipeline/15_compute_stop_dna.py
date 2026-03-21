import geopandas as gpd
import pandas as pd
import numpy as np
import os
import json
import math
from pathlib import Path
import argparse
import sys
import warnings
import h3

warnings.filterwarnings("ignore")

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

# --- KONFIGURACJA DNA v9.0 (ROBUST & VECTORIZED) ---
H3_RESOLUTION = 9       # Ok. 170m szerokości hexa
CATCHMENT_RADIUS = 500  # Zasięg pieszego dla atrybutów (m)
K_DECAY = 0.005         # Spadek wykładniczy
DOMAIN_WEIGHT = 0.1     # Mnożnik synergii domen

DOMAIN_MAPPING = {
    # HEALTH
    'hospital_clinical': 'HEALTH', 'health_clinic': 'HEALTH', 'pharmacy': 'HEALTH',
    # EDUCATION
    'university_campus': 'EDUCATION', 'education_high_school': 'EDUCATION', 
    'education_preschool': 'EDUCATION', 'student_dormitory': 'EDUCATION',
    # COMMERCE
    'shopping_mall': 'COMMERCE', 'supermarket': 'COMMERCE', 'convenience_store': 'COMMERCE',
    'gastronomy': 'COMMERCE', 'personal_services': 'COMMERCE', 'marketplace': 'COMMERCE',
    'specialized_retail': 'COMMERCE', 'wholesale': 'COMMERCE',
    # LEISURE
    'national_stadium': 'LEISURE', 'exhibition_centre': 'LEISURE', 'park_recreation': 'LEISURE',
    'sports_centre': 'LEISURE', 'culture_theatre': 'LEISURE', 'hotel_accommodation': 'LEISURE',
    'micro_playground': 'LEISURE',
    # GOVERNMENT & FINANCE
    'government_central': 'GOVERNMENT', 'police_station': 'GOVERNMENT', 
    'bank': 'GOVERNMENT', 'post_office': 'GOVERNMENT',
    # TRANSPORT (Zawsze strategiczne)
    'international_airport': 'TRANSPORT', 'national_rail_hub': 'TRANSPORT',
    'regional_rail_hub': 'TRANSPORT', 'airport_terminal': 'TRANSPORT'
}

def parse_gtfs_time_safe(time_str):
    try:
        if not time_str or not isinstance(time_str, str): return 0
        parts = time_str.strip().split(':')
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    except: return 0

def get_best_service_ids(feed_path):
    """KULUOODPORNY KALENDARZ: Wybiera najlepsze service_id (Środa lub Top 5 dni)"""
    try:
        cal_path = feed_path / "calendar.txt"
        cd_path = feed_path / "calendar_dates.txt"
        
        # 1. Próba calendar.txt (Szukamy środy - 'wednesday' == 1)
        if cal_path.exists():
            cal = pd.read_csv(cal_path)
            if 'wednesday' in cal.columns:
                active = cal[cal['wednesday'] == 1]['service_id'].tolist()
                if active: return active
        
        # 2. Próba calendar_dates.txt (Heurystyka: Najbardziej zajęty dzień)
        if cd_path.exists():
            cd = pd.read_csv(cd_path)
            # Liczymy wystąpienia service_id na przestrzeni dat
            best_day = cd['date'].value_counts().idxmax()
            return cd[cd['date'] == best_day]['service_id'].tolist()
            
        return [] # Brak kalendarza
    except:
        return []

def calculate_h3_dna(city_name):
    print(f"[{city_name}] START: Computing DNA v9.0 (H3 + Vectorized)...", flush=True)
    try:
        data_dir = get_data_dir()
        city_dir = data_dir / "cities" / city_name
        spatial_dir = city_dir / "02_spatial"
        results_dir = city_dir / "04_results"
        results_dir.mkdir(parents=True, exist_ok=True)

        # 1. INGESTION & IQR FILTERING
        stops = gpd.read_file(spatial_dir / "stops.gpkg").to_crs("EPSG:2180")
        stops['h3_index'] = stops.to_crs("EPSG:4326").geometry.apply(lambda p: h3.latlng_to_cell(p.y, p.x, H3_RESOLUTION))
        
        # Agregacja przystanków do H3 Hubs
        h3_hubs = stops.dissolve(by='h3_index', aggfunc={'stop_name': 'first'}).reset_index()
        
        # RCN IQR FILTER
        rcn = gpd.read_file(spatial_dir / "transactions.gpkg").to_crs("EPSG:2180")
        if not rcn.empty:
            q1 = rcn['price_m2'].quantile(0.25)
            q3 = rcn['price_m2'].quantile(0.75)
            iqr = q3 - q1
            rcn = rcn[(rcn['price_m2'] >= (q1 - 1.5*iqr)) & (rcn['price_m2'] <= (q3 + 1.5*iqr))]
        
        infra_pts = gpd.read_file(spatial_dir / "infrastructure.gpkg", layer="points").to_crs("EPSG:2180")
        infra_poly = gpd.read_file(spatial_dir / "infrastructure.gpkg", layer="multipolygons").to_crs("EPSG:2180")
        infra_poly['geometry'] = infra_poly.centroid
        infra = pd.concat([infra_pts, infra_poly], ignore_index=True)
        
        with open(city_dir / "03_config" / "poi_valuation.json", "r") as f:
            poi_weights = json.load(f)

        # 2. TRANSIT FREQUENCY (Calendar-Aware)
        freq_results = {}
        for feed in (city_dir / "gtfs").iterdir():
            if not feed.is_dir(): continue
            try:
                service_ids = get_best_service_ids(feed)
                st = pd.read_csv(feed / "stop_times.txt")
                tr = pd.read_csv(feed / "trips.txt")
                
                # Tylko kursy aktywne w naszym dniu referencyjnym
                if service_ids:
                    tr = tr[tr['service_id'].isin(service_ids)]
                
                st = st.merge(tr[['trip_id', 'route_id']], on='trip_id')
                st['secs'] = st['departure_time'].apply(parse_gtfs_time_safe)
                st = st[(st['secs'] >= 21600) & (st['secs'] <= 72000)] # 06:00 - 20:00
                
                counts = st.groupby('stop_id').size() / 14.0
                for sid, val in counts.items():
                    freq_results[str(sid)] = freq_results.get(str(sid), 0) + val
            except: continue

        # Mapujemy freq na H3 Index
        stops['hourly_freq'] = stops['stop_id'].apply(lambda x: freq_results.get(str(x), 0))
        h3_hubs['transit_freq'] = stops.groupby('h3_index')['hourly_freq'].sum().reindex(h3_hubs['h3_index']).values

        # 3. VECTORIZED SPATIAL JOINS
        # INFRA
        joined_infra = gpd.sjoin(infra, h3_hubs, how="inner", predicate="intersects")
        # Mapowanie na domeny
        joined_infra['category'] = joined_infra.get('amenity') or joined_infra.get('shop') or joined_infra.get('office') or joined_infra.get('landuse')
        joined_infra['domain'] = joined_infra['category'].map(DOMAIN_MAPPING)
        
        infra_stats = joined_infra.groupby('h3_index').agg(
            raw_gravity=('h3_index', lambda x: 0), # Placeholder
            domain_count=('domain', 'nunique')
        )
        
        # Ponieważ potrzebujemy dystansu, musimy niestety użyć apply na grupach (ale to nadal szybkie)
        def calc_group_gravity(group):
            h3_idx = group.name
            hub_geom = h3_hubs[h3_hubs['h3_index'] == h3_idx].geometry.iloc[0]
            score = 0
            for _, p in group.iterrows():
                tag = p.get('amenity') or p.get('shop') or p.get('office') or p.get('landuse')
                w = poi_weights.get(tag, {"final_value": 10.0})['final_value']
                dist = hub_geom.distance(p.geometry)
                score += w * math.exp(-K_DECAY * dist)
            return score

        infra_stats['raw_gravity'] = joined_infra.groupby('h3_index').apply(calc_group_gravity)
        h3_hubs = h3_hubs.merge(infra_stats, on='h3_index', how='left').fillna(0)
        h3_hubs['infra_score'] = h3_hubs['raw_gravity'] * (1 + DOMAIN_WEIGHT * h3_hubs['domain_count'])

        # RCN
        joined_rcn = gpd.sjoin(rcn, h3_hubs, how="inner", predicate="intersects")
        rcn_stats = joined_rcn.groupby('h3_index')['price_m2'].agg(
            market_val='median', liquidity='count'
        ).reset_index()
        h3_hubs = h3_hubs.merge(rcn_stats, on='h3_index', how='left')
        h3_hubs['market_val'] = h3_hubs['market_val'].fillna(rcn['price_m2'].median() if not rcn.empty else 0)
        h3_hubs['liquidity'] = h3_hubs['liquidity'].fillna(0)

        # POPULATION (Areal Interpolation)
        pop = gpd.read_file(spatial_dir / "population_250m.gpkg").to_crs("EPSG:2180")
        pop['cell_area'] = pop.geometry.area
        pop_inter = gpd.overlay(pop, h3_hubs, how="intersection")
        pop_inter['adj_pop'] = pop_inter['TOT'] * (pop_inter.geometry.area / pop_inter['cell_area'])
        pop_h3 = pop_inter.groupby('h3_index')['adj_pop'].sum().reset_index().rename(columns={'adj_pop': 'pop_val'})
        h3_hubs = h3_hubs.merge(pop_h3, on='h3_index', how='left').fillna(0)

        # 4. ROBUST SCORING (Z-SCORE)
        # Transformacja logarytmiczna
        for c in ['infra_score', 'transit_freq', 'pop_val']:
            h3_hubs[f'{c}_log'] = np.log1p(h3_hubs[c])
        
        # Standardyzacja (Z-Score)
        def z_score(series):
            return (series - series.mean()) / (series.std() + 1e-9)

        h3_hubs['local_score_raw'] = (
            z_score(h3_hubs['infra_score_log']) * 0.35 +
            z_score(h3_hubs['transit_freq_log']) * 0.35 +
            z_score(h3_hubs['pop_val_log']) * 0.15 +
            z_score(h3_hubs['market_val']) * 0.15
        )
        
        h3_hubs['local_percentile'] = h3_hubs['local_score_raw'].rank(pct=True) * 100
        
        def assign_grade(pct):
            if pct >= 95: return "A+"
            if pct >= 85: return "A"
            if pct >= 70: return "B"
            if pct >= 50: return "C"
            if pct >= 25: return "D"
            return "F"

        h3_hubs['grade'] = h3_hubs['local_percentile'].apply(assign_grade)
        
        # Finalne mapowanie H3 -> Przystanki
        final_stops = stops.merge(h3_hubs.drop(columns=['geometry', 'stop_name']), on='h3_index', how='left')
        final_stops.to_file(results_dir / "stop_dna.gpkg", driver="GPKG")
        
        print(f"__PIPELINE_METRICS__={json.dumps({'city': city_name, 'h3_hubs': len(h3_hubs), 'stops': len(final_stops)})}")
        return final_stops

    except Exception as e:
        print(f"[{city_name}] CRITICAL DNA v9.0 ERROR: {str(e)}", file=sys.stderr)
        raise

def run_national_stitching():
    print("\n=== STAGE 3: National DNA Stitching & Robust Scaling (v9.0) ===", flush=True)
    data_dir = get_data_dir()
    all_dfs = []
    for city_dir in (data_dir / "cities").iterdir():
        p = city_dir / "04_results" / "stop_dna.gpkg"
        if p.exists(): all_dfs.append(gpd.read_file(p))
    
    if not all_dfs: return
    full_df = pd.concat(all_dfs, ignore_index=True)
    
    # Globalne log-scaling i z-score
    for c in ['infra_score', 'transit_freq', 'pop_val']:
        full_df[f'{c}_log_nat'] = np.log1p(full_df[c])
    
    full_df['national_score'] = (
        ((full_df['infra_score_log_nat'] - full_df['infra_score_log_nat'].mean()) / full_df['infra_score_log_nat'].std()) * 0.35 +
        ((full_df['transit_freq_log_nat'] - full_df['transit_freq_log_nat'].mean()) / full_df['transit_freq_log_nat'].std()) * 0.35 +
        ((full_df['pop_val_log_nat'] - full_df['pop_val_log_nat'].mean()) / full_df['pop_val_log_nat'].std()) * 0.15 +
        ((full_df['market_val'] - full_df['market_val'].mean()) / full_df['market_val'].std()) * 0.15
    )
    
    full_df['national_percentile'] = full_df['national_score'].rank(pct=True) * 100
    
    full_df.to_file(data_dir / "database" / "master_stop_dna_poland.gpkg", driver="GPKG")
    full_df.drop(columns='geometry').to_csv(data_dir / "database" / "master_stop_dna_poland.csv", index=False)
    print(f"SUCCESS: Master DNA created with {len(full_df)} stops.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--stitch", action="store_true")
    args = parser.parse_args()
    if args.city: calculate_h3_dna(args.city)
    if args.stitch: run_national_stitching()

if __name__ == "__main__":
    main()
