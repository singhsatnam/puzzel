class Solution(object):
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret

    def dfs(self, nums, target, path, ret):
        print("received-", "nums:", nums, " target:", target, " path:", path, " ret:", ret)
        if target < 0:
            print("return fail")
            print()
            return
        if target == 0:
            ret.append(path)
            print("return success")
            print()
            return
        for i in range(len(nums)):
            print("i=", i)
            print("sent-", "nums:", nums[i:], " target(", target, "-", nums[i], "):", target - nums[i], " path:",
                  path + [nums[i]], " ret:", ret)
            print()
            self.dfs(nums[i:], target - nums[i], path + [nums[i]], ret)


soln = Solution()
print(soln.combinationSum([2, 3, 5], 8))
