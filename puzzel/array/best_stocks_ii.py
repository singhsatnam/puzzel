class Solution:
    def get_max_profit(self, arr: list[int]) -> int:
        i = 1
        profit = 0
        while i < len(arr):
            if arr[i] > arr[i - 1]:
                profit = profit + arr[i] - arr[i - 1]
            i = i + 1
        return profit

soln = Solution()
soln.get_max_profit([7, 1, 5, 3, 6, 4])
