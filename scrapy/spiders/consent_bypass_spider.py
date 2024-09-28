from pathlib import Path

import scrapy


class ConsentBypassSpider(scrapy.Spider):
    name = "consent_bypass"

    def start_requests(self):
        urls = [
            "https://finance.yahoo.com/video/brian-cornells-plan-target-back-095539854.html",
            "https://finance.yahoo.com/news/target-ceo-hopes-the-company-will-eventually-remove-locked-cases-as-it-combats-retail-theft-130049971.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.url.split("/")
        yield {
            'Article Title': title
        }
