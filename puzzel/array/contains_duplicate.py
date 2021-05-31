class Solution:
    def contains_duplicate(self, arr):
        arr_set = set()
        for ele in arr:
            if ele in arr_set:
                return True
            else:
                arr_set.add(ele)
        return False


solution = Solution()
arr = [1, 2, 3, 1]
assert solution.contains_duplicate(arr) is True
assert solution.contains_duplicate([1, 2, 3]) is False
