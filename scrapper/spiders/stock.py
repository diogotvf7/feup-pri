from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from models.stock import Stock


def get_element_text(driver, locator_type, locator_value):
    try:
        return driver.find_element(locator_type, locator_value).text
    except:
        return "N/A" 

def read_stock(driver, link):
    driver.get(link)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1.yf-xxbei9"))
        )
    except TimeoutException:
        print("Page took too long to load or stock title not found.")
        return None
    

    stock_data = {
        "Stock Title": (By.CSS_SELECTOR, "h1.yf-xxbei9"),
        "Live Price": (By.CLASS_NAME, "livePrice"),
        "Price Change": (By.XPATH, "//section[@data-testid='quote-price']//*[contains(@data-field, 'regularMarketChange')]"),
        "Price Change Percentage": (By.XPATH, "//section[@data-testid='quote-price']//*[contains(@data-field, 'regularMarketChangePercent')]"),
        "Previous Close": (By.XPATH, "//*[@class='yf-11uk5vd']/*[1]/*[2]"),
        "Open": (By.XPATH, "//*[@class='yf-11uk5vd']/*[2]/*[2]"),
        "Bid": (By.XPATH, "//*[@class='yf-11uk5vd']/*[3]/*[2]"),
        "Ask": (By.XPATH, "//*[@class='yf-11uk5vd']/*[4]/*[2]"),
        "Day's Range": (By.XPATH, "//*[@class='yf-11uk5vd']/*[5]/*[2]"),
        "52 Week Range": (By.XPATH, "//*[@class='yf-11uk5vd']/*[6]/*[2]"),
        "Volume": (By.XPATH, "//*[@class='yf-11uk5vd']/*[7]/*[2]"),
        "Average Volume": (By.XPATH, "//*[@class='yf-11uk5vd']/*[8]/*[2]"),
        "Market Cap (intraday)": (By.XPATH, "//*[@class='yf-11uk5vd']/*[9]/*[2]"),
        "Beta (5Y Monthly)": (By.XPATH, "//*[@class='yf-11uk5vd']/*[10]/*[2]"),
        "PE Ratio (TTM)": (By.XPATH, "//*[@class='yf-11uk5vd']/*[11]/*[2]"),
        "EPS (TTM)": (By.XPATH, "//*[@class='yf-11uk5vd']/*[12]/*[2]"),
        "Earnings Date": (By.XPATH, "//*[@class='yf-11uk5vd']/*[13]/*[2]"),
        "Forward Dividend & Yield": (By.XPATH, "//*[@class='yf-11uk5vd']/*[14]/*[2]"),
        "Ex-Dividend Date": (By.XPATH, "//*[@class='yf-11uk5vd']/*[15]/*[2]"),
        "1y Target Est": (By.XPATH, "//*[@class='yf-11uk5vd']/*[16]/*[2]"),
    }
    stock_args = {}
    for label, locator in stock_data.items():
        text = get_element_text(driver, locator[0], locator[1])
        if (text != "--"):
            stock_args[label] = text

    stock = Stock(**stock_args)
    return stock






        