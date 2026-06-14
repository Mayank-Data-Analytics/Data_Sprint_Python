import pandas as pd

# 1. INGESTION
df = pd.read_csv('editor_metrics.csv')

# 2. COLUMN SELECTION
# Use bracket notation to extract a single metric. 
# This returns a Pandas Series (a 1D array).
editors_only = df['Editor_Name']
print("--- EDITOR COLUMN ONLY ---")
print(editors_only)
print("\n")

# 3. ROW FILTRATION (The Logic Engine)
# We wrap a condition inside the brackets. 
# This returns a new DataFrame containing ONLY rows where Retention is greater than 60%.
high_retention = df[df['Retention_Pct'] > 60.0]
print("--- HIGH RETENTION EDITORS (>60%) ---")
print(high_retention)
print("\n")

# 4. DATA PURGING (The Clean Up)
# Yesterday, df.info() exposed a missing Retention_Pct for 'Alex' in row 6.
# .dropna() ruthlessly deletes any row that contains a missing (NaN) value.
clean_df = df.dropna()
print("--- CLEANED DATA (NO BLANK ROWS) ---")
print(clean_df)