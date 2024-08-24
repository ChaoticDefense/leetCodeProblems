# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:

# Input: nums = [1], target = 0
# Output: -1

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        L = 0
        R = N - 1
        
        # Binary Search, stopping as soon as L = R
        # Basically conditional binary search
        while L < R:
            M = L + ((R-L) // 2)
            # Finding pivot point, where interval increases, 
            # then decreases only once, then increases again
            if nums[M] > nums[R]: # Condition for conditional BS
                L = M + 1 # All nums to the left of M will be bigger than R
            else:
                R = M # M may be pivot point (minimum) so do not want 
                      # to exclude it next time
        
        # Above code is just to find min_idx, now we can find search intervals
        min_idx = L
        
        # Edge case where min_idx is at begininning, do normal BS
        if min_idx == 0:
            L , R = 0, N - 1
        # Target is in interval left of min_idx
        elif target >= nums[0] and target <= nums[min_idx - 1]:
            L, R = 0, min_idx - 1
        # Target is in interval from min_idx to end
        else:
            L, R = min_idx, N - 1
        
        # Normal BS over L and R range
        while L <= R:
            M = L + ((R-L) // 2)
            if nums[M] == target:
                return M
            elif nums[M] < target:
                L = M + 1
            else:
                R = M - 1
        
        return -1
    
nums = [4,5,6,7,0,1,2]
target = 0

print(Solution().search(nums,target))