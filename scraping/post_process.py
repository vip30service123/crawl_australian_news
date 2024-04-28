import fire

from conn import get_database


def post_process(
    typ: str = "links",    
) -> None:
    if typ == "contents":
        db_collection = get_database(dbname="crawl_website", colname="sky_news_au_contents")

        items = [item for item in db_collection.find()]


        checked_links = []

        for item in items:
            if item['url'] not in checked_links:
                checked_links.append(item['url'])
            else:

                db_collection.delete_one(item)

    elif typ == "links":
        db_collection = get_database(dbname="crawl_website", colname="sky_news_au_links_business")

        items = [item for item in db_collection.find()]


        checked_links = []

        for item in items:
            if item['link'] not in checked_links:
                checked_links.append(item['link'])
            else:

                db_collection.delete_one(item)

    else:
        raise Exception("No u.")


    

    
    

if __name__=="__main__":
    fire.Fire(post_process)