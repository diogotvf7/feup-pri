from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os, spiders, json

os.makedirs("database", exist_ok=True)

homepage = "https://finance.yahoo.com"
article_page = "https://finance.yahoo.com/topic/stock-market-news"
stock_pages = ["https://finance.yahoo.com/markets/stocks/most-active", "https://finance.yahoo.com/markets/stocks/gainers", "https://finance.yahoo.com/markets/stocks/losers"]
articles_links = set()
stocks_links = set()

print("Starting the web driver...")
driver = webdriver.Chrome()
print("Web driver started.")

driver.get(homepage)
spiders.reject_cookies(driver)

articles = []
stocks = []
stock_changes = []

def get_number_of_li_elements(ul_element):
    return len(ul_element.find_elements(By.TAG_NAME, 'li'))

def get_article_links(driver, a_links):

    curr_scroll = 2000

    driver.get(article_page)

    articles_ul = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.My\\(0\\).P\\(0\\).Wow\\(bw\\).Ov\\(h\\)'))
    )

    prev_n_articles = get_number_of_li_elements(articles_ul)

    while True:
        try:
            driver.execute_script(f'window.scrollTo(0,{curr_scroll})')
            curr_scroll += 2000

            WebDriverWait(driver, 1).until(
                lambda d: get_number_of_li_elements(articles_ul) > prev_n_articles
            )

            prev_n_articles = get_number_of_li_elements(articles_ul)

        except TimeoutException: #Loaded all articles, leaves the loop
            break

    articles_li = articles_ul.find_elements(By.TAG_NAME, 'li')

    for article in articles_li:
        try:
            url = article.find_element(By.TAG_NAME, 'a').get_attribute('href')
            if url.startswith('https://finance.yahoo.com/news'):
                a_links.add(url)
        except NoSuchElementException:
            continue

def get_stock_links(driver, s_links):
    for page in stock_pages:

        driver.get(page)
        temp_links = set()
        no_more_links = False

        #Gets all possible URLs on the pages, if you want to limit the urls per page change the condition for a length on temp_stock_links
        while(True):

            for i in range(25):
                try:
                    stocks_tr = driver.find_element(By.ID, f'{i}')

                except: #Loaded all stocks, leaves the loop
                    no_more_links = True
                    break

                a_tag = stocks_tr.find_element(By.TAG_NAME, 'a')

                temp_links.add(a_tag.get_attribute('href'))

            if no_more_links: break

            driver.find_element(By.CSS_SELECTOR, '[aria-label="Goto next page"]').click()

            sleep(0.5)

        s_links.update(temp_links)

get_article_links(driver, articles_links)

print(len(articles_links))
print(articles_links)

get_stock_links(driver, stocks_links)

print(len(stocks_links))
print(stocks_links)


# for stock_url in stocks_links:
#     stock = spiders.read_stock(driver, stock_url)
#     stocks.append(stock)

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


