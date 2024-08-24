# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

#     [4,5,6,7,0,1,2] if it was rotated 4 times.
#     [0,1,2,4,5,6,7] if it was rotated 7 times.

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
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
        return nums[L]
    
# nums = [4,5,6,7,0,1,2]
# nums = [11, 13, 15, 17]
nums = [3,4,5,1,2]
print(Solution().findMin(nums))