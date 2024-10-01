from selenium import webdriver
from selenium.webdriver.common.by import By
from models.article import Article

# TODO: Add this information to the database
def read_article(driver, link):
    driver.get(link)
    
    title = driver.find_element(By.CLASS_NAME, "cover-title").text

    authors = driver.find_element(By.CLASS_NAME, "byline-attr-author").find_elements(By.XPATH, ".//a")
    authors = ""
    for author in authors:
        authors += author.text + " "

    created_at = driver.find_element(By.CLASS_NAME, "byline-attr-meta-time").text

    body = driver.find_element(By.CLASS_NAME, "body")
    paragraphs = body.find_elements(By.XPATH, ".//p")
    article_text = ""
    for paragraph in paragraphs:
        article_text += paragraph.text + " " 

    return Article(title, authors, created_at, article_text)