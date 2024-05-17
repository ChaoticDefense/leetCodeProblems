class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for num1 in nums:
            for num2 in nums:
                if num1 != num2 and num1 + num2 == target:
                    return [num1, num2]

        return [num1, num2]

s = Solution()
print(s.twoSum([2,7,11,15], 9))