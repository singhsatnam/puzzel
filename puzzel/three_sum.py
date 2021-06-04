from typing import List


class Solution:
    def binarySearch(self, nums, min, max, target):
        while True:
            if max < min:
                return min
            mid = (min + max) // 2
            if nums[mid] < target:
                min = mid + 1
            elif nums[mid] > target:
                max = mid - 1
            else:
                return mid

    def threeSum(self, nums):
        nums = sorted(nums)
        n = len(nums)
        result = set()
        i = 0
        while i < n - 2:
            j = self.binarySearch(nums, i + 1, n - 2, -(nums[i] + nums[-1]))
            k = self.binarySearch(nums, j + 1, n - 1, -(nums[i] + nums[j]))
            while j < k and k < n:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    result.add(tuple(sorted((nums[i], nums[j], nums[k]))))
                    k -= 1
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
            if nums[i] == 0:
                break
            i += 1
        print(result)
        return result

    def get_three_sum(self, nums: List[int]) -> List[List[int]]:
        print("nums=", nums)
        if not nums: return []
        nums.sort()
        print("sorted nums=", nums)
        ans = []
        for i in range(len(nums) - 2):

            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                print("i=", i, " nums[i]=", nums[i], " nums[i-1]=", nums[i - 1])
                low = i + 1
                high = len(nums) - 1
                target = 0 - nums[i]
                print("low, high, target=", low, " ", high, " ", target)
                while low < high:
                    if nums[low] + nums[high] == target:
                        ans.append([nums[i], nums[low], nums[high]])
                    if nums[low] + nums[high] > target:
                        high -= 1
                    else:
                        low += 1
        print("ans= ", ans)
        print(ans.sort())

        return []


solution = Solution()
solution.get_three_sum([-1, 0, 1, 2, -1, -4])
