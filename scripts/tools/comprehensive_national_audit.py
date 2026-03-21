import geopandas as gpd
import pandas as pd
import json
from pathlib import Path
import os
from datetime import datetime

def run_full_audit():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    report_path = Path(f"reports/FULL_AUDIT_{timestamp}.txt")
    
    data_dir = Path("data")
    cities_root = data_dir / "cities"
    cities = sorted([d.name for d in cities_root.iterdir() if d.is_dir() and d.name != 'rail'])
    
    output = []
    output.append(f"==========================================================================================")
    output.append(f"   NATIONAL TRANSIT & REAL ESTATE DNA - FULL SYSTEM AUDIT (v8.8)")
    output.append(f"   Generated: {timestamp}")
    output.append(f"==========================================================================================\n")

    total_stops = 0
    total_pop = 0

    for city in cities:
        output.append(f"\n[AGLOMERACJA: {city.upper()}]")
        output.append("-" * 90)
        
        dna_path = cities_root / city / "04_results" / "stop_dna.gpkg"
        pop_path = cities_root / city / "02_spatial" / "population_250m.gpkg"
        rcn_path = cities_root / city / "02_spatial" / "transactions.gpkg"

        # 1. Statystyki Ogólne
        try:
            pop_val = gpd.read_file(pop_path)['TOT'].sum()
            total_pop += pop_val
            rcn_df = gpd.read_file(rcn_path)
            med_price = rcn_df['price_m2'].median()
            output.append(f"Populacja: {pop_val:,.0f} | Mediana RCN: {med_price:,.0f} PLN/m2 | Transakcje: {len(rcn_df)}")
        except:
            output.append("BŁĄD: Nie można wczytać podstawowych danych przestrzennych.")
            continue

        # 2. Audyt DNA
        if dna_path.exists():
            try:
                dna = gpd.read_file(dna_path)
                total_stops += len(dna)
                
                # Top 5 Elitarnych Przystanków
                top_5 = dna.sort_values('local_score', ascending=False).head(5)
                output.append("\nTOP 5 PRZYSTANKÓW (ELITE):")
                output.append(f"{'Rank':4} | {'Grade':2} | {'Nazwa':35} | {'Score':6} | {'Pop500':6} | {'Price':8} | {'Freq':5}")
                for _, r in top_5.iterrows():
                    output.append(f"{r['local_rank']:<4} | {r['grade']:2} | {r['name'][:35]:35} | {r['local_score']:<6.2f} | {r['pop_val']:<6.0f} | {r['market_val']:<8.0f} | {r['transit_val']:<5.1f}")

                # Bottom 5 Najsłabszych Przystanków
                bot_5 = dna.sort_values('local_score', ascending=True).head(5)
                output.append("\nBOTTOM 5 PRZYSTANKÓW (THE AXE LIST):")
                for _, r in bot_5.iterrows():
                    output.append(f"{r['local_rank']:<4} | {r['grade']:2} | {r['name'][:35]:35} | {r['local_score']:<6.2f} | {r['pop_val']:<6.0f} | {r['market_val']:<8.0f} | {r['transit_val']:<5.1f}")
                
                output.append("-" * 90)
            except Exception as e:
                output.append(f"BŁĄD DNA: {str(e)}")
        else:
            output.append("STATUS: DNA NOT COMPUTED")

    # Podsumowanie Globalne
    output.append(f"\n\n{'='*90}")
    output.append(f"GLOBAL SUMMARY")
    output.append(f"{'='*90}")
    output.append(f"Total Agglomerations: {len(cities)}")
    output.append(f"Total Stops Analyzed: {total_stops:,.0f}")
    output.append(f"Total Human Reach:    {total_pop:,.0f}")
    output.append(f"Full Report saved to: {report_path}")

    final_text = "\n".join(output)
    print(final_text)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(final_text)

if __name__ == "__main__":
    run_full_audit()
