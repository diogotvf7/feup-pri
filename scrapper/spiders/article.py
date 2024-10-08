from selenium import webdriver
from selenium.webdriver.common.by import By
from .stock_change import read_stock_change
import models


def read_article(driver, link):
    driver.get(link)    
    
    title = driver.find_element(By.CLASS_NAME, "cover-title").text

    authors_element = driver.find_element(By.CLASS_NAME, "byline-attr-author")
    authors_links = authors_element.find_elements(By.XPATH, ".//a")

    if authors_links:  
        authors_list = [author.text.strip() for author in authors_links]

    else: 
        authors_text = authors_element.text.strip()
        if (" and " in authors_text) and ("," in authors_text):
            comma_split = [name.strip() for name in authors_text.split(",")]

            last_part = comma_split.pop() 
            last_authors = [name.strip() for name in last_part.split(" and ")]

            authors_list = comma_split + last_authors
        elif " and " in authors_text:
            authors_list = [name.strip() for name in authors_text.split(" and ")]
        elif "," in authors_text:  
            authors_list = [name.strip() for name in authors_text.split(",")]
        else:  
            authors_list = [authors_text]


    created_at = driver.find_element(By.CLASS_NAME, "byline-attr-meta-time").text

    body = driver.find_element(By.CLASS_NAME, "body")
    paragraphs = body.find_elements(By.XPATH, ".//p")
    article_text = ""
    for paragraph in paragraphs:
        article_text += paragraph.text + " "
    
    stock_changes = read_stock_change(driver, link)

    return models.Article(title, created_at, article_text, stock_changes, authors=authors_list if authors_list else None)
