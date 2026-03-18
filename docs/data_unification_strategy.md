# Data Unification Strategy Report (2026)

## 1. Executive Summary
The project integrates real estate transaction data (RCN) from two distinct source types: WFS Services (Direct) and GML Packages (Manual). Current audits revealed significant structural divergence, preventing direct analysis. This report outlines the DNA of each source and the methodology for total unification.

## 2. Source DNA Analysis

### Type A: WFS Standard (e.g., Warszawa, GZM, Kraków)
- **Structure:** Denormalized (Flat).
- **Geometry:** Point (msGeometry) present in every record.
- **Attributes:** Standardized (tran_cena_brutto, dok_data, teryt).
- **Status:** READY for analysis.

### Type B: Relational GML - Point Based (e.g., Łódź, Giżycko)
- **Structure:** Relational (Normalized).
- **Links:** XLink (Transakcja -> Nieruchomość -> Lokal).
- **Geometry:** Point present in `RCN_Lokal` layer.
- **Date:** Linked via `RCN_Dokument`.
- **Challenge:** Requires 4-way join to reach WFS parity.

### Type C: Relational GML - Polygon Based (e.g., Suwałki)
- **Structure:** Relational (Normalized).
- **Geometry:** MISSING in `RCN_Lokal`. Present as Polygon in `RCN_Budynek`/`RCN_Dzialka`.
- **Challenge:** Requires Centroid extraction from parent polygons to generate analysis points.

## 3. Unification Schema (The Target "Standard")
All sources will be transformed into a single GeoPackage layer (`transactions`) with the following hardened schema:
- `tran_cena_brutto` (REAL): The primary numeric price.
- `dok_data` (DATETIME): Normalized ISO date.
- `teryt` (TEXT): 4 or 6 digit administrative code.
- `lok_pow_uzyt` (REAL): Usable area for price/m2 calculation.
- `geometry` (POINT): EPSG:2180 coordinate.

## 4. Implementation Pipeline: "The Great Stitching"
1. **Source Discovery:** Automatic detection of GML clusters in Hub directories.
2. **Relational Resolver:** A recursive Python engine following XLinks across 4 layers.
3. **Spatial Synthesis:** 
   - Direct Point copy for Type B.
   - Centroid calculation for Type C.
4. **Validation:** Post-processing VIT audit (Vicinity Integrity Test) to confirm 100% vicinity coverage.

## 5. Decision Request
We have the technology to bridge these gaps. **Łódź (12k records)** and **Giżycko (0.4k records)** are already partially unified in my previous test. **Suwałki** requires the Centroid logic.

**Do you approve this unification strategy? (Napisz "PROCEED").**
