from selenium import webdriver
from selenium.webdriver.common.by import By

def reject_cookies(driver):
    if "consent.yahoo.com" in driver.current_url:
        reject_button = driver.find_element(By.XPATH, "//button[@name='reject']")
        reject_button.click()