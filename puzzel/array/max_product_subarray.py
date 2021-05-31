from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = prev_max = prev_min = nums[0]
        for num in nums[1:]:
            curr_min = min(prev_max * num, prev_min * num, num)
            curr_max = max(prev_max * num, prev_min * num, num)
            global_max = max(global_max, curr_max)
            prev_max = curr_max
            prev_min = curr_min
        return global_max


soln = Solution()
print(soln.maxProduct([2, 3, -2, 4]))
print(soln.maxProduct([-2, 0, -1]))
