from bisect import bisect_left


class Solution:
    def min_box_count(self, arr: list[int]) -> int:
        size = 0
        arr = sorted(arr)
        print(arr)
        count = 0
        contains = [0] * len(arr)
        print(contains)
        for i, ele in enumerate(arr):
            print(contains)
            lo = i + 1
            hi = len(arr)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if arr[mid] < arr[i] * 2:
                    lo = mid + 1
                else:
                    hi = mid
            print("lo:", lo, " hi:", hi)
            while hi < len(arr) and contains[hi]:
                hi += 1
            if hi == len(arr):
                break

            if hi < len(arr):
                contains[i] = True
                count += 1
        return len(arr) - count


soln = Solution()
print(soln.min_box_count([8, 9, 1, 6, 2, 6, 5, 8, 3]))
