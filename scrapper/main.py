from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os, spiders, json
from collections import Counter


os.makedirs("database", exist_ok=True)

homepage = "https://finance.yahoo.com"
article_page = "https://finance.yahoo.com/topic/stock-market-news"
#article_page = "https://finance.yahoo.com/topic/latest-news/"
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


#get_article_links(driver, articles_links)
#get_stock_links(driver, stocks_links)
print(len(stocks_links))

counter = 0
stocks_links_list = list(stocks_links)  # Convert the set to a list

""" for i in range(0, len(stocks_links_list)):
    print("Read stock: " + stocks_links_list[i] + " number " + str(counter))
    try:
        stock = spiders.read_stock(driver, stocks_links_list[i])
        if stock is not None:
            stocks.append(stock)
    except Exception as e:
        print("Exception thrown: ", str(e))

    if (i % 100 == 0):  
        driver = webdriver.Chrome()
        driver.get(homepage)
        spiders.reject_cookies(driver)
    counter += 1    """


counter = 0
articles_links_list = list(articles_links)
print(len(articles_links_list))

""" for i in range(0, len(articles_links)):
    if(articles_links_list[i] != "https://finance.yahoo.com/news/home-furniture-retailer-stocks-q2-075938416.html"):
        print("Read article: " + articles_links_list[i] + " number " + str(counter))
        counter += 1
        try:
            article = spiders.read_article(driver, articles_links_list[i])
            articles.append(article)
        except Exception as e:
            print("Exception thrown: ", str(e))
        if (i % 100 == 0):  
            driver = webdriver.Chrome()
            driver.get(homepage)
            spiders.reject_cookies(driver)
 """

def load_json_data(filepath):
    if os.path.exists(filepath):  
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []   

def append_to_json(filepath, new_data):
    current_data = load_json_data(filepath)  
    current_data.extend(new_data)  
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(current_data, f, indent=4, ensure_ascii=False)  

#append_to_json('database/article.json', [article.to_dict() for article in articles])
#append_to_json('database/stock.json', [stock.to_dict() for stock in stocks])

def count_unique_articles(filepath):
    data = load_json_data(filepath)
    unique_titles = set(article['title'] for article in data if 'title' in article)
    print(f"Total unique articles: {len(unique_titles)}")
    return unique_titles

def find_duplicate_articles(filepath):
    data = load_json_data(filepath)
    
    title_counter = Counter(article['title'] for article in data if 'title' in article)
    
    duplicates = {title: count for title, count in title_counter.items() if count > 1}
    
    if duplicates:
        print("Duplicate articles found:")
        for title, count in duplicates.items():
            print(f'"{title}" appears {count} times')
    else:
        print("No duplicate articles found.")

def remove_duplicates_and_save(filepath):
    data = load_json_data(filepath)
    unique_articles = {}
    
    for article in data:
        title = article.get('title')
        if title and title not in unique_articles:
            unique_articles[title] = article  # Store article in dictionary by title
    cleaned_data = list(unique_articles.values())
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, indent=4, ensure_ascii=False)
    
    print(f"Removed duplicates. {len(data) - len(cleaned_data)} duplicates removed.")
    print(f"Saved cleaned data to {filepath}.")


def print_unique_dates(filepath):
    data = load_json_data(filepath)
    unique_dates = set()
    for article in data:
        date_str = article.get('created_at')
        if date_str:
            try:
                unique_dates.add(date_str)  
            except ValueError:
                print(f"Invalid date format for article titled '{article.get('title', 'Unknown')}'")
    print("Unique dates in the articles:")
    for date in sorted(unique_dates):
        print(date)

print_unique_dates('database/data.json')
unique_titles = count_unique_articles('database/data.json')
#remove_duplicates_and_save('database/data.json')
find_duplicate_articles('database/data.json')

driver.close()


