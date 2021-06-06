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
            for ele_b in sorted_b:
                cur_sum = ele_a[1] + ele_b[1]
                if best < cur_sum <= target:
                     res.append([ele_a[0], ele_b[0]])

        return res


soln = Solution()
print(soln.get_valuesclosest_to_target([[1, 6], [2, 2], [3, 4]], [[1, 2]], 7))
