import pandas as pd

print("Initiating Pearson Correlation Analysis...")

# 1. THE INGESTION
input_filename = 'bitcoin_ml_features.csv'

try:
    df = pd.read_csv(input_filename, index_col='Date', parse_dates=True)
except FileNotFoundError:
    print(f"CRITICAL ERROR: '{input_filename}' not found. Check Day 57 execution.")
    exit()

# 2. THE MATHEMATICAL TRANSFORMATION (Correlation)
# df.corr() automatically runs the Pearson mathematical formula against every column in the dataset.
print("Calculating Statistical Correlations...")
correlation_matrix = df.corr()

# Round to 3 decimal places for statistical precision
correlation_matrix = correlation_matrix.round(3)

print("\n--- PEARSON CORRELATION MATRIX ---")
print(correlation_matrix)

# 3. ISOLATING THE TARGET SIGNAL
print("\n--- TARGET PREDICTABILITY ---")
print("How strongly do today's metrics correlate with TOMORROW'S price?")
target_correlations = correlation_matrix[['Target_Next_Day_Price']].sort_values(by='Target_Next_Day_Price', ascending=False)
print(target_correlations)

# 4. THE EXPORT
output_filename = 'bitcoin_correlation_matrix.csv'
correlation_matrix.to_csv(output_filename)

print(f"\nPipeline Closed. Matrix secured to '{output_filename}'")