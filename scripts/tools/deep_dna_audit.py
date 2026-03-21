import geopandas as gpd
import pandas as pd
import json
from pathlib import Path
import os
from datetime import datetime

def run_deep_audit():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    report_path = Path(f"reports/DNA_AUDIT_{timestamp}.txt")
    
    output = []
    output.append(f"=== DEEP DATA INTEGRITY & POI DNA AUDIT (v7.8) - {timestamp} ===\n")
    
    data_dir = Path("data")
    cities_root = data_dir / "cities"
    cities = sorted([d.name for d in cities_root.iterdir() if d.is_dir() and d.name != 'rail'])
    
    total_pop = 0
    total_rcn = 0
    
    for city in cities:
        city_header = f"\n{'='*90}\n MIASTO: {city.upper()}\n{'='*90}"
        output.append(city_header)
        
        spatial = cities_root / city / "02_spatial"
        config = cities_root / city / "03_config"
        
        # 1. Pop Coverage
        pop_val = 0
        if (spatial / "population_250m.gpkg").exists():
            try:
                pop_df = gpd.read_file(spatial / "population_250m.gpkg")
                pop_val = pop_df['TOT'].sum()
                output.append(f"[POPULACJA] Całkowita w strefach: {pop_val:,.0f} osób")
                total_pop += pop_val
            except Exception as e:
                output.append(f"[POPULACJA] BŁĄD ODCZYTU: {e}")
        
        # 2. RCN Audit
        if (spatial / "transactions.gpkg").exists():
            try:
                rcn = gpd.read_file(spatial / "transactions.gpkg")
                if 'price_m2' in rcn.columns:
                    prices = pd.to_numeric(rcn['price_m2'], errors='coerce').dropna()
                    med = prices.median()
                    mx = prices.max()
                    output.append(f"[RCN] Liczba transakcji: {len(rcn)} | Mediana: {med:,.0f} PLN | Max: {mx:,.0f} PLN")
                    total_rcn += len(rcn)
            except Exception as e:
                output.append(f"[RCN] BŁĄD ODCZYTU: {e}")
        
        # 3. Top 20 POI DNA
        if (config / "poi_valuation.json").exists():
            try:
                with open(config / "poi_valuation.json", "r") as f:
                    val_data = json.load(f)
                sorted_poi = sorted(val_data.items(), key=lambda x: x[1]['final_value'], reverse=True)
                
                output.append(f"[POI DNA] Top 20 kategorii (według wagi istotności):")
                output.append(f"{'Pozycja':3} | {'Kategoria OSM':30} | {'Tier':15} | {'Ilość':5} | {'Wartość Jedn.'}")
                output.append("-" * 80)
                for i, (cat, d) in enumerate(sorted_poi[:20], 1):
                    output.append(f"{i:<7} | {cat:30} | {d['tier']:15} | {d['count']:5} | {d['final_value']:,.0f}")
            except Exception as e:
                output.append(f"[POI] BŁĄD ODCZYTU: {e}")

    summary = f"\n\n{'='*90}\nGLOBAL SUMMARY - {timestamp}\n{'='*90}\n"
    summary += f"Total Population Covered: {total_pop:,.0f}\n"
    summary += f"Total RCN Transactions:   {total_rcn:,.0f}\n"
    summary += f"Report saved to: {report_path}\n"
    output.append(summary)

    final_text = "\n".join(output)
    print(final_text)
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(final_text)

if __name__ == "__main__":
    run_deep_audit()
