from selenium import webdriver
from selenium.webdriver.common.by import By
import spiders

# //ul[@class="My(0)"]

class Scrapper():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.data = {}

    def run(self, homepage):
        self.driver.get(homepage)
        spiders.reject_cookies(self.driver)
        
        # while True:
        #     option = input("What would you like to do? (1) Read articles (2) Read stocks (3) Exit: ")

        #     match option:
        #         case "1":
        #             self.read_articles()
        #         case "2":
        #             self.read_stocks()
        #         case "3":
        #             break
        #         case _:
        #             print("Invalid option.")
        #     pass

    def execute_spider(func):
        def wrapper(self, *args, **kwargs):
            return func(self, *args, **kwargs)
        return wrapper
    
    def __del__(self):
        self.driver.close()
    

