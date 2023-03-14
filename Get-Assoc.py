from selenium import webdriver
from selenium.webdriver.common.by import By

url = input("Enter URL: ")

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode

with webdriver.Chrome(options=options) as driver:
    driver.get(url)
    links = [a.get_attribute("href") for a in driver.find_elements(By.TAG_NAME, "a")]

# Write links to file
with open("links.txt", "w") as f:
    f.write("\n".join(filter(None, links)))
