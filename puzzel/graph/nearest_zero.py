def updateMatrix(matrix: list[list[int]]) -> list[list[int]]:
    # BFS helper #
    def bfs(node):
        from collections import deque
        q = deque()
        i, j = node
        q.append(((i, j), 0))  # d (dist to a zero) = 0 initially
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for i in range(len(q)):
                coor, d = q.popleft()
                x, y = coor
                # if a zero nei is found
                if matrix[x][y] == 0:
                    return d
                visited.add(coor)
                # investigate neighbours
                for dir in dirs:
                    newX, newY = x + dir[0], y + dir[1]
                    # within bounds:
                    if 0 <= newX <= len(matrix) - 1 and 0 <= newY <= len(matrix[0]) - 1:
                        # not seen:
                        if (newX, newY) not in visited:
                            q.append(((newX, newY), d + 1))
        return -1

        # main logic #
        '''
        steps:
            - itertate over matrix to find cells = 1
            - pass cells equaling 1 to a bfs to find the closest 0 to them
            - update matrix
        '''

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                d = bfs((i, j))  # d = closest dist to a 0
                matrix[i][j] = d  # update M with d
    return matrix


def bfs_optimized(matrix):
    visited = set()
    from collections import deque
    q = deque()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                visited.add((i, j))
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for dirr in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newX, newY = x + dirr[0], y + dirr[1]
            if 0 <= newX <= len(matrix) - 1 and 0 <= newY <= len(matrix[0]) - 1 and (newX, newY) not in visited:
                matrix[newX][newY] = matrix[x][y] + 1
                visited.add((newX, newY))
                q.append((newX, newY))
    return matrix


mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
# bfs_optimized(matrix=mat)
print(updateMatrix(matrix=mat))
