from typing import List
import collections


class Solution:
    def get_count_of_mutations(self, starting_grid: List[List[int]]) -> int:
        for ele in starting_grid:
            print(ele)
        count_row = len(starting_grid)
        count_column = len(starting_grid[0])
        q = collections.deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count_normal = 0
        minutes = 0

        for i in range(count_row):
            for j in range(count_column):
                if starting_grid[i][j] == 1:
                    count_normal += 1
                elif starting_grid[i][j] == 2:
                    q.append((i, j, 0))

        while q:
            cur_i, cur_j, minutes = q.popleft()
            for di, dj in directions:
                new_i = cur_i + di
                new_j = cur_j + dj
                if 0 <= new_i < count_row and 0 <= new_j < count_column and starting_grid[new_i][new_j] == 1:
                    count_normal -= 1
                    starting_grid[new_i][new_j] = 2
                    q.append((new_i, new_j, minutes + 1))

        return minutes if count_normal == 0 else 1


solution = Solution()
assert solution.get_count_of_mutations([[2, 1, 0], [0, 0, 2], [1, 1, 1]]) == 3

A  | B
10   10
14   12
16   15