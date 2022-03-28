class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest = 0
        for i in range(len(s)):
            left = s[i]
            for j in range(i, len(s)):
                if self.isUnique(s, i, j):
                    print("*** update longest to ",j-i)
                    longest = max(longest, j-i)
        return longest
    
    def isUnique(self, s, low, high):
        print(s[low:high])
        seen = set()
        for i in range(low, high):
            c = s[i]
            if c in seen:
                return False
            else:
                seen.add(c)
        return True

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            j = i
            seen = set()
            while j < len(s) and s[j] not in seen:
                seen.add(s[j])
                j = j + 1
            longest = max(longest, j - i)
        return longest

class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            print(ans)
            mp[s[j]] = j + 1
            print(mp)

        return ans

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res


soln = Solution()
print("abcabcbb")
print(soln.lengthOfLongestSubstring("abcabcbb"))
print("pwwkew")
print(soln.lengthOfLongestSubstring("pwwkew"))
