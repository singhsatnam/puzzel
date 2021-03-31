def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
    def createSet(grid, targetVal):
        result = set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == targetVal:
                    result.add((x, y))
        return result

    rotten = createSet(grid, 2)
    fresh = createSet(grid, 1)

    time = 0
    while len(fresh) > 0:
        turned = set()
        for x, y in fresh:
            if (x + 1, y) in rotten or (x - 1, y) in rotten or (x, y + 1) in rotten or (x, y - 1) in rotten:
                turned.add((x, y))
        # print(time, rotten, fresh, turned)
        if len(turned) == 0:
            return -1
        fresh.difference_update(turned)
        rotten.update(turned)
        time += 1

    return time