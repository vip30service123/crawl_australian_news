from typing import List

from nltk.corpus import stopwords


def lowercase_string_ls(string_ls: List[str]) -> List[str]:
    return [i.lower() for i in string_ls]


def remove_stop_words(string_ls: List[str]) -> List[str]:
    
    stop_words = set(stopwords.words('english'))

    return [w for w in string_ls if w not in stop_words]

