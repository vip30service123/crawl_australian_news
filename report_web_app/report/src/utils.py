import re
from typing import List


def extract_words(string: str) -> List[str]:
    pattern = r"\w+"

    return re.findall(pattern, string)


