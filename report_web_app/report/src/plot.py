import re

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from .conn import get_database, filter_by_days
from .functions import lowercase_string_ls, remove_stop_words, extract_nouns_from_text, extract_words, remove_stop_words_bigram


def top_k_keywords(save_path: str, topk: int = 10, days: str = "all") -> None:
    days_num = -1
    if days == "1 day":
        days_num = 1
    elif days == "1 month":
        days_num = 30
    elif days == "1 year":
        days_num = 365

    items = filter_by_days(dbname="crawl_website", colname="sky_news_au_contents", days_num=days_num)

    words = []
    for item in items:
        for line in item['raw_content']:
            text = extract_words(line)
            words += extract_nouns_from_text(text)

    words = lowercase_string_ls(words)
    words = remove_stop_words(words)

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    top = sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:topk]

    plt.bar([item[0] for item in top], [item[1] for item in top])
    plt.xlabel("Keyword")
    plt.ylabel("Frequency")
    plt.xticks(rotation=90)
    plt.title(f"Top {topk} keywords")
    plt.savefig(save_path, bbox_inches='tight')

    plt.clf()


def top_k_bigrams(save_path: str, topk: int = 10, days: str = "all"):
    days_num = -1
    if days == "1 day":
        days_num = 1
        print("1 day")
    elif days == "1 month":
        days_num = 30
        print("1 month")
    elif days == "1 year":
        days_num = 365
        print("1 year")


    items = filter_by_days(dbname="crawl_website", colname="sky_news_au_contents", days_num=days_num)

    re_pattern = r"[^a-zA-Z\s]"

    bigrams = []
    for item in items:
        for line in item['raw_content']:

            phrases = re.split(re_pattern, line)

            for phrase in phrases:
                words = extract_words(phrase)
                bigrams += [words[i] + " " + words[i+1] for i in range(len(words)-1)]
    
    bigrams = lowercase_string_ls(bigrams)
    bigrams = remove_stop_words_bigram(bigrams)

    bigram_count = {}
    for bigram in bigrams:
        if bigram in bigram_count:
            bigram_count[bigram] += 1
        else:
            bigram_count[bigram] = 1

    top = sorted(bigram_count.items(), key=lambda item: item[1], reverse=True)[:topk]

    plt.bar([item[0] for item in top], [item[1] for item in top])
    plt.xlabel("Bigram")
    plt.ylabel("Frequency")
    plt.xticks(rotation=90)
    plt.title(f"Top {topk} bigrams")
    plt.savefig(save_path, bbox_inches='tight')

    plt.clf()
