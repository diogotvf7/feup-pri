from selenium.webdriver.common.by import By

css_selector_for_article_paragraphs = ".article > div:nth-child(1) > div:nth-child(3) > div:nth-child(3)"


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

    article_body = driver.find_element(By.CSS_SELECTOR, css_selector_for_article_paragraphs)
    paragraphs = article_body.find_elements(By.XPATH, ".//p")
    article_text = ""
    for paragraph in paragraphs:
        article_text += paragraph.text + " " 
    print("Article Body: " + article_text)

    