# Task 6: Scraping Structured Data - OWASP Top 10
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import time

# Setup Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Load OWASP Top 10 page
url = "https://owasp.org/www-project-top-ten/"
driver.get(url)
time.sleep(3)

top_10_list = []

# Find the top 10 vulnerabilities using XPath
try:
    risk_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'risk')]//h3/a | //ul[contains(@class, 'risks')]//a")
    
    # Limit to top 10 to be safe
    for elem in risk_elements[:10]:
        title = elem.text.strip()
        href = elem.get_attribute("href")
        if title and href:
            top_10_list.append({"Vulnerability": title, "Link": href})
            
except Exception as e:
    print(f"Error finding elements: {e}")

driver.quit()

# Print to verify
print("OWASP Top 10 Extracted:")
for item in top_10_list:
    print(f"- {item['Vulnerability']}: {item['Link']}")

# Write to CSV
with open("owasp_top_10.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Vulnerability", "Link"])
    writer.writeheader()
    writer.writerows(top_10_list)

print("\n✅ Saved to owasp_top_10.csv")
