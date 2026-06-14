import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. THE INGESTION
print("Loading clean metrics from the ETL pipeline...")
df = pd.read_csv('clean_pipeline_metrics.csv')

# 2. THE CANVAS SETUP
# Defining the exact dimensions of the image asset.
plt.figure(figsize=(10, 6))
# Setting a clean, professional background grid (highly preferred in corporate reporting).
sns.set_theme(style="darkgrid")

# 3. THE VISUALIZATION LOGIC
# Commanding Seaborn to build a bar chart analyzing the team.
# 'hue' color-codes them based on whether they met the >60% target.
chart = sns.barplot(
    data=df,
    x='Editor_Name',
    y='Retention_Pct',
    hue='Target_Met',
    palette={True: '#2ecc71', False: '#e74c3c'} # Green for success, Red for failure
)

# 4. EXECUTIVE FORMATTING
# This proves to an employer that you care about readability and presentation.
plt.title('Team Performance: Average Viewer Retention', fontsize=16, fontweight='bold')
plt.xlabel('Team Member', fontsize=12)
plt.ylabel('Average Viewer Retention (%)', fontsize=12)

# 5. THE EXPORT
# We export it as a hard, high-resolution PNG asset to attach to a portfolio or report.
output_filename = 'performance_analysis.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

print(f"--- VISUALIZATION COMPLETE ---")
print(f"Success: Portfolio asset securely exported to '{output_filename}'")