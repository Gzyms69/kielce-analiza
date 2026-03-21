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

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", message=".*Geometry is in a geographic CRS.*")

def get_data_dir():
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

# --- KONFIGURACJA DNA v10.1 (REPAIRED) ---
H3_RESOLUTION = 9       
CATCHMENT_RADIUS = 500  
K_DECAY = 0.005         
DOMAIN_WEIGHT = 0.1     

DOMAIN_MAPPING = {
    'hospital_clinical': 'HEALTH', 'health_clinic': 'HEALTH', 'pharmacy': 'HEALTH',
    'university_campus': 'EDUCATION', 'education_high_school': 'EDUCATION', 
    'education_preschool': 'EDUCATION', 'student_dormitory': 'EDUCATION',
    'shopping_mall': 'COMMERCE', 'supermarket': 'COMMERCE', 'convenience_store': 'COMMERCE',
    'gastronomy': 'COMMERCE', 'personal_services': 'COMMERCE', 'marketplace': 'COMMERCE',
    'specialized_retail': 'COMMERCE', 'wholesale': 'COMMERCE',
    'national_stadium': 'LEISURE', 'exhibition_centre': 'LEISURE', 'park_recreation': 'LEISURE',
    'sports_centre': 'LEISURE', 'culture_theatre': 'LEISURE', 'hotel_accommodation': 'LEISURE',
    'micro_playground': 'LEISURE',
    'government_central': 'GOVERNMENT', 'police_station': 'GOVERNMENT', 
    'bank': 'GOVERNMENT', 'post_office': 'GOVERNMENT',
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
    try:
        cal_path = feed_path / "calendar.txt"
        cd_path = feed_path / "calendar_dates.txt"
        if cal_path.exists():
            cal = pd.read_csv(cal_path)
            if 'wednesday' in cal.columns:
                active = cal[cal['wednesday'] == 1]['service_id'].tolist()
                if active: return active
        if cd_path.exists():
            cd = pd.read_csv(cd_path)
            best_day = cd['date'].value_counts().idxmax()
            return cd[cd['date'] == best_day]['service_id'].tolist()
        return []
    except: return []

def _build_h3_hex_polygons(h3_indices, crs="EPSG:2180"):
    from shapely.geometry import Polygon
    hexes = []
    for idx in h3_indices:
        boundary = h3.cell_to_boundary(idx)
        ring = [(lng, lat) for lat, lng in boundary]
        ring.append(ring[0])
        hexes.append({"h3_index": idx, "geometry": Polygon(ring)})
    gdf = gpd.GeoDataFrame(hexes, crs="EPSG:4326").to_crs(crs)
    return gdf

def _extract_category(row):
    for col in ['amenity', 'shop', 'office', 'landuse', 'leisure', 'aeroway', 'railway']:
        val = row.get(col)
        if pd.notna(val) and val: return str(val)
    return None

def calculate_h3_dna(city_name):
    print(f"[{city_name}] Obliczanie DNA v10.1 (Naprawiona geometria i statystyka)...", flush=True)
    try:
        data_dir = get_data_dir()
        city_dir = data_dir / "cities" / city_name
        spatial_dir = city_dir / "02_spatial"
        results_dir = city_dir / "04_results"
        results_dir.mkdir(parents=True, exist_ok=True)

        stops_path = spatial_dir / "stops.gpkg"
        if not stops_path.exists(): return

        stops = gpd.read_file(stops_path).to_crs("EPSG:2180")
        stops['h3_index'] = stops.to_crs("EPSG:4326").geometry.apply(lambda p: h3.latlng_to_cell(p.y, p.x, H3_RESOLUTION))
        
        unique_h3 = stops['h3_index'].unique()
        h3_hubs = _build_h3_hex_polygons(unique_h3, crs="EPSG:2180")
        rep_stops = stops.groupby('h3_index').agg(stop_name=('stop_name', 'first')).reset_index()
        h3_hubs = h3_hubs.merge(rep_stops, on='h3_index', how='left')
        h3_hubs['hex_centroid'] = h3_hubs.geometry.centroid
        
        # RCN — PRZYWRÓCONY FILTR IQR (Likwidacja anomalii cenowych)
        rcn = gpd.read_file(spatial_dir / "transactions.gpkg").to_crs("EPSG:2180")
        if not rcn.empty and 'price_m2' in rcn.columns:
            prices = rcn['price_m2'].dropna()
            if not prices.empty:
                q1, q3 = prices.quantile(0.25), prices.quantile(0.75)
                iqr = q3 - q1
                rcn = rcn[(rcn['price_m2'] >= (q1 - 1.5*iqr)) & (rcn['price_m2'] <= (q3 + 1.5*iqr))]
        
        infra_pts = gpd.read_file(spatial_dir / "infrastructure.gpkg", layer="points").to_crs("EPSG:2180")
        infra_poly = gpd.read_file(spatial_dir / "infrastructure.gpkg", layer="multipolygons").to_crs("EPSG:2180")
        infra_poly['geometry'] = infra_poly.centroid
        infra = pd.concat([infra_pts, infra_poly], ignore_index=True)
        
        with open(city_dir / "03_config" / "poi_valuation.json", "r") as f:
            poi_weights = json.load(f)

        # TRANSIT FREQ
        freq_results = {}
        for feed in (city_dir / "gtfs").iterdir():
            if not feed.is_dir(): continue
            try:
                service_ids = get_best_service_ids(feed)
                st, tr = pd.read_csv(feed / "stop_times.txt"), pd.read_csv(feed / "trips.txt")
                if service_ids: tr = tr[tr['service_id'].isin(service_ids)]
                st = st.merge(tr[['trip_id', 'route_id']], on='trip_id')
                st['secs'] = st['departure_time'].apply(parse_gtfs_time_safe)
                st = st[(st['secs'] >= 21600) & (st['secs'] <= 72000)]
                counts = st.groupby('stop_id').size() / 14.0
                for sid, val in counts.items(): freq_results[str(sid)] = freq_results.get(str(sid), 0) + val
            except: continue

        stops['hourly_freq'] = stops['stop_id'].apply(lambda x: freq_results.get(str(x), 0))
        freq_per_h3 = stops.groupby('h3_index')['hourly_freq'].sum().reset_index()
        h3_hubs = h3_hubs.merge(freq_per_h3.rename(columns={'hourly_freq': 'transit_freq'}), on='h3_index', how='left')
        h3_hubs['transit_freq'] = h3_hubs['transit_freq'].fillna(0)

        # INFRA SPATIAL JOIN — POWRÓT DO INTERSECTS (Dla dużych poligonów lotnisk/galerii)
        joined_infra = gpd.sjoin(infra, h3_hubs[['h3_index', 'geometry']], how="inner", predicate="intersects")
        joined_infra['category'] = joined_infra.apply(_extract_category, axis=1)
        joined_infra['domain'] = joined_infra['category'].map(DOMAIN_MAPPING)
        domain_stats = joined_infra.groupby('h3_index')['domain'].nunique().reset_index().rename(columns={'domain': 'domain_count'})
        
        joined_infra = joined_infra.merge(h3_hubs[['h3_index', 'hex_centroid']], on='h3_index', how='left')
        joined_infra['dist'] = joined_infra.apply(lambda r: r['geometry'].distance(r['hex_centroid']), axis=1)
        joined_infra['w'] = joined_infra['category'].apply(lambda c: poi_weights.get(c, {}).get('final_value', 10.0))
        joined_infra['grav'] = joined_infra['w'] * np.exp(-K_DECAY * joined_infra['dist'])
        
        gravity_stats = joined_infra.groupby('h3_index')['grav'].sum().reset_index().rename(columns={'grav': 'raw_gravity'})
        h3_hubs = h3_hubs.merge(gravity_stats, on='h3_index', how='left').merge(domain_stats, on='h3_index', how='left')
        h3_hubs['raw_gravity'] = h3_hubs['raw_gravity'].fillna(0)
        h3_hubs['domain_count'] = h3_hubs['domain_count'].fillna(0)
        h3_hubs['infra_score'] = h3_hubs['raw_gravity'] * (1 + DOMAIN_WEIGHT * h3_hubs['domain_count'])

        # RCN JOIN
        if not rcn.empty and 'price_m2' in rcn.columns:
            joined_rcn = gpd.sjoin(rcn, h3_hubs[['h3_index', 'geometry']], how="inner", predicate="intersects")
            rcn_stats = joined_rcn.groupby('h3_index')['price_m2'].agg(market_val='median', liquidity='count').reset_index()
            h3_hubs = h3_hubs.merge(rcn_stats, on='h3_index', how='left')
            h3_hubs['market_val'] = h3_hubs['market_val'].fillna(rcn['price_m2'].median())
        else:
            h3_hubs['market_val'], h3_hubs['liquidity'] = 0, 0
        h3_hubs['liquidity'] = h3_hubs['liquidity'].fillna(0)

        # POPULATION
        pop_path = spatial_dir / "population_250m.gpkg"
        if pop_path.exists():
            pop = gpd.read_file(pop_path).to_crs("EPSG:2180")
            if not pop.empty and 'TOT' in pop.columns:
                pop['pop_centroid'] = pop.geometry.centroid
                pop_joined = gpd.sjoin(pop.set_geometry('pop_centroid'), h3_hubs[['h3_index', 'geometry']], how="inner", predicate="within")
                pop_h3 = pop_joined.groupby('h3_index')['TOT'].sum().reset_index().rename(columns={'TOT': 'pop_val'})
                h3_hubs = h3_hubs.merge(pop_h3, on='h3_index', how='left')
        h3_hubs['pop_val'] = h3_hubs['pop_val'].fillna(0)

        # SCORING (Z-SCORE)
        for c in ['infra_score', 'transit_freq', 'pop_val']: h3_hubs[f'{c}_log'] = np.log1p(h3_hubs[c])
        def z_score(s): return (s - s.mean()) / (s.std() + 1e-9)
        h3_hubs['local_score_raw'] = (z_score(h3_hubs['infra_score_log']) * 0.35 + z_score(h3_hubs['transit_freq_log']) * 0.35 +
                                      z_score(h3_hubs['pop_val_log']) * 0.15 + z_score(h3_hubs['market_val']) * 0.15)
        h3_hubs['local_percentile'] = h3_hubs['local_score_raw'].rank(pct=True) * 100
        
        def assign_grade(pct):
            if pct >= 95: return "A+"
            if pct >= 85: return "A"
            if pct >= 70: return "B"
            if pct >= 50: return "C"
            if pct >= 25: return "D"
            return "F"
        h3_hubs['grade'] = h3_hubs['local_percentile'].apply(assign_grade)
        
        # FINAL STITCHING & DE-DUPLICATION (Grupowanie po nazwie przystanku)
        export_cols = [c for c in h3_hubs.columns if c != 'hex_centroid']
        final_stops = stops.merge(h3_hubs[export_cols].drop(columns=['geometry', 'stop_name']), on='h3_index', how='left')
        
        if 'norm_name' in final_stops.columns:
            # Likwidacja duplikatów: bierzemy rekord o najwyższym wyniku DNA dla danej nazwy w mieście
            final_stops = final_stops.sort_values('local_score_raw', ascending=False).drop_duplicates('norm_name')
        
        final_stops.to_file(results_dir / "stop_dna.gpkg", driver="GPKG")
        return final_stops
    except Exception as e:
        print(f"[{city_name}] CRITICAL DNA ERROR: {str(e)}", file=sys.stderr); raise

def run_national_stitching():
    data_dir = get_data_dir()
    all_dfs = []
    for city_dir in (data_dir / "cities").iterdir():
        p = city_dir / "04_results" / "stop_dna.gpkg"
        if p.exists(): all_dfs.append(gpd.read_file(p))
    if not all_dfs: return
    full_df = pd.concat(all_dfs, ignore_index=True)
    for c in ['infra_score', 'transit_freq', 'pop_val']: full_df[f'{c}_log_nat'] = np.log1p(full_df[c])
    full_df['national_score'] = (((full_df['infra_score_log_nat'] - full_df['infra_score_log_nat'].mean()) / full_df['infra_score_log_nat'].std()) * 0.35 +
                                 ((full_df['transit_freq_log_nat'] - full_df['transit_freq_log_nat'].mean()) / full_df['transit_freq_log_nat'].std()) * 0.35 +
                                 ((full_df['pop_val_log_nat'] - full_df['pop_val_log_nat'].mean()) / full_df['pop_val_log_nat'].std()) * 0.15 +
                                 ((full_df['market_val'] - full_df['market_val'].mean()) / full_df['market_val'].std()) * 0.15)
    full_df['national_percentile'] = full_df['national_score'].rank(pct=True) * 100
    full_df.to_file(data_dir / "database" / "master_stop_dna_poland.gpkg", driver="GPKG")
    full_df.drop(columns='geometry').to_csv(data_dir / "database" / "master_stop_dna_poland.csv", index=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city"); parser.add_argument("--force", action="store_true"); parser.add_argument("--stitch", action="store_true")
    args = parser.parse_args()
    if args.city: calculate_h3_dna(args.city)
    if args.stitch: run_national_stitching()

if __name__ == "__main__":
    main()
