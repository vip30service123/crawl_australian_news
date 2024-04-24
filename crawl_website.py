import scrapy
from conn import get_database
from datetime import datetime, timedelta



class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        "https://edition.cnn.com/2024/04/23/politics/senate-vote-foreign-aid/index.html"
    ]

    def parse(self, response):
        
        
