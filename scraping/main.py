from scrapy.crawler import CrawlerProcess

from crawl_website_sky_news import QuotesSpider


process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()

