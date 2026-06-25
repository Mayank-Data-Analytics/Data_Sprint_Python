import requests
import pandas as pd

print("Initiating Financial API Pipeline...")

# 1. THE ENDPOINT (The Server Address)
# Instead of a website URL, we target a specific API endpoint designed for machines.
endpoint = "https://api.coingecko.com/api/v3/coins/markets"

# 2. THE PAYLOAD (Query Parameters)
# APIs allow you to filter the database before downloading it. 
# We are asking for prices in USD, sorted by Market Cap, limit 50.
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 50,
    'page': 1
}

# 3. THE REQUEST
response = requests.get(endpoint, params=params)

# Executive Error Handling
if response.status_code != 200:
    print(f"CRITICAL FAILURE: Server rejected API request. Status Code: {response.status_code}")
    exit()

print("API Connection Secured. Extracting JSON payload...")

# 4. THE PARSER (JSON Translation)
# The server responds with JSON (JavaScript Object Notation).
# The .json() command instantly translates it into a structured Python list of dictionaries.
raw_json_data = response.json()

# 5. THE TRANSFORMATION (ETL)
# The API gives us dozens of data points per asset. We only want five specific financial metrics.
data_vault = []

for asset in raw_json_data:
    data_vault.append({
        'Asset_Name': asset['name'],
        'Ticker': asset['symbol'].upper(),
        'Current_Price_USD': asset['current_price'],
        'Market_Cap_USD': asset['market_cap'],
        '24h_Volume': asset['total_volume']
    })

# Force the clean dictionary into our mathematical Pandas framework
df = pd.DataFrame(data_vault)

print("\n--- API EXTRACTION SUCCESSFUL: LIVE MARKET DATA PREVIEW ---")
print(df.head())

# 6. THE EXPORT
output_filename = 'live_crypto_market_data.csv'
df.to_csv(output_filename, index=False)

print(f"\nPipeline Closed. Financial data secured to '{output_filename}'")