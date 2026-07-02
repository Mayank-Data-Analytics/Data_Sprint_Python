print("Initiating Microeconomics Elasticity Engine...")

# 1. THE SCENARIO DATA
old_price = 50.00
new_price = 65.00

old_users = 2000
new_users = 1750

# 2. THE MATHEMATICAL ENGINE
# Formula: (New - Old) / Old
pct_change_price = (new_price - old_price) / old_price
pct_change_users = (new_users - old_users) / old_users

# 3. PRICE ELASTICITY OF DEMAND (PED)
ped = pct_change_users / pct_change_price

# 4. TERMINAL OUTPUT
print("\n--- RAW METRICS ---")
print(f"Price Increase: {pct_change_price * 100:.2f}%")
print(f"User Churn (Quantity Drop): {pct_change_users * 100:.2f}%")
print(f"\nPrice Elasticity of Demand (PED): {ped:.2f}")

# 5. THE EXECUTIVE VERDICT
# We use the absolute value (abs) because PED is traditionally read as a positive number
print("\n--- BUSINESS OUTCOME ---")
ped_absolute = abs(ped)

if ped_absolute > 1.0:
    print("Verdict: ELASTIC. Users are highly sensitive to price. This price hike will likely destroy overall revenue.")
elif ped_absolute < 1.0:
    print("Verdict: INELASTIC. Users are sticky. You can safely raise prices and increase overall profitability.")
else:
    print("Verdict: UNIT ELASTIC. The user loss perfectly offsets the price gain. Revenue remains flat.")