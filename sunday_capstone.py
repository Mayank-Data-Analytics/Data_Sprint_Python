print("Initiating EdTech Analytics Engine...\n")

# 1. THE RAW DATA
courses = ["Python Bootcamp", "SQL Mastery", "Excel for Finance", "Data Science 101", "Machine Learning"]
enrollments = [1500, 900, 2200, 800, 400]
completions = [1200, 750, 1900, 500, 150]
price_per_course = [2000, 1500, 1000, 3000, 5000]

# 2. THE CALCULATION ENGINE
total_revenue = []
drop_off_rates = []

for i in range(len(courses)):
    # Multiply enrollments by price for the current index [i]
    revenue = enrollments[i] * price_per_course[i]
    total_revenue.append(revenue)
    
    # Calculate who didn't finish, divide by total enrollments, multiply by 100 for percentage
    drop_off = ((enrollments[i] - completions[i]) / enrollments[i]) * 100
    drop_off_rates.append(round(drop_off, 2))

# 3. TERMINAL OUTPUT (Executive View)
print("--- COURSE METRICS (REVENUE & CHURN) ---")
for i in range(len(courses)):
    print(f"Course: {courses[i]}")
    # The :, formatting adds commas to the large revenue numbers for readability
    print(f"  Gross Revenue: ₹{total_revenue[i]:,}")
    print(f"  Drop-off Rate: {drop_off_rates[i]}%")
    print("-" * 40)