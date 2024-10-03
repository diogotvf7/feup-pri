from selenium import webdriver
from selenium.webdriver.common.by import By

# class Scraper:
#     def __init__(self):
#         self.driver = webdriver.Firefox()
        
def reject_cookies(driver):
    if "consent.yahoo.com" in driver.current_url:
        print("Rejecting cookies...")
        reject_button = driver.find_element(By.XPATH, "//button[@name='reject']")
        reject_button.click()
        print("Cookies rejected.")
    else:
        print("No cookies to reject.")

