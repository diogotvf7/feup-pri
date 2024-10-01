from selenium import webdriver
from selenium.webdriver.common.by import By

def read_stock_change(driver):

    names = driver.find_element(By.XPATH, "//a[@class, 'ticker medium']")
    print(names)
    names = ""
    for author in names:
        names += author.text + " "
    
    return
    






        