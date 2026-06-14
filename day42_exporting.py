import pandas as pd

# 1. THE EXTRACT (Ingesting the raw data)
print("Initiating Pipeline...")
df = pd.read_csv('editor_metrics.csv')

# 2. THE TRANSFORM (Cleaning and Engineering)
# We drop the blank rows and use .copy() to ensure we own the new DataFrame.
clean_df = df.dropna().copy()

# We engineer a new column to instantly flag top-tier editors.
clean_df['Target_Met'] = clean_df['Retention_Pct'] > 60.0

# 3. THE LOAD (Exporting the Asset)
# We command Pandas to write the clean_df into a brand new file.
# 'index=False' prevents Pandas from writing the arbitrary row numbers (0, 1, 2) into the final file.
output_filename = 'clean_pipeline_metrics.csv'
clean_df.to_csv(output_filename, index=False)

print("--- PIPELINE COMPLETE ---")
print(f"Success: Processed data securely exported to '{output_filename}'")