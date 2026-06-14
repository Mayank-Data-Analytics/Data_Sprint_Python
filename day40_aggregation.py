import pandas as pd

# 1. INGESTION & PURGING (The Foundation)
df = pd.read_csv('editor_metrics.csv')
df = df.dropna() # Never calculate performance metrics on incomplete rows

# 2. BASIC MATH (Agency-Wide Metrics)
# How many total seconds of video did the agency produce?
total_duration = df['Duration_Sec'].sum()
print(f"--- TOTAL AGENCY PRODUCTION: {total_duration} Seconds ---")
print("\n")

# 3. THE PIVOT: GROUPING (Individual Editor Profiling)
# We group the data by the editor's name, isolate the Retention column, 
# and calculate the exact average for each person.
avg_retention = df.groupby('Editor_Name')['Retention_Pct'].mean()
print("--- AVERAGE RETENTION BY EDITOR ---")
print(avg_retention)
print("\n")

# 4. MULTI-METRIC AGGREGATION (The Operational Dashboard)
# This is your true dashboard. It counts how many videos they cut, 
# and calculates their average video duration and retention rate simultaneously.
executive_summary = df.groupby('Editor_Name').agg(
    Total_Videos=('Video_ID', 'count'),
    Avg_Duration=('Duration_Sec', 'mean'),
    Avg_Retention=('Retention_Pct', 'mean')
)

print("--- REBUILD REACH: EXECUTIVE PERFORMANCE SUMMARY ---")
print(executive_summary)