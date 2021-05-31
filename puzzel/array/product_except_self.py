from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        lmult = 1
        rmult = 1
        for i in range(len(nums)):
            res[i] = lmult
            lmult *= nums[i]

        print(res)
        for i in range(0, len(nums)):
            index = len(nums) - i - 1
            res[index] = res[index] * rmult
            rmult *= nums[index]

        print(res)
        return res


soln = Solution()
soln.productExceptSelf([1, 2, 3, 4])
