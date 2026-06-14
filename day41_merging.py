import pandas as pd

# 1. THE FRACTURED DATA (Simulating two different operational files)

# Table A: The Video Production Log
videos_df = pd.DataFrame({
    'Video_ID': ['V101', 'V102', 'V103', 'V104'],
    'Editor_Name': ['Alex', 'Sam', 'Alex', 'Jordan'],
    'Client': ['Apex Corp', 'Nova Tech', 'Zenith Media', 'Apex Corp']
})

# Table B: The Contractor Payroll Rates
rates_df = pd.DataFrame({
    'Editor_Name': ['Alex', 'Sam', 'Jordan'],
    'Cost_Per_Video': [150, 200, 120]
})

# 2. THE MERGE (The Engine at Work)
# We fuse the payroll rates into the video log by matching the 'Editor_Name'.
# 'how="left"' ensures we keep every single video in the left table, even if an editor is missing from the rates table.
financial_log = pd.merge(videos_df, rates_df, on='Editor_Name', how='left')

# 3. VECTORIZED MATH (Creating New Data)
# Assume Rebuild Reach charges clients a flat $500 per video. 
# We create a Revenue column, then subtract the Cost column to calculate exact Profit.
financial_log['Client_Revenue'] = 500
financial_log['Agency_Profit'] = financial_log['Client_Revenue'] - financial_log['Cost_Per_Video']

print("--- REBUILD REACH: PER-VIDEO PROFITABILITY LOG ---")
print(financial_log)