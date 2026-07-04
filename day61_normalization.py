print("Initiating Feature Engineering: Min-Max Normalizer...")

# 1. THE RAW DATA (Vastly different scales)
user_ages = [22, 45, 33, 28, 50]
annual_spend = [150.00, 8500.00, 3200.00, 450.00, 12000.00]

# 2. THE MATHEMATICAL ENGINE
def min_max_scaler(data_list):
    min_val = min(data_list)
    max_val = max(data_list)
    normalized_list = []
    
    for x in data_list:
        # The Min-Max Formula
        x_norm = (x - min_val) / (max_val - min_val)
        normalized_list.append(round(x_norm, 4))
        
    return normalized_list

# 3. EXECUTION & TERMINAL OUTPUT
norm_ages = min_max_scaler(user_ages)
norm_spend = min_max_scaler(annual_spend)

print(f"\nRaw Ages: {user_ages}")
print(f"Normalized Ages (0 to 1): {norm_ages}")

print(f"\nRaw Spend: {annual_spend}")
print(f"Normalized Spend (0 to 1): {norm_spend}")