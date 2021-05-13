class Solution:
    def print_2d(self, arr):
        for i in range(len(arr)):
            print(arr[i])

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        print("text1: ", text1)
        print("text2: ", text2)

        dp = [[0 for i in range(n + 1)] for i in range(m + 1)]
        print("dp:", dp)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                print("i, j=", i, j)
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    print(text1[i - 1], text2[j - 1], "// updated dp on match: ")
                    self.print_2d(dp)
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )
                    print(text1[i - 1], text2[j - 1], "// updated dp on no match:")
                    self.print_2d(dp)

        return dp[m][n]


soln = Solution()
print("result: ", soln.longestCommonSubsequence("abcd", "aabceabcdff"))
