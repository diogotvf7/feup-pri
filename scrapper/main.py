from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os, spiders, json

os.makedirs("database", exist_ok=True)


homepage = "https://finance.yahoo.com/topic/stock-market-news"
articles_links = []

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
curr_scroll = 2000

articles_ul = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.My\\(0\\).P\\(0\\).Wow\\(bw\\).Ov\\(h\\)'))
)

def get_number_of_li_elements(ul_element):
    return len(ul_element.find_elements(By.TAG_NAME, 'li'))

prev_n_articles = get_number_of_li_elements(articles_ul)

while True:
    try:
        driver.execute_script(f'window.scrollTo(0,{curr_scroll})')
        #print('dei scroll')
        curr_scroll += 2000

        WebDriverWait(driver, 1).until(
            lambda d: get_number_of_li_elements(articles_ul) > prev_n_articles
        )

        print(f"Articles: {get_number_of_li_elements(articles_ul)}")

        prev_n_articles = get_number_of_li_elements(articles_ul)

    except TimeoutException:
        print("No articles loaded, leaving while loop.")
        break
    
    
#print('acabei os scrolls')

articles_li = articles_ul.find_elements(By.TAG_NAME, 'li')

for article in articles_li:
    try:
        url = article.find_element(By.TAG_NAME, 'a').get_attribute('href')
        if url.startswith('https://finance.yahoo.com/news'):
            articles_links.append(url)
    except NoSuchElementException:
        next

print(articles_links)
print(len(articles_links))
print(len(articles_links) != len(set(articles_links)))


# for stock_url in stocks_links:
#     stock = spiders.read_stock(driver, stock_url)
#     stocks.append(stock)

for article_url in articles_links:
    article = spiders.read_article(driver, article_url)
    articles.append(article)

    stock_change = spiders.read_stock_change(driver, article_url)
    stock_changes.append(stock_change)

# for stock_url in stocks_links:
#     stock = spiders.read_stock(driver, stock_url)
#     stocks.append(stock)



with open('database/article.json', 'w') as f:
    json.dump([article.to_dict() for article in articles], f, indent=4)

# with open('database/stock.json', 'w') as f:
#     json.dump([stock.to_dict() for stock in stocks], f, indent=4)

# with open('database/stock_change.json', 'w') as f:
#     json.dump(stock_changes, f, indent=4)


driver.close()


