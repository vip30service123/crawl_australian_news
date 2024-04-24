import scrapy
from conn import get_database


collection = get_database(dbname="crawl_website", colname="sky_news_au_links_business")

crawled_links = [item['link'] for item in collection.find()]


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://www.skynews.com.au/business",
    ]

    def parse(self, response):
        links = set()
        for link in response.xpath("//a/@href").extract():
            if "https://www.skynews.com.au/business/" in link and link not in crawled_links:
                links.add(link)

        links = [{'link': link} for link in links]

        collection.insert_many(links)