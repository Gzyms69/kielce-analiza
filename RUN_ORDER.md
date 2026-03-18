# Pipeline Execution Guide: National Transit & Wealth Platform (2026)

This document defines the strict execution order for rebuilding the entire Polish analytical dataset. All scripts must be run from the project root using the virtual environment.

## Execution Order (Pipeline)

### Phase 1: Transit & Geography
1. `python3 scripts/pipeline/01_fetch_gtfs.py`  
   Downloads nationwide GTFS packages for 70+ operators.
2. `python3 scripts/pipeline/02_collect_stops.py`  
   Extracts unique transit nodes and calculates agglomeration hubs.
3. `python3 scripts/pipeline/03_download_osm_pbf.py`  
   Downloads the latest 2GB OpenStreetMap file for Poland.
4. `python3 scripts/pipeline/04_download_population.py`  
   Downloads and extracts the NSP 2021 (GUS) population grid.

### Phase 2: Infrastructure & Real Estate
5. `python3 scripts/pipeline/05_extract_infrastructure.py`  
   Uses `osmium` and `ogr2ogr` to clip OSM buildings/POI to transit zones.
6. `python3 scripts/pipeline/06_identify_rcn_teryt.py`  
   Maps transit zones to Polish administrative TERYT codes.
7. `python3 scripts/pipeline/07_harvest_rcn.py`  
   Fetches 2025-2026 real estate transactions from GUGiK WFS servers.

### Phase 3: Data Hardening & Unification
8. `python3 scripts/pipeline/08_fix_relational_data.py`  
   Repairs relational GML files for Łódź and Giżycko (CRS correction & Axes fix).
9. `python3 scripts/pipeline/09_fix_suwalki_geometry.py`  
   Calculates centroids for Suwałki building-based transactions.
10. `python3 scripts/pipeline/10_unify_schemas.py`  
    Forces identical schemas and calculates `price_m2` across all 29 hubs.
11. `python3 scripts/pipeline/11_build_master_db.py`  
    Consolidates everything into `data/database/master_analytical.gpkg`.

## Quality Control Tools
- **Audit Data**: `python3 scripts/tools/audit_data_quality.py`  
  Generates a full report on CRS and coverage.
- **Generate Samples**: `python3 scripts/tools/generate_atlas_samples.py`  
  Shows the nearest transactions and population for 5 stops per city.

---
**Standard: EPSG:2180 (Poland 1992) | No Emojis | Strict Logging**
