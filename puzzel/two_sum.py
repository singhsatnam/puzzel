class Solution:
    def get_compliment(self, sum, arr) -> []:
        dic = {}
        for i, num in enumerate(arr):
            if num in dic:
                return [dic[num], i]
            else:
                dic[sum - num] = i


assert Solution().get_compliment(9, [2, 7, 11, 15]) == [0, 1]
