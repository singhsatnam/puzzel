from typing import List


class Solution:
    def get_distinct(self, nums: List[int]) -> int:
        length = 0
        if len(nums) == 0 : return True
        for i in range(1, len(nums)):
            if nums[length] != nums[i]:
                length += 1
                nums[length] = nums[i]
        print(nums)
        return length + 1


arr = [1, 2, 2, 3, 4, 4, 4]
solution = Solution()
print(solution.get_distinct(arr))