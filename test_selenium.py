from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch Chrome
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

print("Page Title:", driver.title)

driver.quit()
