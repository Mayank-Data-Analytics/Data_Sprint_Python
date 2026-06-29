import pandas as pd

print("Initiating Predictive Feature Engineering...")

# 1. THE INGESTION
# We use the clean data you secured on Day 56
input_filename = 'bitcoin_trend_signals.csv'

try:
    df = pd.read_csv(input_filename, index_col='Date', parse_dates=True)
except FileNotFoundError:
    print(f"CRITICAL ERROR: '{input_filename}' not found. Check Week 8 execution.")
    exit()

# 2. FEATURE ENGINEERING (The Clues)
# Calculate the exact dollar change from yesterday to today
df['Daily_Dollar_Change'] = df['Daily_Price'].diff()

# 3. TARGET ENGINEERING (The Answer Key)
# .shift(-1) pulls TOMORROW'S price into TODAY'S row. 
# This is how you train a model to look at today and predict tomorrow.
df['Target_Next_Day_Price'] = df['Daily_Price'].shift(-1)

# 4. DATA CLEANSING
# The very last row will have a NaN (blank) for the Target because tomorrow hasn't happened yet. We drop it.
df = df.dropna()

# Round to 2 decimal places for institutional cleanliness
df = df.round(2)

print("\n--- PREDICTIVE DATASET HEAD ---")
# Displaying just the critical columns to verify the time-shift worked
print(df[['Daily_Price', 'Daily_Dollar_Change', 'Target_Next_Day_Price']].head())

# 5. THE EXPORT
output_filename = 'bitcoin_ml_features.csv'
df.to_csv(output_filename)

print(f"\nPipeline Closed. ML Features secured to '{output_filename}'")