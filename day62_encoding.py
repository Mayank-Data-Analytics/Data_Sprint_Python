print("Initiating Categorical Encoder...")

# 1. THE RAW BUSINESS DATA
# A list of user subscription statuses
statuses = ["Active", "Churned", "Active", "Active", "Churned"]

# 2. THE BINARY TRANSLATION ENGINE
encoded_statuses = []

for status in statuses:
    if status == "Churned":
        encoded_statuses.append(1)  # 1 indicates the "event" occurred
    elif status == "Active":
        encoded_statuses.append(0)  # 0 indicates the event did not occur

# 3. TERMINAL OUTPUT
print(f"Raw Business Statuses: {statuses}")
print(f"Machine Learning Ready (Binary): {encoded_statuses}")