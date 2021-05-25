class Solution:
    def get_num_islands(self, grid):
        if grid:
            count_island = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == "1":
                        self.dfs(grid, i, j)
                        count_island += 1
            return count_island

        return 0

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "0"
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
soln = Solution()
print(soln.get_num_islands(grid))
