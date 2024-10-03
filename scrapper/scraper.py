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

def get_stock_change(driver):
    try: 
        carousel = driver.find_element(By.CLASS_NAME, "carousel-top")
    except:
        print("No stock carousel found.")
        return
    try:
        stock_changes = carousel.find_elements(By.CLASS_NAME, "ticker")
    except:
        print("No stock changes found.")
        return

    for stock in stock_changes:
        stock_name = stock.get_attribute("title")
        percent_change = stock.find_element(By.CLASS_NAME, "percentChange").find_element(By.XPATH, ".//span").text
        print("Stock change: " + stock_name + ":  "  + percent_change)