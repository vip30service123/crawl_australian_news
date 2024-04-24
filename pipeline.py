from scrapy.crawler import CrawlerProcess

from src.sky_news_australia.contentspider import *
from src.sky_news_australia.linkspider import *





if __name__=="__main__":
    process = CrawlerProcess()
    process.crawl(LinksSpider)
    # process.crawl(ContentSpider)
    process.start()