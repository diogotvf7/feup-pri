from selenium import webdriver
from selenium.webdriver.common.by import By
from models.stock_change import StockChange

def read_stock_change(driver, link):
    driver.get(link)
    try: 
        carousel = driver.find_element(By.CLASS_NAME, "carousel-top")
    except:
        print("No stock carousel found.")
        return "N/A"
    stock_changes = carousel.find_elements(By.CLASS_NAME, "ticker")
    if (len(stock_changes) == 0):
        print("No stock changes found.")
        return "N/A"
    
    stock_objects = []
    for stock in stock_changes:
        stock_name = stock.get_attribute("title")
        percent_change = stock.find_element(By.CLASS_NAME, "percentChange").find_element(By.XPATH, ".//span").text
        stock_objects.append(StockChange(stock_name, percent_change).__dict__)

    return stock_objects