import scrapy
from conn import get_database
from datetime import datetime, timedelta


collection = get_database(dbname="crawl_website", colname="sky_news_au_contents")

links_collection = get_database(dbname="crawl_website", colname="sky_news_au_links_business")
crawled_content_links = [item['url'] for item in collection.find()]

available_links = [link['link'] for link in links_collection.find() if link not in crawled_content_links]


def string_to_date(string: str):
    # 2 types: "April 17, 2024 - 12:50PM" and "12 hours ago"
    try:
        hours = int(string.split()[0])
        return datetime.now() - timedelta(hours=hours)
    except:
        month = string.split()[0]
        string = string.replace(month, month[:3])
        return datetime.strptime(string, '%b %d, %Y - %I:%M%p')


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = available_links

    def parse(self, response):
        
        tag = response.xpath("//ul[@id='breadcrumbs']//a/text()").extract()
        title = response.xpath("//h1[@id='story-headline']/text()").extract()

        # there are 2 types: long and short new
        if title:
            title = title[0]
            story_intro = response.xpath("//p[@id='story-intro']/text()").extract()[0]
            authors = response.xpath("//span[@class='author_name']/a/@data-tgev-label").extract()
            published_date = response.xpath("//div[@id='publish-date']/text()").extract()[0]
            published_date = string_to_date(published_date)
            raw_content = response.xpath("//div[@class='ap-container story-body-nodes']//p//text()").extract()
        
        else:
            title = response.xpath("//h1[@class='module-header vms-header']/text()").extract()[0]
            story_intro = []
            authors = []
            published_date = response.xpath("//div[@class='date-live']/text()").extract()[0]
            published_date = string_to_date(published_date)
            raw_content = response.xpath("//div[@class='video-body']/p/text()").extract()
            

        # Join lines
        content = []
        new_line = ''
        for line in raw_content:
            new_line += line
            if line[-1] == '.':
                content.append(new_line)
                new_line = ''

        item = {
            "url": response.request.url,
            "tag": tag,
            "title": title,
            "story_intro": story_intro,
            "authors": authors,
            "published_date": published_date,
            "raw_content": raw_content
        }
        
        collection.insert_many([item])
