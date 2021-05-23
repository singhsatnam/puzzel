class Solution:
    def canCross(self, stones):
        if stones[1] != 1:
            return False
        next_possible_stone_map = {x: set() for x in stones}

        next_possible_stone_map[1].add(1)
        print(next_possible_stone_map)
        for curr_stone in stones[:-1]:
            print()
            print(curr_stone)
            for j in next_possible_stone_map[curr_stone]:
                print("j: ", j, end="")
                for k in range(j - 1, j + 2):
                    if k > 0 and curr_stone + k in next_possible_stone_map:
                        next_possible_stone_map[curr_stone + k].add(k)
        return bool(next_possible_stone_map[stones[-1]])


soln = Solution()
soln.canCross([0, 1, 3, 5, 6, 8, 12, 17])
