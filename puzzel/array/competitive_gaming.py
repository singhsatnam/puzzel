class Solution():
    def get_count_of_players_who_can_upgrade(self, n, k, scores) -> int:
        state = [0] * 101
        for ele in scores:
            state[ele] = state[ele] + 1
        print("hllo")
        cur_rank = 0
        res = 0
        for i in range(len(state) - 1, 0, -1):
            if state[i] != 0:
                cur_rank += state[i]
                print(i, " value ", state[i], " ", cur_rank)
            if cur_rank >= k:
                print(i, " returning ", state[i], " ", cur_rank)
                return cur_rank



soln = Solution()
res = soln.get_count_of_players_who_can_upgrade(12, 7, [10, 9, 9, 9, 9, 5, 5, 2, 2, 2, 1, 1])
print("res=", res)
