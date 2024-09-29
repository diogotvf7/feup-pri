from selenium import webdriver
from selenium.webdriver.common.by import By
from scraper import get_article_information
from database.database import Database

articles = [
    "https://finance.yahoo.com/video/brian-cornells-plan-target-back-095539854.html",
    "https://finance.yahoo.com/news/target-ceo-hopes-the-company-will-eventually-remove-locked-cases-as-it-combats-retail-theft-130049971.html",
]

def reject_cookies():
    if "consent.yahoo.com" in driver.current_url:
        print("Rejecting cookies...")
        reject_button = driver.find_element(By.XPATH, "//button[@name='reject']")
        reject_button.click()
        print("Cookies rejected.")
    else:
        print("No cookies to reject.")

#database = Database()

print("Starting the web driver...")
driver = webdriver.Firefox()
print("Web driver started.")

driver.get(articles[0])

print("Waiting for the page to load...")
driver.implicitly_wait(2)

reject_cookies()
get_article_information(driver)


driver.implicitly_wait(0.5)

