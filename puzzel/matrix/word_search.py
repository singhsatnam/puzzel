class Solution:
    def does_word_exist(self, grid, word):
        if grid is None or word is None:
            return False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp = self.dfs(grid, word, 0, i, j)
                print()
                if (temp):
                    print("hobbit ")
                    return True

        return False

    def dfs(self, grid, word, curr_pos, i, j):
        print("making dfs for ", word[curr_pos], "at pos ", i, j)
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        if i < 0 or i >= len(grid) or j < 0 or j > len(grid[0]) or grid[i][j] != word[curr_pos]:
            print("returning false at ", word[curr_pos])
            return False
        if curr_pos == len(word) - 1:
            print("returning True")
            return True
        temp = self.dfs(grid, word, curr_pos + 1, i, j + 1) or \
               self.dfs(grid, word, curr_pos + 1, i, j - 1) or \
               self.dfs(grid, word, curr_pos + 1, i + 1, j) or \
               self.dfs(grid, word, curr_pos + 1, i - 1, j)
        return temp


soln = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
for ele in board:
    print(ele)
word = "ABCCEDS"
print(soln.does_word_exist(board, word))
