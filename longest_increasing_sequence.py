from typing import List


class Solution:
    def lengthOfLIS(self, nums):

        def binarySearch(sub, val):
            lo, hi = 0, len(sub) - 1
            while (lo <= hi):
                mid = lo + (hi - lo) // 2
                if sub[mid] < val:
                    lo = mid + 1
                elif val < sub[mid]:
                    hi = mid - 1
                else:
                    return mid
            return lo

        sub = []
        for val in nums:
            pos = binarySearch(sub, val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        print(sub)
        return len(sub)
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     print("input=", nums)
    #     if not nums:
    #         return 0
    #
    #     n = len(nums)
    #     dp = [1] * n
    #
    #     for i in range(1, n):
    #         for j in range(i):
    #             print("i=", i, " j=", j)
    #             if nums[i] > nums[j]:
    #                 print("dp=", dp)
    #                 dp[i] = max(dp[i], 1 + dp[j])
    #                 print("Updated dp=", dp)
    #
    #     return max(dp)


soln = Solution()
print(soln.lengthOfLIS([3, 2, 5, 1, 2, 6, 8, 7]))
