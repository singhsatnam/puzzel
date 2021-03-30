class Solution:
    def get_min_deletions(self, string: str) -> int:
        from collections import Counter
        count_dict = Counter(string)
        count = 0
        accounted = set()
        for frequency in count_dict.values():
            while frequency in accounted:
                count += 1
                frequency -= 1
            if frequency != 0:
                accounted.add(frequency)
        return count


print(Solution().get_min_deletions("aaabbbcccddeef"))
