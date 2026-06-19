import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Initiating Matrix Correlation Engine...")

# 1. THE INGESTION (Simulating a Multi-Metric SaaS Account Dataset)
# We are tracking 5 key business metrics across user accounts.
raw_data = {
    'Monthly_Logins': [42, 5, 12, 25, 18, 30, 8, 15, 3, 50],
    'Support_Tickets': [1, 7, 4, 2, 5, 1, 6, 3, 9, 0],
    'Features_Used': [15, 2, 5, 11, 6, 12, 3, 7, 1, 20],
    'Upgrade_Clicks': [8, 0, 2, 5, 1, 6, 0, 3, 0, 12],
    'Lifetime_Value_USD': [950, 100, 250, 600, 400, 750, 150, 300, 50, 1200]
}
df = pd.DataFrame(raw_data)

# 2. THE TRANSFORMATION (The Core Mathematical Matrix)
# df.corr() commands Pandas to calculate the mathematical correlation matrix.
# It pairs every column and scores their relationship from -1.00 (inverse) to +1.00 (perfect).
corr_matrix = df.corr()
print("\n--- PASSED: RAW MATHEMATICAL CORRELATION MATRIX ---")
print(corr_matrix)

# 3. THE CANVAS SETUP
plt.figure(figsize=(8, 6))

# 4. THE VISUALIZATION LOGIC
# We translate the complex matrix numbers into a highly scannable color grid.
sns.heatmap(
    corr_matrix,
    annot=True,             # Injects the exact mathematical score into each square
    cmap='coolwarm',        # Standard corporate colorway (Red = Positive, Blue = Negative)
    fmt=".2f",              # Standardizes decimal formatting to two points
    linewidths=0.5,         # Adds clean borders between the matrix cells
    vmin=-1, vmax=1         # Locks the color boundaries to standard statistical variance
)

# 5. EXECUTIVE FORMATTING
plt.title('SaaS Account Metrics: Multi-Variable Correlation Matrix', fontsize=14, fontweight='bold', pad=15)

# 6. THE EXPORT
output_filename = 'correlation_heatmap.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

print(f"\n--- MATRIX VISUALIZATION COMPLETE ---")
print(f"Success: Executive asset securely exported to '{output_filename}'")