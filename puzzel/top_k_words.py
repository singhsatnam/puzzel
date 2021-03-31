from collections import Counter
import heapq
# from typing import List
#
# class WrapString:
#     def __init__(self, string):
#         self.val = string
#
#     def __lt__(self, other):
#         return self.val > other.val  # return opposite result! why? check last comment
#
#
# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         word_count = Counter(words)
#         min_heap = []
#         for w in word_count:
#             heapq.heappush(min_heap, ((word_count[w], WrapString(w)), w))
#             if len(min_heap) > k:
#                 heapq.heappop(min_heap)
#         return [heapq.heappop(min_heap)[1] for _ in range(len(min_heap))][::-1]
#
#
# quo = ["Emo is the hottest of the season! Elmo will be on every kid's wishlist!",
# "The new Elmo dolls are super high quality",
# "Expect the Elsa dolls to be very popular this year",
#                 "Elsa and Elmo are the toys I'll be buying for my kids",
#                 "For parents of older kids, look into buying them a drone",
#                 "Warcraft is slowly rising in popularity ahead of the holiday season"]
#
# sol = Solution()
# print(sol.topKFrequent(quo, 4))
#
#
# def topKFrequent2(words, k):
#     d = {}
#     for word in words:
#         d[word] = d.get(word, 0) + 1
#
#     ret = sorted(d, key=lambda word: (-d[word], word))
#
#     return ret[:k]
#
# print(topKFrequent2(quo, 2))
#
# k = 2
# keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
# reviews = [
#     "I love anacell Best services; Best services provided by anacell",
#     "betacellular has great services",
#     "deltacellular provides much better services than betacellular",
#     "cetracular is worse than anacell",
#     "Betacellular is better than deltacellular.",
# ]

import re
from collections import Counter


class CustomWord:
    def __init__(self, wrd, count):
        self.wrd = wrd
        self.count = count

    def __lt__(self, otherWord):
        if self.count == otherWord.count:
            return self.wrd > otherWord.wrd
        return self.count < otherWord.count


def topNcompetitors(numCompetitors, topNCompetitors, competitors,
                    numReviews, reviews):

    if numCompetitors == 0 or topNCompetitors == 0 or competitors == None or len(competitors) == 0 or reviews == None or numReviews ==0 or len(reviews) == 0:
        return []



    lst_wrd = []

    for review in reviews:
        lst_wrd += set(review.lower().replace('[^a-z0-9]', '').split())

    res = []
    if (topNCompetitors > numCompetitors):
        for comp in competitors:
            if (comp in lst_wrd):
                res.append(comp)
        print(res)
        return sorted(set(res))

    count = Counter(lst_wrd)

    heap = []

    for wrd, frq in count.items():
        if wrd in competitors:
            heapq.heappush(heap, CustomWord(wrd, frq))
            if len(heap) > topNCompetitors:
                heapq.heappop(heap)

    return [heapq.heappop(heap).wrd for _ in range(topNCompetitors)][::-1]
    pass



numCompetitors = 6
topNCompetitors = 7
competitors = ["anacell", "anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
numReviews = 5
reviews = [
    "I love anacell Best services; Best services provided by anacell",
    "betacellular has great services",
    "deltacellular provides much better services than betacellular",
    "cetracular is worse than anacell",
    "Betacellular is better than deltacellular."
]


print(topNcompetitors(numCompetitors, None, competitors,
                    numReviews, reviews))