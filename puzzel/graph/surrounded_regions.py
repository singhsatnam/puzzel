class Solution:

    def dfs(self, matrix, i, j):
        if i == 0 or j == 0 or i == len(matrix) or j == len(matrix) or matrix[i][j] == 'X':
            return matrix

        # Working with cell which is not boundary and a candidate for capturing
        matrix[i][j] = 'X' # masking 0 cell
        temp = self.dfs(matrix, i + 1, j)
        self.dfs(matrix, i - 1, j)
        self.dfs(matrix, i, j + 1)
        self.dfs(matrix, i, j - 1)

        # traverse from the boders, make connected 0 nodes .
        # traverse from anywhere, if encounter boder on a 0 node, make everyone . Use stack to keep track of the connected nodes


    def main(self, matrix):
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix = self.dfs(matrix, i, j)



soln = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
soln.main(board)