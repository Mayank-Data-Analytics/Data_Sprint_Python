import requests
from bs4 import BeautifulSoup
import pandas as pd
import time  # CRITICAL NEW IMPORT: Required for Rate Limiting

print("Initiating Automated Pagination Engine...")

# 1. THE VAULT & THE TARGET
data_vault = []
total_pages_to_scrape = 5  # We hardcap at 5 pages for this sandbox test to avoid server strain

# 2. THE PAGINATION LOOP
# range(1, 6) tells Python to run the loop for numbers 1, 2, 3, 4, and 5.
for page_num in range(1, total_pages_to_scrape + 1):
    
    # DYNAMIC URL INJECTION: Notice the 'f' before the string and the {page_num} variable.
    # This automatically changes the URL on every cycle (page-1.html, page-2.html, etc.)
    url = f"http://books.toscrape.com/catalogue/page-{page_num}.html"
    print(f"Executing extraction on: Page {page_num}...")
    
    response = requests.get(url)
    response.encoding = 'utf-8' # Yesterday's encoding patch
    
    # Error Handling: If a page doesn't exist (e.g., a 404 error), break the loop safely.
    if response.status_code != 200:
        print(f"Warning: Server rejected Page {page_num}. Halting pagination.")
        break
        
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('article', class_='product_pod')
    
    # 3. THE EXTRACTION
    for item in products:
        title = item.h3.a['title']
        price_string = item.find('p', class_='price_color').text
        
        # Yesterday's bulletproof cleaning logic
        clean_price = float(price_string.replace('£', '').replace('Â', '').strip())
        
        data_vault.append({
            'Product_Name': title,
            'Price_GBP': clean_price
        })
    
    # 4. EXECUTIVE MANDATE: RATE LIMITING
    # This pauses the script for exactly 1 second before requesting the next page.
    # NEVER run a loop without a sleep timer. It prevents your IP from being blacklisted.
    time.sleep(1)

# 5. THE TRANSFORMATION & LOAD (ETL)
df = pd.DataFrame(data_vault)

print(f"\n--- EXTRACTION COMPLETE: {len(df)} Total Records Secured ---")
print(df.head())

output_filename = 'scraped_paginated_books.csv'
df.to_csv(output_filename, index=False)

print(f"\nPipeline Closed. Master dataset secured to '{output_filename}'")