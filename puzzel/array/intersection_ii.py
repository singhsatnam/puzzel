class Solution:
    def get_intersection(self, arr1, arr2):
        map1 = self.counts_constructor(arr1, {})
        map2 = self.counts_constructor(arr2, {})
        intersection = {}

        map1 = 

        for k, v in map1.items():
            if k in map2:
                map2_count = map2[k]
                intersection[k] = min(v, map2_count)

        return self.make_array(intersection)

    def counts_constructor(self, arr, map: dict) -> dict:

        for ele in arr:
            map[ele] = 0
        return map

    def make_array(self, map: dict) -> list:
        print(map)
        list = []
        for k, v in map.items():
            list.append([k] * v)

soln = Solution()
res = soln.get_intersection([2, 2, 3, 4], [2, 3, 4, 1])
print(res)
