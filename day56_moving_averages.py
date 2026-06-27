import pandas as pd

print("Initiating Algorithmic Trend Engine...")

# 1. THE INGESTION
input_filename = 'portfolio_matrix_30d.csv'

try:
    df = pd.read_csv(input_filename, index_col='Date', parse_dates=True)
except FileNotFoundError:
    print(f"CRITICAL ERROR: '{input_filename}' not found.")
    exit()

# 2. ISOLATE THE ASSET
# We are going to extract just Bitcoin to build a clean signal matrix.
btc_df = df[['BITCOIN']].copy()
btc_df.rename(columns={'BITCOIN': 'Daily_Price'}, inplace=True)

# 3. THE MATHEMATICAL TRANSFORMATION (Moving Averages)
# .rolling(window=X).mean() tells Pandas to look at the last X days and calculate the average.
print("Calculating 7-Day and 21-Day Simple Moving Averages (SMA)...")

btc_df['7_Day_SMA'] = btc_df['Daily_Price'].rolling(window=7).mean()
btc_df['21_Day_SMA'] = btc_df['Daily_Price'].rolling(window=21).mean()

# Drop the days where the 21-Day SMA can't be calculated (the first 20 days)
btc_df = btc_df.dropna()

# Round everything to 2 decimal places for clean formatting
btc_df = btc_df.round(2)

print("\n--- BITCOIN TREND SIGNAL MATRIX ---")
print(btc_df.tail())

# 4. THE EXPORT
output_filename = 'bitcoin_trend_signals.csv'
btc_df.to_csv(output_filename)

print(f"\nPipeline Closed. Trend signals secured to '{output_filename}'")