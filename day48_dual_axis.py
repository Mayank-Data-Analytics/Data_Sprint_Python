import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Initiating Dual-Axis Overlay Engine...")

# 1. THE INGESTION (Simulating 6 Months of SaaS Performance)
# Notice the massive difference in scale between Revenue ($) and Churn (%).
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Revenue_USD': [45000, 48000, 52000, 51000, 59000, 64000],
    'Churn_Rate_Pct': [6.5, 5.8, 5.0, 5.2, 3.5, 2.1]
}
df = pd.DataFrame(data)

# 2. THE CANVAS SETUP
# We define the master canvas (fig) and the Primary Left Axis (ax1)
fig, ax1 = plt.subplots(figsize=(10, 6))
sns.set_theme(style="whitegrid") # Using a lighter grid for complex overlays

# 3. VISUALIZATION LOGIC: LAYER 1 (The Bar Chart on Left Axis)
# Plotting the massive Revenue numbers first.
sns.barplot(
    ax=ax1, 
    data=df, x='Month', y='Revenue_USD', 
    color='#3498db', alpha=0.7 # alpha=0.7 makes the bars slightly transparent
)
ax1.set_ylabel('Monthly Revenue (USD)', color='#2980b9', fontweight='bold', fontsize=12)
ax1.tick_params(axis='y', labelcolor='#2980b9') # Colors the left axis numbers blue

# 4. THE SPLIT (Creating the Secondary Right Axis)
# .twinx() clones the X-axis but creates a brand new independent Y-axis on the right side.
ax2 = ax1.twinx()

# 5. VISUALIZATION LOGIC: LAYER 2 (The Line Chart on Right Axis)
# Plotting the tiny Churn percentages over the bars.
sns.lineplot(
    ax=ax2, 
    data=df, x='Month', y='Churn_Rate_Pct', 
    color='#e74c3c', linewidth=3, marker='o', markersize=8
)
ax2.set_ylabel('Churn Rate (%)', color='#c0392b', fontweight='bold', fontsize=12)
ax2.tick_params(axis='y', labelcolor='#c0392b') # Colors the right axis numbers red
# Force the right axis to always start at 0 so the trend isn't visually misleading
ax2.set_ylim(0, 8) 

# 6. EXECUTIVE FORMATTING
plt.title('SaaS Performance: Revenue Growth vs. Churn Reduction', fontweight='bold', fontsize=16, pad=15)
plt.tight_layout()

# 7. THE EXPORT
output_filename = 'dual_axis_overlay.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

print(f"--- DUAL-AXIS GENERATION COMPLETE ---")
print(f"Success: Executive asset securely exported to '{output_filename}'")