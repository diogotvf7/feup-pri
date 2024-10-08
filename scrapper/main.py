from selenium import webdriver
import os, spiders, json

os.makedirs("database", exist_ok=True)


homepage = "https://finance.yahoo.com/"
articles_links = [
    "https://finance.yahoo.com/video/brian-cornells-plan-target-back-095539854.html",
    "https://finance.yahoo.com/news/target-ceo-hopes-the-company-will-eventually-remove-locked-cases-as-it-combats-retail-theft-130049971.html",
    "https://finance.yahoo.com/news/us-inflation-set-reassure-labor-200000086.html?guccounter=1&guce_referrer=aHR0cHM6Ly9maW5hbmNlLnlhaG9vLmNvbS8_X2d1Y19jb25zZW50X3NraXA9MTcyODIyODU2NA&guce_referrer_sig=AQAAAHp0W9cttuqOrPpNFi0-YUcezCRY0DQlT06kzPbt99HFSglWNfmjir-O_MhzWkym_vMZ-nw07unILAOsxJAD15WN-1hCGLPM1CWiXq0Av9XOcrPDvPdENzV29LMmVOAiRqrVDUrpffgqP6tflr6jkRyhiWjhhau2JJxLfoQPcE0S",
    "https://finance.yahoo.com/news/oil-moguls-emerge-key-cash-120000190.html?guce_referrer=aHR0cHM6Ly9maW5hbmNlLnlhaG9vLmNvbS8_Z3VjY291bnRlcj0x&guce_referrer_sig=AQAAAC3MUqC0ymDqmMDY9U9VmDpzuFbisJ8tMR2ufCebzhUnMdX-mz5tWKzMaCt72iP7adkPV0_2TsM5UeBJmdMawNKRHN6cYxaDWAyvCLemXG47K_TUL6tM2O5u4C20PPdSoMnfbzzrEhbnnsEPv2klySMolweBK6roew6tdtjBN2mS&_guc_consent_skip=1728228656",
    "https://finance.yahoo.com/news/foxconn-third-quarter-revenue-jumps-074035303.html?guccounter=1&guce_referrer=aHR0cHM6Ly9maW5hbmNlLnlhaG9vLmNvbS90b3BpYy9sYXRlc3QtbmV3cy8_Z3VjY291bnRlcj0x&guce_referrer_sig=AQAAAH9hENzbUigxIXYrmf2O_-EaOd3EF9VuzIFQLSIqRhgjGdbl6jHBNbNbDYy98KieRXickWt1aGf-G1gSLAJ4HiY4XeU0x1RePNY82MU3XdWuEqrtMtTC01rpaCvXuuFQmbYbj31mHVD_4lsoCTHjS6umLDSVB3ghhhetcNZFBiLl"
    "https://finance.yahoo.com/news/solar-power-companies-growing-fast-043418350.html"
]

stocks_links = [
    "https://finance.yahoo.com/quote/AMZN/",
    "https://finance.yahoo.com/quote/NKE/"
]

print("Starting the web driver...")
driver = webdriver.Chrome()
print("Web driver started.")

driver.get(homepage)
spiders.reject_cookies(driver)

articles = []
stocks = []
stock_changes = []

for article_url in articles_links:
    article = spiders.read_article(driver, article_url)
    articles.append(article)

for stock_url in stocks_links:
    stock = spiders.read_stock(driver, stock_url)
    stocks.append(stock)



with open('database/article.json', 'w') as f:
    json.dump([article.to_dict() for article in articles], f, indent=4)

with open('database/stock.json', 'w') as f:
    json.dump([stock.to_dict() for stock in stocks], f, indent=4)

with open('database/stock_change.json', 'w') as f:
    json.dump(stock_changes, f, indent=4)


driver.close()


