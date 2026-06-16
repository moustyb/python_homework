# Task 3: Write a Program to Extract Data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time

# Initialize Selenium with headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Load the web page
url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)
time.sleep(3)  # Wait for page to load

# Find all li elements for search results
book_items = driver.find_elements(By.CSS_SELECTOR, "li.title-info")
print(f"Found {len(book_items)} book items.\n")

results = []

# Main loop to extract data
for item in book_items:
    try:
        # Find Title
        title_elem = item.find_element(By.CSS_SELECTOR, "a.title")
        title = title_elem.text.strip()
        
        # Find Author(s)
        author_elems = item.find_elements(By.CSS_SELECTOR, "span.author a")
        authors = [a.text.strip() for a in author_elems]
        author_str = "; ".join(authors) if authors else "Unknown Author"
        
        # Find Format and Year
        format_elem = item.find_element(By.CSS_SELECTOR, "span.format")
        format_year = format_elem.text.strip()
        
        # Create dict and append
        book_dict = {
            "Title": title,
            "Author": author_str,
            "Format-Year": format_year
        }
        results.append(book_dict)
        
    except Exception as e:
        continue

driver.quit()

# Create DataFrame and print
df = pd.DataFrame(results)
print("Extracted Data DataFrame:")
print(df.head(), "\n")

# Task 4: Write out the data
# Write to CSV
df.to_csv("get_books.csv", index=False)
print("✅ Saved to get_books.csv")

# Write to JSON
with open("get_books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4)
print("✅ Saved to get_books.json")
