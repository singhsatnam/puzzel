from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):

        if not obstacleGrid:
            return
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        print(obstacleGrid)
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        print(obstacleGrid)
        for i in range(1, r):
            obstacleGrid[i][0] = obstacleGrid[i - 1][0] * (1 - obstacleGrid[i][0])
        print(obstacleGrid)
        for i in range(1, c):
            obstacleGrid[0][i] = obstacleGrid[0][i - 1] * (1 - obstacleGrid[0][i])
        print(obstacleGrid)
        for i in range(1, r):
            for j in range(1, c):
                obstacleGrid[i][j] = (obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]) * (1 - obstacleGrid[i][j])
        print(obstacleGrid)
        return obstacleGrid[-1][-1]


sol = Solution()
res = sol.uniquePathsWithObstacles(
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ])

print(res)

# def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#     width = len(obstacleGrid)
#     dp = [None] * width
#     print(dp)
#     dp[0] = 1
#     print(dp)
#     for row in obstacleGrid:
#         for j in range(width):
#             print("j= ", j)
#             if row[j] == 1:
#                 dp[j] = 0
#                 print("row of j==1 ", j, dp)
#             elif j > 1:
#                 dp[j] = dp[j] + dp[j - 1]
#                 print("row of j>1 ", j, dp)
#     print(dp)
#     return dp[width - 1]
