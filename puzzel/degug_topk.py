from collections import Counter
import heapq


class CustomWord:
    def __init__(self, wrd, count):
        self.wrd = wrd
        self.count = count

    def __lt__(self, otherWord):
        if self.count == otherWord.count:
            return self.wrd > otherWord.wrd
        return self.count < otherWord.count


def topNCompetitors(numCompetitors, topNCompetitors, competitors,
                    numReviews, reviews):
    # WRITE YOUR CODE HERE
    # Well I dont really need numCompetitors or numReviews.
    # I plan to use a heap structure to maintain the list of topNCompetitors
    # I can use my own comparator method to compare two elements

    # Working on the edge case when topNCompetitors is more

    if numCompetitors == 0 or topNCompetitors == 0 or competitors == None or len(
            competitors) == 0 or reviews == None or numReviews == 0 or len(reviews) == 0 or len(
            competitors) != numCompetitors or len(reviews) != numReviews:
        return []

    if numCompetitors == 0 or topNCompetitors == 0 or competitors == None or len(
            competitors) == 0 or reviews == None or numReviews == 0 or len(reviews) == 0 or len(
        competitors) != numCompetitors or len(reviews) != numReviews:
        return []
    lst_wrd = []

    for review in reviews:
        lst_wrd += set(review.lower().replace('[^a-z0-9]', '').split())

    res = []
    if (topNCompetitors > numCompetitors):
        for comp in competitors:
            if (comp in lst_wrd):
                res.append(comp)
        return sorted(set(res))

    count = Counter(lst_wrd)
    heap = []

    for wrd, frq in count.items():
        if wrd in competitors:
            heapq.heappush(heap, CustomWord(wrd, frq))
            if len(heap) > topNCompetitors:
                heapq.heappop(heap)

    # res2 = []
    # for _ in range(topNCompetitors):
    #     res2.append(heapq.heappop(heap).wrd)
    # print(res2)

    res = [heapq.heappop(heap).wrd for _ in range(topNCompetitors)][::-1]
    print(res)
    print(type(res))
    return res

    pass



numCompetitors = 6
topNCompetitorss = 2
competitors = ["deltacellular", "anacell", "anacell", "betacellular", "cetracular", "eurocell"]
numReviews = 5
reviews = [
    "I love anacell deltacellular Best services; Best services provided by anacell",
    "betacellular has great services",
    "deltacellular provides much better services than betacellular anacell",
    "cetracular is worse than anacell",
    "Betacellular is better than deltacellular."
]


print(topNCompetitors(numCompetitors, topNCompetitorss, competitors, None, reviews))