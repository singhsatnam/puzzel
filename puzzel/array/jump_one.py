class Solution:
    def can_reach(self, nums, pos) -> bool:
        print("pos ", pos)
        if pos == len(nums) - 1:
            return True
        print("for i in range 1, ", nums[pos])
        for i in range(1, nums[pos]):
            print("calling can_reach(nums, ", pos + i, ")")
            self.can_reach(nums, pos + i)
        return False

soln = Solution()
print([2,3,1,1,4])
print(soln.can_reach([2,3,1,1,4], 0))
