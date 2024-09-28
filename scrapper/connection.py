from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://finance.yahoo.com/video/brian-cornells-plan-target-back-095539854.html")

driver.implicitly_wait(5)

page_html = driver.page_source
print(page_html)

title = driver.find_element(By.XPATH, "//h1").text
print(title)

title = driver.title
print(title)