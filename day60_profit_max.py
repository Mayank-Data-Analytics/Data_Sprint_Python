print("Initiating Profit Maximization Engine...")

# 1. THE RAW SCENARIO DATA
quantity = [100, 200, 300, 400, 500]
price = [50, 45, 40, 35, 30]
total_cost = [1000, 1500, 2200, 3200, 4500]

# 2. TOTAL REVENUE (TR) CALCULATION
total_revenue = []
for i in range(len(quantity)):
    tr = quantity[i] * price[i]
    total_revenue.append(tr)

# 3. MARGINAL REVENUE (MR) & MARGINAL COST (MC)
mr_list = []
mc_list = []
quantities_for_margin = []

# We start the loop at index 1 because Marginal metrics require looking backward
# to calculate the change from the previous tier.
for i in range(1, len(quantity)):
    delta_tr = total_revenue[i] - total_revenue[i-1]
    delta_tc = total_cost[i] - total_cost[i-1]
    delta_q = quantity[i] - quantity[i-1]
    
    mr = delta_tr / delta_q
    mc = delta_tc / delta_q
    
    mr_list.append(mr)
    mc_list.append(mc)
    quantities_for_margin.append(quantity[i])

# 4. TERMINAL OUTPUT & BUSINESS LOGIC
print("\n--- MARGINAL ANALYSIS (per 100 users) ---")
optimal_q = None
smallest_difference = float('inf')

for i in range(len(mr_list)):
    current_mr = mr_list[i]
    current_mc = mc_list[i]
    current_q = quantities_for_margin[i]
    
    print(f"Scaling to {current_q} Users -> MR: ${current_mr:.2f} | MC: ${current_mc:.2f}")
    
    # Mathematical Engine to find MR = MC
    diff = abs(current_mr - current_mc)
    if current_mr >= current_mc and diff < smallest_difference:
        smallest_difference = diff
        optimal_q = current_q

# 5. THE EXECUTIVE VERDICT
print("\n--- EXECUTIVE VERDICT ---")
if optimal_q:
    print(f"To maximize absolute profit, STOP scaling at exactly {optimal_q} users.")
    print("Scaling past this point means acquiring the next user costs more than the revenue they generate.")