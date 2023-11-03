from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import time
from selenium.webdriver import ActionChains


# Initialize a WebDriver (e.g., Chrome or Firefox)
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")
time.sleep(2)

# Perform a Google search
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("Website Builder")
search_box.submit()
time.sleep(2)

# Find and open sponsored links in new tabs
sponsored_links = driver.find_elements(By.CSS_SELECTOR, ".uUPGi a")

for link in sponsored_links:
    # Open the link in a new tab
    link.send_keys(Keys.CONTROL + Keys.RETURN)
    time.sleep(2)
