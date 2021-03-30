class Solution:
    def contains_positive_and_negative(self, arr) -> int:
        # O(1) for inserting in set and O(n) for iterating over arr
        s = set(-a for a in arr if a < 0) & set(a for a in arr if a > 0)
        return max(s) if s else 0


assert Solution().contains_positive_and_negative([3, 2, -2, 5, -3]) == 3
assert Solution().contains_positive_and_negative([-3, -3]) == 0
