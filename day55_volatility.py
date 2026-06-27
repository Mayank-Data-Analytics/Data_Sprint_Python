import pandas as pd

print("Initiating Quantitative Volatility Engine...")

# 1. THE INGESTION
# We load yesterday's pivot table. We command Pandas to treat the 'Date' column as the official index.
input_filename = 'portfolio_matrix_30d.csv'

try:
    df = pd.read_csv(input_filename, index_col='Date', parse_dates=True)
    print("Multi-Asset Matrix loaded successfully.")
except FileNotFoundError:
    print(f"CRITICAL ERROR: '{input_filename}' not found. Did you complete Day 54?")
    exit()

# 2. THE TRANSFORMATION (Daily Returns)
# .pct_change() automatically subtracts yesterday's price from today's, and divides by yesterday's price.
# This gives us the exact percentage the asset moved each day.
daily_returns = df.pct_change()

# The first row will be 'NaN' (Not a Number) because there is no "yesterday" to compare to. We drop it.
daily_returns = daily_returns.dropna()

print("\n--- DAILY RETURNS MATRIX (Percentage Movements) ---")
# Multiply by 100 to make it readable (e.g., 0.05 becomes 5.0%)
print((daily_returns.head() * 100).round(2).astype(str) + '%')

# 3. QUANTITATIVE RISK PROFILING (Standard Deviation)
# .std() calculates how wildly the daily returns swing away from their average. 
# A higher number means higher risk.
volatility_profile = daily_returns.std() * 100

print("\n--- 30-DAY VOLATILITY RISK PROFILE (%) ---")
print(volatility_profile.round(2))

# 4. THE EXPORT
output_filename = 'portfolio_daily_returns.csv'
daily_returns.to_csv(output_filename)

print(f"\nPipeline Closed. Risk data secured to '{output_filename}'")