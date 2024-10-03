from selenium import webdriver
from selenium.webdriver.common.by import By

import spiders

import json

homepage = "https://finance.yahoo.com/"
articles_links = [
    "https://finance.yahoo.com/video/brian-cornells-plan-target-back-095539854.html",
    "https://finance.yahoo.com/news/target-ceo-hopes-the-company-will-eventually-remove-locked-cases-as-it-combats-retail-theft-130049971.html",
]

stocks_links = [
    "https://finance.yahoo.com/quote/AMZN/",
    "https://finance.yahoo.com/quote/NKE/"
]

print("Starting the web driver...")
driver = webdriver.Chrome()
print("Web driver started.")

driver.get(homepage)
spiders.reject_cookies(driver)

articles = []
stocks = []
stock_changes = []

for article_url in articles_links:
    article = spiders.read_article(driver, article_url)
    articles.append(article.__dict__)


    print("Reading stock changes")
    stock_change = spiders.read_stock_change(driver, article_url)
    stock_changes.append(stock_change)
    print("Stock changes read")



for stock_url in stocks_links:
    stock = spiders.read_stock(driver, stock_url)
    stocks.append(stock.stock_data)


combined_data = {
    "articles": articles,
    "stocks": stocks,
    "stock_changes": stock_changes
}

with open('articles.json', 'w') as f:
    json.dump(combined_data, f, indent=4)




# driver.implicitly_wait(0.5)

