import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Initiating Correlation Engine...")

# 1. THE INGESTION (Simulating SaaS User Data)
# We are testing the hypothesis: Does higher engagement equal higher revenue?
raw_data = {
    'User_ID': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06', 'U07', 'U08', 'U09', 'U10'],
    'Monthly_Logins': [5, 12, 18, 25, 8, 30, 42, 15, 3, 50],
    'Lifetime_Value_USD': [100, 250, 400, 600, 150, 750, 950, 300, 50, 1200]
}
df = pd.DataFrame(raw_data)

# 2. THE CANVAS SETUP
plt.figure(figsize=(10, 6))
sns.set_theme(style="darkgrid")

# 3. THE VISUALIZATION LOGIC
# A 'regplot' (Regression Plot) maps the scatter points AND calculates the trendline.
# This is a massive signal to hiring managers that you understand predictive analytics.
sns.regplot(
    data=df,
    x='Monthly_Logins',
    y='Lifetime_Value_USD',
    scatter_kws={'color': '#2980b9', 's': 100},   # 's' sets the size of the dots for readability
    line_kws={'color': '#e74c3c', 'linewidth': 2} # The regression line is red to stand out
)

# 4. EXECUTIVE FORMATTING
plt.title('Correlation Analysis: User Engagement vs. Revenue (LTV)', fontsize=16, fontweight='bold')
plt.xlabel('Monthly Logins', fontsize=12)
plt.ylabel('Customer Lifetime Value (USD)', fontsize=12)

# 5. THE EXPORT
output_filename = 'correlation_analysis.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

print(f"--- CORRELATION VISUALIZATION COMPLETE ---")
print(f"Success: Executive asset securely exported to '{output_filename}'")