from selenium import webdriver
from selenium.webdriver.common.by import By
from models.stock import Stock


# def read_stock_change(driver):

#     names = driver.find_element(By.XPATH, "//a[@class, 'ticker']")
#     print(names)
#     names = ""
#     for author in names:
#         names += author.text + " "
    
#     return
    


def get_element_text(driver, locator_type, locator_value):
    try:
        return driver.find_element(locator_type, locator_value).text
    except:
        return "N/A" 

def read_stock(driver, link):
    driver.get(link)

    stock_data = {
        "Stock Title": (By.CSS_SELECTOR, "h1.yf-xxbei9"),
        "Live Price": (By.CLASS_NAME, "livePrice"),
        "Price Change": (By.XPATH, "//section[@data-testid='quote-price']//*[contains(@data-field, 'regularMarketChange')]"),
        "Price Change Percentage": (By.XPATH, "//section[@data-testid='quote-price']//*[contains(@data-field, 'regularMarketChangePercent')]"),
        "Previous Close": (By.XPATH, "//*[@class='yf-mrt107']/*[1]/*[2]"),
        "Open": (By.XPATH, "//*[@class='yf-mrt107']/*[2]/*[2]"),
        "Bid": (By.XPATH, "//*[@class='yf-mrt107']/*[3]/*[2]"),
        "Ask": (By.XPATH, "//*[@class='yf-mrt107']/*[4]/*[2]"),
        "Day's Range": (By.XPATH, "//*[@class='yf-mrt107']/*[5]/*[2]"),
        "52 Week Range": (By.XPATH, "//*[@class='yf-mrt107']/*[6]/*[2]"),
        "Volume": (By.XPATH, "//*[@class='yf-mrt107']/*[7]/*[2]"),
        "Average Volume": (By.XPATH, "//*[@class='yf-mrt107']/*[8]/*[2]"),
        "Market Cap (intraday)": (By.XPATH, "//*[@class='yf-mrt107']/*[9]/*[2]"),
        "Beta (5Y Monthly)": (By.XPATH, "//*[@class='yf-mrt107']/*[10]/*[2]"),
        "PE Ratio (TTM)": (By.XPATH, "//*[@class='yf-mrt107']/*[11]/*[2]"),
        "EPS (TTM)": (By.XPATH, "//*[@class='yf-mrt107']/*[12]/*[2]"),
        "Earnings Date": (By.XPATH, "//*[@class='yf-mrt107']/*[13]/*[2]"),
        "Forward Dividend & Yield": (By.XPATH, "//*[@class='yf-mrt107']/*[14]/*[2]"),
        "Ex-Dividend Date": (By.XPATH, "//*[@class='yf-mrt107']/*[15]/*[2]"),
        "1y Target Est": (By.XPATH, "//*[@class='yf-mrt107']/*[16]/*[2]"),
    }
    # Not sure what to do with '--' values -> treat as null?
    
    stock_args = {}
    for label, locator in stock_data.items():
        text = get_element_text(driver, locator[0], locator[1])
        if text:
            stock_args[label] = text

    stock = Stock(**stock_args)
    return stock






        