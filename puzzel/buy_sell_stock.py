from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        l = 0
        r = size - 1
        max = 0
        while (l != r):
            print("l: ", l, " r: ", r)
            cur = prices[r] - prices[l]
            print("curPrice:", cur)
            print("l-r: ", cur)
            max = max if max > cur else cur
            print(max)
            if (prices[l] > prices[r]):
                print("more")
                l += 1
            else:
                print("less")
                r -= 1
        print("Final max: ", max)
        return max


solution = Solution()
solution.maxProfit([7, 1, 5, 3, 6, 4])