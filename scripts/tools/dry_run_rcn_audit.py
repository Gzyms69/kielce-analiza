import geopandas as gpd
import pandas as pd
from pathlib import Path
import os
import warnings

warnings.filterwarnings('ignore')

def audit_rcn_data():
    print("=== DEEP AUDIT OF RCN DATA (POST-HARVEST) ===")
    data_dir = Path("data/cities")
    
    cities = sorted([d.name for d in data_dir.iterdir() if d.is_dir() and d.name != 'rail' and (data_dir / d.name / '02_spatial' / 'transactions.gpkg').exists()])
    
    report = []
    
    for city in cities:
        gpkg_path = data_dir / city / "02_spatial" / "transactions.gpkg"
        
        try:
            df = gpd.read_file(gpkg_path)
            
            if df.empty:
                report.append({"city": city, "status": "EMPTY", "count": 0, "min_date": "N/A", "max_date": "N/A", "null_price": "N/A", "null_area": "N/A", "avg_price_m2": "N/A"})
                continue
            
            # Check dates (FIX: mixed timezones)
            if 'dok_data' in df.columns:
                df['dok_data'] = pd.to_datetime(df['dok_data'], errors='coerce', utc=True)
                min_date = df['dok_data'].min().strftime('%Y-%m-%d') if not df['dok_data'].isna().all() else "N/A"
                max_date = df['dok_data'].max().strftime('%Y-%m-%d') if not df['dok_data'].isna().all() else "N/A"
            else:
                min_date = "NO_COL"
                max_date = "NO_COL"
                
            # Check prices and areas
            null_price = 0
            null_area = 0
            avg_price_m2 = 0
            
            if 'tran_cena_brutto' in df.columns:
                # Oczyszczanie tekstu z formatowania w GML jesli to string
                if df['tran_cena_brutto'].dtype == 'object':
                     df['tran_cena_brutto'] = df['tran_cena_brutto'].str.replace(' ', '').str.replace(',', '.')
                df['tran_cena_brutto'] = pd.to_numeric(df['tran_cena_brutto'], errors='coerce')
                null_price = df['tran_cena_brutto'].isna().sum()
                
            if 'lok_pow_uzyt' in df.columns:
                if df['lok_pow_uzyt'].dtype == 'object':
                     df['lok_pow_uzyt'] = df['lok_pow_uzyt'].str.replace(' ', '').str.replace(',', '.')
                df['lok_pow_uzyt'] = pd.to_numeric(df['lok_pow_uzyt'], errors='coerce')
                null_area = df['lok_pow_uzyt'].isna().sum()
                
            if 'tran_cena_brutto' in df.columns and 'lok_pow_uzyt' in df.columns:
                df['price_m2_raw'] = df['tran_cena_brutto'] / df['lok_pow_uzyt']
                valid_prices = df[(df['price_m2_raw'] > 0) & (df['price_m2_raw'] < 100000)]['price_m2_raw']
                if not valid_prices.empty:
                    avg_price_m2 = valid_prices.mean()
                    
            report.append({
                "city": city,
                "status": "OK",
                "count": len(df),
                "min_date": min_date,
                "max_date": max_date,
                "null_price": null_price,
                "null_area": null_area,
                "avg_price_m2": f"{avg_price_m2:.0f}"
            })
            
        except Exception as e:
            report.append({"city": city, "status": f"ERR: {str(e)[:20]}", "count": 0, "min_date": "N/A", "max_date": "N/A", "null_price": "N/A", "null_area": "N/A", "avg_price_m2": "N/A"})
            
    df_report = pd.DataFrame(report)
    print("\n" + df_report.to_string(index=False))

if __name__ == "__main__":
    audit_rcn_data()
