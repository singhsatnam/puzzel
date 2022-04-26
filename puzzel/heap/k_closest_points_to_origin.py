import math
import heapq
points = [[3,3],[5,-1],[-2,4]]
k = 2

def kClosest(points, k):
    arr = []
    heapq.heapify(arr)
    for ele in points:
        curr_dist = get_euclidean_distance(ele[0], ele[1])
        heapq.heappush(arr, (curr_dist, ele))
    # print([heapq.heappop(arr) for i in range(len(arr))])
    return heapq.nsmallest(k, arr)

def bin_search(points, k):
    dist = [get_euclidean_distance(ele[0], ele[1]) for ele in points]
    print(dist)
    low = 0
    high = max(dist)
    closest = []
    indexi = [i for i in range(0, len(dist))]
    print(indexi)

    print("start")
    while k>0:
        mid = (high+low)/2
        print(mid)
        less, more = split_dist(indexi, dist, mid)
        print(less, more)
        if k > len(less):
            k = k-1
            closest.extend(less)
            low = min(more)
        else:
            return less
        print(closest)



def split_dist(indexi, dist, mid):
    less = []
    more = []
    for i, num in dist:
        if num > mid:
            more.append(i)
        else:
            less.append(i)
    return less, more

def get_euclidean_distance(x, y) -> float:
    x1 = 0
    y1 = 0
    return math.sqrt(math.pow((x-x1), 2) + math.pow((y-y1), 2))

res = bin_search(points, k)
print("res ", res)