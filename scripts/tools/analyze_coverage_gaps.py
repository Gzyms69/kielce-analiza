import geopandas as gpd
import pandas as pd
from pathlib import Path
import sqlite3

MASTER_DB = "data/database/master_analytical.gpkg"

def analyze_gaps():
    print("=== DEEP DATA INTEGRITY & COVERAGE AUDIT ===\n")
    
    # 1. Wczytanie próbek z bazy Master
    print("  Loading Master Data Samples...")
    stops = gpd.read_file(MASTER_DB, layer="stops")
    transactions = gpd.read_file(MASTER_DB, layer="transactions")
    
    # 2. Statystyki ogólne
    print(f"  Total Master Stops: {len(stops)}")
    print(f"  Total Master Transactions (2025+): {len(transactions)}")
    
    # 3. Analiza cen (Realism Check)
    print("\n  Price Distribution (Checking for outliers/0 values):")
    stats = transactions['tran_cena_brutto'].describe()
    print(stats)
    
    invalid_prices = transactions[transactions['tran_cena_brutto'] <= 0].shape[0]
    print(f"  Transactions with Price <= 0: {invalid_prices} (Invalid)")
    
    # 4. Analiza geograficzna - Top Cities by Wealth
    print("\n  Top 5 Most Active Cities (by Transaction Count):")
    print(transactions['city'].value_counts().head(5))
    
    print("\n  Average Price per City (Quick Look):")
    avg_prices = transactions.groupby('city')['tran_cena_brutto'].mean().sort_values(ascending=False)
    print(avg_prices.head(10))
    
    # 5. Wyjaśnienie Luki Pokrycia (Warszawa case study)
    print("\n  DEEP DIVE: Why Warszawa has only 33-40% coverage?")
    warszawa_stops = stops[stops['city'] == 'warszawa']
    warszawa_rcn = transactions[transactions['city'] == 'warszawa']
    
    print(f"    Warszawa Stops: {len(warszawa_stops)}")
    print(f"    Warszawa Transactions (2025+): {len(warszawa_rcn)}")
    print(f"    Ratio (Stops/RCN): {len(warszawa_rcn)/len(warszawa_stops):.2f}")
    
    # Jeśli na 10,000 przystanków mamy tylko 4,000 transakcji z 2025 roku, 
    # to matematycznie niemożliwe jest 100% pokrycia w promieniu 1500m dla każdego.
    
    # 6. Sprawdzenie Koordynatów (Czy są w Polsce?)
    print("\n  Spatial Bounds Check (EPSG:2180):")
    bounds = transactions.total_bounds
    print(f"    Min X: {bounds[0]:.0f}, Min Y: {bounds[1]:.0f}")
    print(f"    Max X: {bounds[2]:.0f}, Max Y: {bounds[3]:.0f}")
    # EPSG:2180 bounds should be roughly [170000, 130000] to [870000, 780000]
    
    if 170000 < bounds[0] < 870000 and 130000 < bounds[1] < 780000:
        print("    [PASS] All coordinates are within Poland's 1992 grid.")
    else:
        print("    [FAIL] Some coordinates are outside Poland! Investigation required.")

if __name__ == "__main__":
    analyze_gaps()
