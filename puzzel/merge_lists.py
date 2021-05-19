from typing import List


# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#
#         intervals.sort(key=lambda x: x[0])
#
#         merged = []
#         for interval in intervals:
#             if not merged or merged[-1][1] < interval[0]:
#                 merged.append(interval)
#             else:
#                 merged[-1][1] = max(merged[-1][1], interval[1])
#
#         return merged


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        print(sorted_intervals)
        merged_lists = []
        first = sorted_intervals[0][0]
        second = 0
        i = 1
        while i < len(sorted_intervals):
            print(i)
            if sorted_intervals[i - 1][1] >= sorted_intervals[i][0]:
                print("if", sorted_intervals[i - 1][1], ">=", sorted_intervals[i][0])
            else:
                second = sorted_intervals[i - 1][1]
                merged_lists.append([first, second])
                first = sorted_intervals[i][0]
            if i == len(sorted_intervals) - 1:
                merged_lists.append([first, sorted_intervals[i][1]])
            i = i + 1
        print(merged_lists)


soln = Solution()
# soln.merge([[15, 18], [2, 6], [8, 10], [1, 3]])
soln.merge([[1, 4], [4, 5]])
