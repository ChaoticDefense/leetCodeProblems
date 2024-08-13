# See learning/binarySearch.py for explanation
class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1

        return -1


nums = [1, 2, 4, 7, 10, 39, 78, 96]
target = 39
print(Solution().search(nums, target))