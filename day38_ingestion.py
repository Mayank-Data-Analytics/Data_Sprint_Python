import pandas as pd

# 1. THE INGESTION: Pulling the CSV file into a Pandas DataFrame
df = pd.read_csv('editor_metrics.csv')

# 2. THE INSPECTION: Never print the whole DataFrame if it has 10,000 rows. 
# .head() prints only the first 5 rows so you can verify it loaded correctly.
print("--- FIRST 5 ROWS ---")
print(df.head())
print("\n")

# 3. THE AUDIT: .info() tells you exactly how many rows, columns, and data types you have.
# It instantly exposes missing data (Notice row 6 has a blank Retention_Pct in the CSV).
print("--- DATA AUDIT ---")
print(df.info())
print("\n")

# 4. THE MATH: .describe() instantly calculates the count, mean, min, and max 
# for every single numeric column in the file. 
print("--- STATISTICAL SUMMARY ---")
print(df.describe())