class Solution:
    def get_lenght_of_longest_unique_substring(self, string) -> int:
        if string is None:
            return 0
        seen_before = set()
        max_unique_length = 0
        for char in string:
            print(char)
            if char in seen_before:
                return max_unique_length
            seen_before.add(char)
            max_unique_length += 1

        return max_unique_length


soln = Solution()
print(soln.get_lenght_of_longest_unique_substring("abcabcbb"))
