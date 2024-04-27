import matplotlib.pyplot as plt

from .conn import get_database
from .utils import extract_words


def most_word_appearence(save_path: str, topk:int = 10) -> None:
    
    db_collection = get_database(dbname="crawl_website", colname="sky_news_au_contents")

    items = [item for item in db_collection.find()]

    words = []

    for item in items:
        for line in item['raw_content']:
            words += extract_words(line)

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    top = sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:topk]

    print(top)

    plt.bar([item[0] for item in top], [item[1] for item in top])

    plt.savefig(save_path)