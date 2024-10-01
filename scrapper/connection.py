from selenium import webdriver
from selenium.webdriver.common.by import By
from scraper import get_article_information, reject_cookies
from database.database import Database

articles = [
    "https://finance.yahoo.com/video/brian-cornells-plan-target-back-095539854.html",
    "https://finance.yahoo.com/news/target-ceo-hopes-the-company-will-eventually-remove-locked-cases-as-it-combats-retail-theft-130049971.html",
]

# database = Database()

print("Starting the web driver...")
driver = webdriver.Firefox()
print("Web driver started.")

driver.get(articles[0])

print("Waiting for the page to load...")
driver.implicitly_wait(2)

reject_cookies(driver)
get_article_information(driver)


driver.implicitly_wait(0.5)

