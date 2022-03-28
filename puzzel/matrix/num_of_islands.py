from typing import List


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

class Solution2:
    def get_num_islands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        count_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    print("sending for ", i, j)
                    self.dfs(grid, i, j)
                    self.print_array(grid)
                    count_islands += 1

        return count_islands

    def print_array(self, grid):
        if grid:
            for ele in grid:
                print(ele)

    def dfs(self, grid: List[List[str]], i: int, j: int):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "0"
        for ele in directions:
            self.dfs(grid, i + ele[0], j + ele[1])
        print("covered all directions for ", i, j)

soln = Solution2()
print(soln.get_num_islands(grid))
