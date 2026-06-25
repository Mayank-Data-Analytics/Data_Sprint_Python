import requests
import pandas as pd
from datetime import datetime
import time

print("Initiating Multi-Asset API Aggregation Pipeline...")

# 1. THE TARGET MATRIX
assets = ['bitcoin', 'ethereum', 'solana']
master_data_vault = []

# 2. THE RATE-LIMITED EXTRACTION LOOP
for coin in assets:
    print(f"Extracting historical time-series for: {coin.upper()}...")
    
    # Dynamic Endpoint Injection
    endpoint = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
    params = {'vs_currency': 'usd', 'days': '30', 'interval': 'daily'}
    
    response = requests.get(endpoint, params=params)
    
    if response.status_code != 200:
        print(f"CRITICAL ERROR on {coin}. Status: {response.status_code}. Halting.")
        break
        
    raw_prices = response.json()['prices']
    
    for data_point in raw_prices:
        clean_date = datetime.fromtimestamp(data_point[0] / 1000).strftime('%Y-%m-%d')
        
        master_data_vault.append({
            'Date': clean_date,
            'Asset': coin.upper(),
            'Price_USD': round(data_point[1], 2)
        })
    
    # EXECUTIVE MANDATE: Respect API Firewalls
    time.sleep(2)

# 3. LOAD RAW DATA
df_raw = pd.DataFrame(master_data_vault)
df_raw = df_raw.drop_duplicates(subset=['Date', 'Asset'])

# 4. TRANSFORMATION: RELATIONAL PIVOT
# We pivot the matrix so 'Date' is the index, and each Asset gets its own column.
# This is the exact format required to run correlation math in Python.
df_pivot = df_raw.pivot(index='Date', columns='Asset', values='Price_USD')

print("\n--- AGGREGATION SUCCESSFUL: MULTI-ASSET MATRIX PREVIEW ---")
print(df_pivot.tail())

# 5. EXPORT
output_filename = 'portfolio_matrix_30d.csv'
df_pivot.to_csv(output_filename)

print(f"\nPipeline Closed. Relational matrix secured to '{output_filename}'")