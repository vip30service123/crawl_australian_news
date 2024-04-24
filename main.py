from scrapy.crawler import CrawlerProcess

from crawl_website import QuotesSpider


process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()

