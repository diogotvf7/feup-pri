from selenium import webdriver
from selenium.webdriver.common.by import By

import spiders

import json

homepage = "https://finance.yahoo.com/"
articles_links = [
    "https://finance.yahoo.com/video/brian-cornells-plan-target-back-095539854.html",
    "https://finance.yahoo.com/news/target-ceo-hopes-the-company-will-eventually-remove-locked-cases-as-it-combats-retail-theft-130049971.html",
]

print("Starting the web driver...")
driver = webdriver.Firefox()
print("Web driver started.")

driver.get(homepage)
spiders.reject_cookies(driver)

articles = []
for article_url in articles_links:
    article = spiders.read_article(driver, article_url)
    articles.append(article.__dict__)

with open('articles.json', 'w') as f:
    json.dump(articles, f, indent=4)



# driver.implicitly_wait(0.5)

