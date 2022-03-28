class Solution():
    def remove_duplicates(self, nums: list[int]) -> int:
        unique_pos = 0
        i = 1
        # move i if same num
        # increment up and copy i id num is different

        print(nums)
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                unique_pos = unique_pos + 1
                nums[unique_pos] = nums[i]
            i = i + 1

        return unique_pos + 1





soln = Solution()
soln.remove_duplicates([1, 1, 2])