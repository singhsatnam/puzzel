from typing import List


class Solution:
    # DFS
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            print("not nums", nums)
            res.append(path)
            # return # backtracking
        print("nums:", nums, " path:", path)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


soln = Solution()
nums = [1, 2, 3, 4, 5]
print(soln.permute(nums))