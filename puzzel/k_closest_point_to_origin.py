import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        heap = []

        for (x, y) in points:
            print(x, y)
            dist = -(x * x + y * y)
            print(dist)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [(x, y) for (dist, x, y) in heap]

sol = Solution()
print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))