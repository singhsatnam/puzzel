def pathMaxScore(m):
    startVal = m[0][0]
    startCoor = (0, 0)
    stack = [(startVal, startCoor, [])]  # [] bcuz problem says path should exlude start and end
    dirs = [(1, 0), (0, 1)]  # only right and down are allowed
    maxScore = 0
    while stack:
        node, coor, path = stack.pop()
        x, y = coor

        # check if leaf node (aka the mth, nth cell) is reached
        if x == len(m) - 1 and y == len(m[0]) - 1:
            maxScore = max(maxScore, min(path[:-1]))  # path[:-1] bcuz problem says exclude end
            # count += 1

        for dir in dirs:
            newX, newY = x + dir[0], y + dir[1]
            # within bounds:
            if newX >= 0 and newX <= len(m) - 1 and newY >= 0 and newY <= len(m[0]) - 1:
                stack.append((m[newX][newY], (newX, newY), path + [m[newX][newY]]))

    return maxScore

print(pathMaxScore([[1, 2, 3],
 [4, 5, 1]]))
print(pathMaxScore([[5, 1],
 [4, 5]]))

