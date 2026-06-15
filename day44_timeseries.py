import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Initiating Time-Series Engine...")

# 1. THE INGESTION (Simulating a 30-Day Financial Log)
# We use a dictionary to simulate pulling 30 days of revenue data from a database.
raw_data = {
    'Date': ['2026-05-01', '2026-05-02', '2026-05-03', '2026-05-04', '2026-05-05', 
             '2026-05-06', '2026-05-07', '2026-05-08', '2026-05-09', '2026-05-10',
             '2026-05-11', '2026-05-12', '2026-05-13', '2026-05-14', '2026-05-15',
             '2026-05-16', '2026-05-17', '2026-05-18', '2026-05-19', '2026-05-20',
             '2026-05-21', '2026-05-22', '2026-05-23', '2026-05-24', '2026-05-25',
             '2026-05-26', '2026-05-27', '2026-05-28', '2026-05-29', '2026-05-30'],
    'Daily_Revenue': [500, 520, 480, 550, 600, 590, 610, 630, 600, 650,
                      670, 700, 680, 720, 750, 740, 780, 800, 790, 820,
                      850, 840, 880, 900, 890, 930, 950, 940, 980, 1050]
}

df = pd.DataFrame(raw_data)

# 2. THE TRANSFORMATION (The Most Critical Step in Finance/SaaS)
# Right now, the engine thinks 'Date' is just a word. We MUST convert it to a mathematical time object.
df['Date'] = pd.to_datetime(df['Date'])

# 3. THE CANVAS SETUP
plt.figure(figsize=(12, 6))
sns.set_theme(style="darkgrid")

# 4. THE VISUALIZATION LOGIC
# We command Seaborn to build a line chart to show the trend over time.
sns.lineplot(
    data=df, 
    x='Date', 
    y='Daily_Revenue', 
    color='#2980b9',   # Professional corporate blue
    linewidth=2.5,     # Thicker line for executive readability
    marker='o'         # Adds a distinct dot for every single day
)

# 5. EXECUTIVE FORMATTING
plt.title('30-Day Trailing Revenue Trend', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Daily Revenue (USD)', fontsize=12)

# This rotates the dates on the bottom axis by 45 degrees so they don't overlap and look messy.
plt.xticks(rotation=45) 

# 6. THE EXPORT
output_filename = 'revenue_timeseries.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

print(f"--- TIME-SERIES VISUALIZATION COMPLETE ---")
print(f"Success: Executive asset securely exported to '{output_filename}'")