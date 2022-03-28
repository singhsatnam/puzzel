class Solution:
    def routePairs(maxTravelDist, forwardRouteList, returnRouteList):
        res = []
        maxdis = 0
        s1, s2 = 0, 0
        for i in forwardRouteList:
            for j in returnRouteList:
                if i[1] + j[1] == maxTravelDist:
                    res.append([i[0], j[0]])
                else:
                    if i[1] + j[1] > maxdis and i[1] + j[1] < maxTravelDist:
                        s1, s2 = i[0], j[0]
                        maxdis = i[1] + j[1]
        if len(res) == 0:
            res.append([s1, s2])
        return res


x = Solution
print(x.routePairs(10000, [[1, 3000], [2, 5000], [3, 7000], [4, 10000]], [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]))
