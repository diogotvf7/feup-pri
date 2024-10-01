from selenium import webdriver
from selenium.webdriver.common.by import By

css_selector_for_article_paragraphs = ".article > div:nth-child(1) > div:nth-child(3) > div:nth-child(3)"


# class Scraper:
#     def __init__(self):
#         self.driver = webdriver.Firefox()
        

# TODO: Add this information to the database
def get_article_information(driver):
    article_title = driver.find_element(By.CLASS_NAME, "cover-title").text
    print("Article title: " + article_title)

    article_authors = driver.find_element(By.CLASS_NAME, "byline-attr-author").find_elements(By.XPATH, ".//a")
    authors = ""
    for author in article_authors:
        authors += author.text + " "
    print("Article authors: " + authors)

    article_date = driver.find_element(By.CLASS_NAME, "byline-attr-meta-time").text
    print("Article Data: " + article_date)
    article_body = driver.find_element(By.CLASS_NAME, "body")
    paragraphs = article_body.find_elements(By.XPATH, ".//p")
    article_text = ""
    for paragraph in paragraphs:
        article_text += paragraph.text + " " 

    print("Article Body: " + article_text)

def reject_cookies(driver):
    if "consent.yahoo.com" in driver.current_url:
        print("Rejecting cookies...")
        reject_button = driver.find_element(By.XPATH, "//button[@name='reject']")
        reject_button.click()
        print("Cookies rejected.")
    else:
        print("No cookies to reject.")

def read_stock(driver):

    stock_title = driver.find_element(By.CSS_SELECTOR, "h1.yf-xxbei9").text
    print("Stock Title: " + stock_title)


    live_price = driver.find_element(By.CLASS_NAME, "livePrice").text
    print("Live Price: " + live_price)

    price_change = driver.find_element(By.XPATH, "//section[@data-testid='quote-price']//*[contains(@data-field, 'regularMarketChange')]").text
    print("Price Change: " + price_change)

    price_change_percentage = driver.find_element(By.XPATH, "//section[@data-testid='quote-price']//*[contains(@data-field, 'regularMarketChangePercent')]").text
    print("Price change percentage: " + price_change_percentage)

    ####################################################################
    
    previous_close = driver.find_element(By.XPATH, "//*[@class='yf-mrt107']/*[1]/*[2]").text
    print("Previous Close: " + previous_close)

    open = driver.find_element(By.XPATH, "//*[@class='yf-mrt107']/*[2]/*[2]").text
    print("Open: " + open)

    bid = driver.find_element(By.XPATH, "//*[@class='yf-mrt107']/*[3]/*[2]").text
    print("Bid: " + bid)

    ask = driver.find_element(By.XPATH, "//*[@class='yf-mrt107']/*[4]/*[2]").text
    print("Ask: " + ask)

    day_range = driver.find_element(By.XPATH, "//*[@class='yf-mrt107']/*[5]/*[2]").text
    print("Day's Range: " + day_range)

    week_range = driver.find_element(By.XPATH, "//*[@class='yf-mrt107']/*[6]/*[2]").text
    print("52 Week Ranges: " + week_range)

    volume = driver.find_element(By.XPATH, "//*[@class='yf-mrt107']/*[7]/*[2]").text
    print("Volume: " + volume)

    avg_volume = driver.find_element(By.XPATH, "//*[@class='yf-mrt107']/*[8]/*[2]").text
    print("Average Volume: " + avg_volume)

    market_cap = driver.find_element(By.XPATH, "//*[@class='yf-mrt107']/*[9]/*[2]").text
    print("Market Cap (intraday): " + market_cap)

    beta = driver.find_element(By.XPATH, "//*[@class='yf-mrt107']/*[10]/*[2]").text
    print("Beta (5Y Monthly): " + beta)

    pe_ratio = driver.find_element(By.XPATH, "//*[@class='yf-mrt107']/*[11]/*[2]").text
    print("PE Ratio (TTM): " + pe_ratio)

    eps = driver.find_element(By.XPATH, "//*[@class='yf-mrt107']/*[12]/*[2]").text
    print("EPS (TTM): " + eps)

    earning_date = driver.find_element(By.XPATH, "//*[@class='yf-mrt107']/*[13]/*[2]").text
    print("Earnings Date: " + earning_date)

    forward_dividend_yeld = driver.find_element(By.XPATH, "//*[@class='yf-mrt107']/*[14]/*[2]").text
    print("Forward Dividend & Yield: " + forward_dividend_yeld)

    ex_dividend_date = driver.find_element(By.XPATH, "//*[@class='yf-mrt107']/*[15]/*[2]").text
    print("Ex-Dividend Date: " + ex_dividend_date)

    target_est = driver.find_element(By.XPATH, "//*[@class='yf-mrt107']/*[16]/*[2]").text
    print("1y Target Est: " + target_est)


