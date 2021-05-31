from typing import List


class Solution:
    def maxSubArray(self, nums):
        dp = [0] * len(nums)

        for i, num in enumerate(nums):
            dp[i] = max(dp[i - 1] + num, num)
        return max(dp)

    def maxSubArray1(self, nums):
        max_sum_until_i = max_sum = nums[0]
        for i, num in enumerate(nums[1:], start=1):
            max_sum_until_i = max(max_sum_until_i + num, num)
            max_sum = max(max_sum, max_sum_until_i, max_sum)
        return max_sum


soln = Solution()
print(soln.maxSubArray1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
