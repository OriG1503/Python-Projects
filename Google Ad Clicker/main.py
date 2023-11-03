#region - Imports
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
import random
from selenium.webdriver import ActionChains
#endregion

#region - Main Variables 
driver = webdriver.Chrome()
action = ActionChains(driver)
#endregion

#region - All Functions
def page_scroll_down():
    scroll_duration = [0.5,0.125,0.658,0.8,1,1.5,2]  # Adjust this value to control the scroll speed
    scroll_height = 100  # Adjust this value to control how much to scroll in pixels
    start_time = time.time()
    duration = 10

    # Scroll down repeatedly until you reach the bottom of the page
    while time.time() - start_time < duration:
        driver.execute_script(f"window.scrollBy(0, {scroll_height});")
        time.sleep(random.choice(scroll_duration))
        
        # Define a condition to stop scrolling, for example, reaching the bottom of the page
        if driver.execute_script("return window.innerHeight + window.scrollY >= document.body.offsetHeight"):
            break

def open_web():
    #פתיחת דף האינטרנט המבוקש
    driver.get("https://www.google.com/")
    driver.maximize_window()
    time.sleep(2)

def search_bar_typing(searchPhrase):
    #מציאת הבר של החיפוש וכתיבת הערך
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(searchPhrase)
    search_box.submit()
    time.sleep(2)

def find_ads():
    adClickAbleSections = driver.find_elements(
        By.XPATH, "//a[contains(@class,'sVXRqc')]"
        )
    return adClickAbleSections
    
def click_ads():
    adClickAbleSections = find_ads()
    length = len(adClickAbleSections)

    for i in range(0, length):
        action.key_down(Keys.CONTROL).perform()
        adClickAbleSections[i].click()
        action.key_up(Keys.CONTROL).perform()
        time.sleep(2)
    time.sleep(3)

    enter_ads_tabs(length)

def enter_ads_tabs(length):
    for i in range(0, length):
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        page_scroll_down()
        time.sleep(5)
        driver.close()

def stop_script():
    time.sleep(5)
    driver.quit()

#endregion

def main(searchPhrase):

    open_web()

    search_bar_typing(searchPhrase)    

    click_ads()

for i in range(3):
    main("Domain Buying")

stop_script()