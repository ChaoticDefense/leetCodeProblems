# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:


# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Get length of nums
        n = len(nums)
        
        # Init output
        longest = 0
        
        l = 0
        
        # Keep track of number zeros in window
        num_zeros = 0
        
        # loop over array
        for r in range(n):
            # Keep track of number of zero
            if nums[r] == 0:
                num_zeros += 1
             
            # Invalid condition: number of zeros greater than number allowed
            # Keep moving l until window is valid   
            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            
            # Window size, compare to longest valid window    
            w = r - l + 1
            longest = max(longest, w)
        
        
        return longest
   
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print(Solution().longestOnes(nums,k))