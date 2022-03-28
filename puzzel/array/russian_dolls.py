from bisect import bisect_left
from typing import List


# class Solution:
#     def maxEnvelopes(self, E: List[List[int]]) -> int:
#         E.sort(key=lambda x: (x[0], -x[1]))
#         print(E)
#         dp = []
#         for _, height in E:
#             print("dp: ", dp, "height:", height)
#             left = bisect_left(dp, height)
#             print("left:", left)
#             if left == len(dp):
#                 print("len == left, appending")
#                 dp.append(height)
#             else:
#                 print("len != left, inserting")
#                 dp[left] = height
#                 print("new dp:", dp)
#         return len(dp)


class Solution:
    def maxEnvelopes(self, envelopes):
        if not envelopes: return 0
        envelopes.sort(key=lambda x: (x[0], -x[
            1]))  # this is super important! width is up order, when width is the same , heigh is in down order!!! Then we only need to perform LIS on the height-dimension!
        # print(envelopes)
        tailsh = [0] * len(envelopes)
        size = 0

        for wh in envelopes:
            i, j = 0, size
            while i != j:
                # only seek height's LIS (longest increasing subsequence), alike Leetcode Question 300.
                # https://leetcode.com/problems/longest-increasing-subsequence/
                m = (i + j) // 2
                if tailsh[m] < wh[1]:
                    i = m + 1
                else:
                    j = m
            tailsh[i] = wh[1]

            size = max(size, i + 1)
        return size


soln = Solution()
# print(soln.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))
print(soln.maxEnvelopes([[2,3], [5,4], [6,4], [6,7], [1,2]]))
print(soln.maxEnvelopes([[1, 1], [1, 1]]))
print(soln.maxEnvelopes([[0, 0], [0, 0]]))
