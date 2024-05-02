from datetime import datetime, timedelta
from typing import List

from pymongo import MongoClient


def get_database(dbname: str = "crawled_website", colname: str = None):
 
    CONNECTION_STRING = "mongodb://localhost:27017"

    client = MongoClient(CONNECTION_STRING)
 
    if colname:
        return client[dbname][colname]

    else:
        return client[dbname]
    

def get_all_contents(dbname: str = "crawled_website", colname: str = None) -> List:
    db_collection = get_database(dbname="crawl_website", colname="sky_news_au_contents")

    return [item for item in db_collection.find()]


def filter_by_days(dbname: str = "crawled_website", colname: str = None, days_num: int = -1) -> List:
    if days_num == -1:
        return get_all_contents(dbname=dbname, colname=colname)
    
    db_collection = get_database(dbname="crawl_website", colname="sky_news_au_contents")
    d = datetime.today() - timedelta(days=days_num)

    return [item for item in db_collection.find({"published_date" : {"$gte" : d}})]
