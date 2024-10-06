from selenium import webdriver
from selenium.webdriver.common.by import By
import models

def read_article(driver, link):
    driver.get(link)
    
    title = driver.find_element(By.CLASS_NAME, "cover-title").text

    #Problem here - inconsistent in the website
    authors_element = driver.find_element(By.CLASS_NAME, "byline-attr-author")
    authors_links = authors_element.find_elements(By.XPATH, ".//a")
    authors = ""
    for author in (authors_links):
        authors += author.text + " "

    created_at = driver.find_element(By.CLASS_NAME, "byline-attr-meta-time").text

    body = driver.find_element(By.CLASS_NAME, "body")
    paragraphs = body.find_elements(By.XPATH, ".//p")
    article_text = ""
    for paragraph in paragraphs:
        article_text += paragraph.text + " " 

    return models.Article(title, authors, created_at, article_text)