from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a != 0:
            heappush(max_heap, (-a, 'a'))
            print("A", max_heap)
        if b != 0:
            heappush(max_heap, (-b, 'b'))
            print("b" , max_heap)
        if c != 0:
            heappush(max_heap, (-c, 'c'))
            print("c", max_heap)
        s = []
        while max_heap:
            print("max_heap:", max_heap)
            print("S:", s)
            first, char1 = heappop(max_heap)  # char with most rest numbers
            print("first: ", first, " char1: ", char1)
            if len(s) >= 2 and s[-1] == s[-2] == char1:  # check whether this char is the same with previous two
                if not max_heap:  # if there is no other choice, just return
                    return ''.join(s)
                second, char2 = heappop(max_heap)  # char with second most rest numbers
                s.append(char2)
                second += 1  # count minus one, because the second here is negative, thus add 1
                if second != 0:  # only if there is rest number count, add it back to heap
                    heappush(max_heap, (second, char2))
                heappush(max_heap, (first, char1))  # also need to put this part back to heap
                continue

            #  situation that this char can be directly added to answer
            s.append(char1)
            first += 1
            if first != 0:
                heappush(max_heap, (first, char1))
        return ''.join(s)


s = Solution()
print(s.longestDiverseString(1, 2, 5))