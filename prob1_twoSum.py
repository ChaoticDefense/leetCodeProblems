class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums):
                if idx1 != idx2 and num1 + num2 == target:
                    return [idx1, idx2]

        return [num1, num2]

s = Solution()
print(s.twoSum([3,3], 6))