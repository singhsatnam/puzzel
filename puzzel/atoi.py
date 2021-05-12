class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        s = s.lstrip()
        end = len(s)
        for i in range(1, len(s)):  # Ignore the first character.
            if not s[i].isdigit():
                end = i
                break
        try:
            num = int(s[0:end])  # Error if first character was invalid.
            return min(max(-2 ** 31, num), 2 ** 31 - 1)
        except ValueError:
            return 0


soln = Solution()
assert soln.myAtoi("16") == 16
assert soln.myAtoi("-16") == -16
assert soln.myAtoi(" -32") == -32
