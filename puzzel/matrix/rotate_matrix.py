class Solution:
    def rotate(self, A):
        n = len(A)
        for i in range(n):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        for row in A:
            for j in range(n // 2):
                row[j], row[~j] = row[~j], row[j]


soln = Solution()
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soln.rotate(grid)
for ele in grid:
    print(ele)
