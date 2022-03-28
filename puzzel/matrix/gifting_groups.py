from typing import List


def get_matrix_from_string_list(str_list):
    grid = []
    for i, ele in enumerate(str_list):
        grid.append([int(char) for char in ele])
    return grid

#
# def dfs(idx, length, matrix):
#     if matrix[idx][idx] == 0:
#         return
#     for i in range(length):
#         if matrix[idx][i] == 1:
#             matrix[idx][i] = 0
#             dfs(i, length, matrix)
#
#
# def countGroups(related):
#     grid = get_matrix_from_string_list(related)
#     for ele in grid:
#         print(ele)
#
#     count = 0
#     length = len(related)
#     for indx in range(length):
#         if related[indx][indx] == 1:
#             count += 1
#             dfs(indx, length, related)
#     return count
#
#
# def findCircleNum(related):
#     grid = get_matrix_from_string_list(related)
#     visited = set()
#
#     def dfs(node):
#         print("grid[i] = ", grid[i])
#         for neighbour, adj in enumerate(grid[node]):
#             print(neighbour, adj)
#
#             if adj and neighbour not in visited:
#                 visited.add(neighbour)
#                 dfs(neighbour)
#
#     group_count = 0
#     for i in range(len(grid)):
#         print("for row:", i)
#         if i not in visited:
#             dfs(i)
#             group_count += 1
#     return group_count


def findCircleNum2(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    grid_len = len(grid)
    visited = [False] * grid_len

    def dfs(i):
        for j in range(grid_len):
            if grid[i][j] == 1 and not visited[j]:
                visited[j] = True
                dfs(j)

    group_count = 0
    for i in range(grid_len):
        print("i", i)
        if not visited[i]:
            # Increment count for each unvisited person (and his group) and mark them visited
            group_count += 1
            visited[i] = True
            # Use dfs to mark his relations/group visited
            dfs(i)

    return group_count


print(findCircleNum2(get_matrix_from_string_list(['1100', '1110', '0110', '0001'])))
