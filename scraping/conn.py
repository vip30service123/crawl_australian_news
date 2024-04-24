from pymongo import MongoClient


def get_database(dbname: str = "crawled_website", colname: str = None):
 
    CONNECTION_STRING = "mongodb://localhost:27017"

    client = MongoClient(CONNECTION_STRING)
 
    if colname:
        return client[dbname][colname]

    else:
        return client[dbname]



# if __name__=="__main__":
#     client = get_database()['sky_news_au']

#     item = {
#         'name': "Johan",
#         'age': 12
#     }

#     client.insert_many([item])