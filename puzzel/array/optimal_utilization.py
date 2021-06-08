from typing import List


class Solution:
    def get_valuesclosest_to_target(self, seq_a: List[List[int]],
                                    seq_b: List[List[int]],
                                    target: int) -> List[List[int]]:
        sorted_a = sorted(seq_a, key=lambda x: x[1])
        sorted_b = sorted(seq_b, key=lambda x: x[1])
        best = 0
        res = []
        for ele_a in sorted_a:
            print()
            print("ele a:", ele_a)
            for ele_b in sorted_b:
                print("ele b:", ele_b)
                cur_sum = ele_a[1] + ele_b[1]
                print(cur_sum, ele_a[0], ele_b[0])
                if cur_sum <= target:
                    if cur_sum > best:
                        best = cur_sum
                        res = []
                        res.append([ele_a[0], ele_b[0]])
                    elif cur_sum == best:
                        res.append([ele_a[0], ele_b[0]])

        return res


soln = Solution()
print(soln.get_valuesclosest_to_target([[1, 3], [2, 5], [3, 7], [4, 10]],
                                       [[1, 2], [2, 3], [3, 4], [4, 5]],
                                       10))
