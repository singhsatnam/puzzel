import collections
import re


def mostCommonWord(p, banned):
    ban = set(banned)
    words = re.findall(r'\w+', p.lower())
    return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]

mostCommonWord("pippa is the best dog and pippa is also hungry")