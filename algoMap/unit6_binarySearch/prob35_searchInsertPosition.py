# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4


from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        L = 0
        R = N - 1
        
        while L <= R:
            M = L + ((R-L) // 2)
            if nums[M] == target:
                return M
            elif nums[M] < target:
                L = M + 1
            else:
                R = M - 1
        
        return L
    
nums = [1,3,5,6]
target = 7

print(Solution().searchInsert(nums, target))