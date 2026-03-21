import geopandas as gpd
import pandas as pd
import numpy as np
import json
from pathlib import Path
import os
from datetime import datetime
import warnings

warnings.filterwarnings("ignore")

# Baseline ludności dla weryfikacji rzędu wielkości (rdzeń miasta)
CITY_BASELINES = {
    "warszawa": 1800000, "krakow": 800000, "lodz": 670000, "wroclaw": 640000,
    "poznan": 530000, "szczecin": 400000, "bydgoszcz": 340000, "lublin": 330000,
    "bialystok": 290000, "katowice": 290000, "gzm": 2300000, # GZM to cała metropolia
    "rzeszow": 190000, "kielce": 190000, "olsztyn": 170000, "radom": 200000,
    "torun": 190000, "czestochowa": 210000, "legnica": 90000,
    "elblag": 110000, "opole": 120000, "gorzow": 120000, "suwalki": 70000,
    "elk": 60000, "lomza": 60000, "przemysl": 60000, "gizycko": 30000, "swinoujscie": 40000
}

def run_master_audit():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    report_path = Path(f"reports/FULL_AUDIT_{timestamp}.txt")
    data_dir = Path("data")
    cities_root = data_dir / "cities"
    cities = sorted([d.name for d in cities_root.iterdir() if d.is_dir() and d.name != 'rail'])
    
    output = []
    output.append("="*110)
    output.append(f"   MASTER NATIONAL DATA AUDIT (v9.0) - SOURCE OF TRUTH")
    output.append(f"   Generated: {timestamp}")
    output.append("="*110 + "\n")

    global_stats = {"total_stops": 0, "total_rcn": 0, "total_pop": 0}

    for city in cities:
        city_header = f"\n>>> AGLOMERACJA: {city.upper()}"
        output.append(city_header)
        output.append("-" * 110)
        
        city_dir = cities_root / city
        spatial = city_dir / "02_spatial"
        results = city_dir / "04_results"
        
        # 1. RCN INTEGRITY (Historical Coverage & IQR)
        rcn_path = spatial / "transactions.gpkg"
        if rcn_path.exists():
            try:
                rcn = gpd.read_file(rcn_path)
                rcn['rok'] = pd.to_datetime(rcn['data_transakcji'], errors='coerce').dt.year
                year_dist = rcn['rok'].value_counts().sort_index().to_dict()
                
                prices = rcn['price_m2'].dropna()
                q1, q3 = prices.quantile(0.25), prices.quantile(0.75)
                iqr = q3 - q1
                
                output.append(f"[RCN] Liczba: {len(rcn):,.0f} | Rozkład lat: {year_dist}")
                output.append(f"[RCN] Ceny: Mediana={prices.median():,.0f} | IQR=[{q1:,.0f} - {q3:,.0f}] | CRS: {rcn.crs}")
                global_stats["total_rcn"] += len(rcn)
            except Exception as e:
                output.append(f"[RCN] BŁĄD: {e}")
        
        # 2. POPULATION COVERAGE
        pop_path = spatial / "population_250m.gpkg"
        if pop_path.exists():
            try:
                pop = gpd.read_file(pop_path)
                pop_total = int(pop['TOT'].sum())
                baseline = CITY_BASELINES.get(city.lower(), 50000)
                status = "OK" if pop_total >= baseline * 0.8 else "SUSPICIOUSLY LOW"
                output.append(f"[POP] Całkowita (strefa): {pop_total:,.0f} | Baseline: {baseline:,.0f} | Status: {status}")
                global_stats["total_pop"] += pop_total
            except Exception as e:
                output.append(f"[POP] BŁĄD: {e}")

        # 3. STOP DNA (Elite / Axe)
        dna_path = results / "stop_dna.gpkg"
        if dna_path.exists():
            try:
                dna = gpd.read_file(dna_path)
                global_stats["total_stops"] += len(dna)
                
                # Walidacja Fallbacku (Filar 2)
                # Sprawdzamy ile przystanków ma dokładnie medianę miasta (czyli zadziałał fallback)
                city_med = dna['market_val'].median()
                fallback_hits = len(dna[dna['market_val'] == city_med])
                fallback_pct = (fallback_hits / len(dna)) * 100
                
                output.append(f"[DNA] Liczba węzłów: {len(dna)} | Fallback RCN: {fallback_pct:.1f}% | CRS: {dna.crs}")
                
                # Top 5 Elite
                top_5 = dna.sort_values('local_score', ascending=False).head(5)
                output.append("\nTOP 5 PRZYSTANKÓW (ELITE):")
                output.append(f"{'Rank':4} | {'Grade':2} | {'Nazwa':35} | {'Infra':8} | {'Pop500':6} | {'Price':8} | {'Freq':5}")
                for _, r in top_5.iterrows():
                    output.append(f"{r['local_rank']:<4} | {r['grade']:2} | {r['name'][:35]:35} | {r['infra_score']:<8.0f} | {r['pop_val']:<6.0f} | {r['market_val']:<8.0f} | {r['transit_freq']:<5.1f}")

                # Bottom 5 Axe
                bot_5 = dna.sort_values('local_score', ascending=True).head(5)
                output.append("\nBOTTOM 5 PRZYSTANKÓW (THE AXE LIST):")
                for _, r in bot_5.iterrows():
                    output.append(f"{r['local_rank']:<4} | {r['grade']:2} | {r['name'][:35]:35} | {r['infra_score']:<8.0f} | {r['pop_val']:<6.0f} | {r['market_val']:<8.0f} | {r['transit_freq']:<5.1f}")
                
            except Exception as e:
                output.append(f"[DNA] BŁĄD: {e}")
        else:
            output.append("[DNA] STATUS: NOT COMPUTED")

    # GLOBAL SUMMARY
    output.append("\n" + "="*110)
    output.append("GLOBAL SYSTEM SUMMARY")
    output.append("="*110)
    output.append(f"Total Agglomerations: {len(cities)}")
    output.append(f"Total Transactions:   {global_stats['total_rcn']:,.0f}")
    output.append(f"Total Stops:          {global_stats['total_stops']:,.0f}")
    output.append(f"Total Reachable Pop:  {global_stats['total_pop']:,.0f}")
    output.append(f"Report saved to: {report_path}")

    final_text = "\n".join(output)
    print(final_text)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(final_text)

if __name__ == "__main__":
    run_master_audit()
