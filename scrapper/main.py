from selenium import webdriver

import os
import spiders
import json

os.makedirs("database", exist_ok=True)


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



with open('database/article.json', 'w') as f:
    json.dump(articles, f, indent=4)

with open('database/stock.json', 'w') as f:
    json.dump(stocks, f, indent=4)

with open('database/stock_change.json', 'w') as f:
    json.dump(stock_changes, f, indent=4)




# driver.implicitly_wait(0.5)

