from typing import List


class Solution:
    def get_direction(self, cmd: str) -> (int, int):
        directions_dic = {
            'RIGHT': (0, 1),
            'DOWN': (1, 0),
            'LEFT': (0, -1),
            'UP': (-1, 0)
        }

        return directions_dic[cmd]

    def get_new_pos(self, index: (int, int), direction: (int, int), n):
        new_pos = (index[0] + direction[0], index[1] + direction[1])
        if new_pos[0] < 0 or new_pos[0] > n - 1 or new_pos[1] < 0 or new_pos[0] > n - 1:
            return index
        return new_pos

    def get_cell_from_index(self, index: (int, int), n):
        return (index[0] * n) + index[1]

    def get_rover_position(self, n: int, cmds: List[str]):
        cur_pos = (0, 0)
        for ele in cmds:
            direction = self.get_direction(ele)
            cur_pos = self.get_new_pos(cur_pos, direction, n)
            print(self.get_cell_from_index(cur_pos, n))

        return self.get_cell_from_index(cur_pos, n)


soln = Solution()
print(soln.get_rover_position(n=4, cmds=['RIGHT', 'DOWN', 'LEFT', 'LEFT', 'DOWN']))
