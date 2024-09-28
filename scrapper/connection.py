from selenium import webdriver
from selenium.webdriver.common.by import By
from database.database import Database

articles = [
    "https://finance.yahoo.com/video/brian-cornells-plan-target-back-095539854.html",
    "https://finance.yahoo.com/news/target-ceo-hopes-the-company-will-eventually-remove-locked-cases-as-it-combats-retail-theft-130049971.html",
]

def reject_cookies():
    driver.implicitly_wait(1)
    print(f"Current url is {driver.current_url}")
    if "consent.yahoo.com" in driver.current_url:
        print("Rejecting cookies...")
        reject_button = driver.find_element(By.XPATH, "//button[@name='reject']")
        reject_button.click()
        print("Cookies rejected.")
    else:
        print("No cookies to reject.")

def save_article(database, article):
    driver.get(articles[0])

    reject_cookies()
    # print entire html
    # print(driver.page_source)

    title = driver.find_element(By.XPATH, "//h1[@class='cover-title']").text
    print(f"Title: {title}")

    author = driver.find_element(By.XPATH, "//a[contains(@data-ylk, 'elm:author')]").text
    print(f"Author: {author}")

    created_at = driver.find_element(By.XPATH, "//time[]").get_attribute("datetime")
    print(f"Created at: {created_at}")

    body = driver.find_element(By.XPATH, "//div[@class='body']").text
    print(f"Body: {body}")
    
    database.insert("articles", ["title", "author", "created_at", "body"], [title, author, created_at, body])

database = Database()

print("Starting the web driver...")
driver = webdriver.Firefox()
print("Web driver started.")

driver.implicitly_wait(1)

driver.implicitly_wait(1)

for (i, article) in enumerate(articles):
    print(f"Processing article {i + 1}...")
    save_article(database, article)

print("Waiting for the page to load...")
driver.implicitly_wait(2)

reject_cookies()



