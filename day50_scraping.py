import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Initiating Web Extraction Engine...")

# 1. THE TARGET
# This is a safe, legal sandbox site designed for scraping practice.
url = "http://books.toscrape.com/catalogue/category/books/science_22/index.html"

# 2. THE REQUEST
# We send a "GET" request to the server, asking it to send back the HTML code.
response = requests.get(url)
response.encoding = 'utf-8'

# Executive Error Handling: Always verify the server responded successfully (Code 200)
if response.status_code != 200:
    print(f"CRITICAL FAILURE: Server rejected request. Status Code: {response.status_code}")
    exit()

print("Connection established. Parsing DOM...")

# 3. THE PARSER
# We feed the raw, messy text into BeautifulSoup so it understands the HTML structure.
soup = BeautifulSoup(response.text, 'html.parser')

# 4. THE EXTRACTION LOGIC
# Look at the website's source code: Every product is wrapped in an <article class="product_pod"> tag.
# We command BeautifulSoup to find all of them.
products = soup.find_all('article', class_='product_pod')

data_vault = [] # Empty list to store our extracted data

for item in products:
    # Extract the Title: It is stored inside an <h3> tag, inside an <a> tag, under the attribute 'title'.
    title = item.h3.a['title']
    
    # Extract the Price: It is stored in a <p> tag with the class 'price_color'.
    price_string = item.find('p', class_='price_color').text
    
    # Data Cleaning: The price comes back as '£52.29'. We strip the '£' and convert it to a float.
    clean_price = float(price_string.replace('£', '').replace('Â', '').strip())
    
    # Append the clean data as a dictionary
    data_vault.append({
        'Product_Name': title,
        'Price_GBP': clean_price
    })

# 5. THE TRANSFORMATION & LOAD (ETL)
# We take the raw extracted list and force it into our structured Pandas framework.
df = pd.DataFrame(data_vault)

# Print a preview to the terminal to verify success
print("\n--- EXTRACTION SUCCESSFUL: DATA PREVIEW ---")
print(df.head())

# Export the newly created dataset
output_filename = 'scraped_science_books.csv'
df.to_csv(output_filename, index=False)

print(f"\nPipeline Complete. Structured data secured to '{output_filename}'")