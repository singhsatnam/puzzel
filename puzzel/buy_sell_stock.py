import sys


class Solution:
    def maxProfit(self, prices):
        minprice = float("inf")
        maxprofit = 0
        for i in range(len(prices)):
            if (prices[i] < minprice):
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([2, 6, 1]))
