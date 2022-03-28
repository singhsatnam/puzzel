class Solution:
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = self.make_array(n, m)
        self.print2(dp)

        for i in range(n):
            for j in range(m):
                print("considering ", i, " ", j)
                if text1[i] == text2[j]:
                    print(text1[i], " match ", text2[j])
                    self.print2(dp)
                    print("changing pos ", i + 1, " ", j + 1)
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    self.print2(dp)
                else:
                    print(text1[i], " do not match ", text2[j])
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
                    self.print2(dp)
        return dp[-1][-1]

    def make_array(self, len_one, len_two) -> list:
        temp = [([0] * (len_two + 1))] * (len_one + 1)
        temp2 = [[0] * (len_two + 1) for _ in range(len_one + 1)]
        return temp

    def print2(self, mat):
        print(mat)


soln = Solution()
res = soln.longest_common_subsequence("abcde", "act")
print(res)
