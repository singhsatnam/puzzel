a = [[1,3],[2,6],[8,10],[15,18]]
# print(sorted(a, key=lambda x: x[0]))


def merge(intervals):
    if len(intervals) == 0: return []
    intervals = sorted(intervals, key=lambda x: x[0])
    res = [intervals[0]]
    print("res: ", res)
    for n in intervals[1:]:
        print("present n: ", n)
        print("res of last: ", res[-1][1])
        if n[0] <= res[-1][1]:
            res[-1][1] = max(n[1], res[-1][1])
        else:
            res.append(n)
    return res


print(merge(a))
