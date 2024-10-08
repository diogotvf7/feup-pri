from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os, spiders, json

os.makedirs("database", exist_ok=True)


homepage = "https://finance.yahoo.com/topic/stock-market-news"
articles_links = [

]

stocks_links = [
    "https://finance.yahoo.com/quote/AMZN/",
    "https://finance.yahoo.com/quote/NKE/"
]

print("Starting the web driver...")
#driver = webdriver.Firefox()
driver = webdriver.Chrome()
print("Web driver started.")

driver.get(homepage)
spiders.reject_cookies(driver)

articles = []
stocks = []
stock_changes = []


articles_ul = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.My\\(0\\).P\\(0\\).Wow\\(bw\\).Ov\\(h\\)'))
)

articles_li = articles_ul.find_elements(By.TAG_NAME, 'li')

for article in articles_li:
    try:
        url = article.find_element(By.TAG_NAME, 'a').get_attribute('href')
        if url.startswith('https://finance.yahoo'):
            articles_links.append(url)
    except NoSuchElementException:
        next

print(articles_links)
for stock_url in stocks_links:
    stock = spiders.read_stock(driver, stock_url)
    stocks.append(stock)



# for article_url in articles_links:
#     article = spiders.read_article(driver, article_url)
#     articles.append(article)

#     stock_change = spiders.read_stock_change(driver, article_url)
#     stock_changes.append(stock_change)

# for stock_url in stocks_links:
#     stock = spiders.read_stock(driver, stock_url)
#     stocks.append(stock)



# with open('database/article.json', 'w') as f:
#     json.dump([article.to_dict() for article in articles], f, indent=4)

# with open('database/stock.json', 'w') as f:
#     json.dump([stock.to_dict() for stock in stocks], f, indent=4)

# with open('database/stock_change.json', 'w') as f:
#     json.dump(stock_changes, f, indent=4)


driver.close()


