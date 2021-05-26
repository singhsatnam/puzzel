class Solution():
    def gameOfLife(self, board):
        if not board or len(board[0]) == 0:
            return

        m, n = len(board), len(board[0])
        for i, row in enumerate(board):
            for j, ele in enumerate(row):
                count = 0
                for a in range(max(0, i - 1), min(i + 2, m)):
                    for b in range(max(0, j - 1), min(j + 2, n)):
                        if (a, b) != (i, j) and 1 <= board[a][b] <= 2:
                            count += 1
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 3
                else:
                    if count < 2 or count > 3:
                        board[i][j] = 2
        print(board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
        return board


soln = Solution()
grid = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print(soln.gameOfLife(grid))
