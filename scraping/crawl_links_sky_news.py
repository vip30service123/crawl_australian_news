import scrapy
from datetime import datetime

from conn import get_database


collection = get_database(dbname="crawl_website", colname="sky_news_au_links_business")

crawled_links = [item['link'] for item in collection.find()]


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://www.skynews.com.au/australia-news",
        "https://www.skynews.com.au/world-news",
        "https://www.skynews.com.au/opinion",
        "https://www.skynews.com.au/business",
        "https://www.skynews.com.au/lifestyle",
    ]

    def parse(self, response):
        links = set()
        for link in response.xpath("//a/@href").extract():
            try:
                if "https://www.skynews.com.au/" in link and link not in links and link not in crawled_links and link.count("/") > 3:
                    links.add(link)
            except:
                continue

        links = [{"link": link, "crawl_date": datetime.now()} for link in links]


        if links:
            collection.insert_many(links)
