import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Initiating Multi-Panel Dashboard Engine...")

# 1. THE INGESTION (Simulating a SaaS Weekly Readout)
trend_data = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Revenue': [5000, 5200, 5100, 5800, 6200, 6000, 6500]
})

churn_data = pd.DataFrame({
    'Tier': ['Basic', 'Pro', 'Enterprise'],
    'Churn_Rate': [12.5, 5.2, 1.1]
})

# 2. THE CANVAS SETUP (The Subplot Grid)
# We command Matplotlib to build 1 row with 2 columns.
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))
sns.set_theme(style="darkgrid")

# 3. VISUALIZATION LOGIC: PANEL 1 (Left Side)
sns.lineplot(
    ax=axes[0], 
    data=trend_data, x='Day', y='Revenue', 
    color='#27ae60', linewidth=3, marker='o'
)
axes[0].set_title('Weekly Revenue Trend (USD)', fontweight='bold', fontsize=14)
axes[0].set_ylabel('Revenue ($)')

# 4. VISUALIZATION LOGIC: PANEL 2 (Right Side)
sns.barplot(
    ax=axes[1], 
    data=churn_data, x='Tier', y='Churn_Rate',
    palette={'Basic': '#e74c3c', 'Pro': '#f39c12', 'Enterprise': '#3498db'}
)
axes[1].set_title('Churn Rate by Subscription Tier (%)', fontweight='bold', fontsize=14)
axes[1].set_ylabel('Churn Rate (%)')

# 5. EXECUTIVE FORMATTING
# This forces Matplotlib to calculate perfect spacing so nothing overlaps.
plt.tight_layout()

# 6. THE EXPORT
output_filename = 'executive_dashboard.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

print(f"--- DASHBOARD GENERATION COMPLETE ---")
print(f"Success: Unified executive asset securely exported to '{output_filename}'")