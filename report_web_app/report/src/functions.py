import re
from typing import List, Union

from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag


def lowercase_string_ls(string_ls: List[str]) -> List[str]:
    return [i.lower() for i in string_ls]


def remove_stop_words(string_ls: List[str]) -> List[str]:
    
    stop_words = set(stopwords.words('english'))

    return [w for w in string_ls if w not in stop_words]


def extract_nouns_from_text(text: Union[str, List[str]]) -> List[str]:

    if type(text) == str:
        text = word_tokenize(text)

    pos_tagged = pos_tag(text)

    nouns = filter(lambda x: x[1]=='NN', pos_tagged)

    return [p[0] for p in nouns]


def extract_words(string: str) -> List[str]:
    pattern = r"\w+"

    return re.findall(pattern, string)