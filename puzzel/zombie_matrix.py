def minHour(self, grid: List[List[int]]) -> int:
    if not grid:
        # not sure if this needs to be a zero but I would put -1 since it's technically an invalid input while
        # 0 hours is a valid descriptive length of time, as something can take 0 hours to do, but not -1 hours to do.
        return(-1)

    width, height = len(grid[0]), len(grid)
    q = collections.deque([])
    hours = -1    # this accounts for the first run. If there are no zombies
                       # to start we can return -1 since counting the hours to turn
                       # zero people is unusual, it didn't take 0 hours to do because nothing
                       # is really being timed.

    # sets up the initial run. Queues the first zombies to start the
    # zombification process
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                q.appendleft((i, j))

    # If q is empty because there are no zombies in the given 2d array
    # we skip this and just return the hours which would be -1
    # for the same reason listed above at the initialization of hours
    while q:
        # this will go through each hour separately, work with all the current zombies
        # and then stage the next zombies before adding to hours after the for loop finishes
        for _ in range(len(q)):
            i, j = q.pop()
            for h, w in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= w < width and 0 <= h < height and grid[h][w] == 0:
                    grid[h][w] = 1
                    q.appendleft((h, w))
        hours += 1

    return(hours)