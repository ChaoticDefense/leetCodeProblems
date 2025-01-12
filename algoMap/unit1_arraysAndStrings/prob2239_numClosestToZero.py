# Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

 

# Example 1:

# Input: nums = [-4,-2,1,4,8]
# Output: 1
# Explanation:
# The distance from -4 to 0 is |-4| = 4.
# The distance from -2 to 0 is |-2| = 2.
# The distance from 1 to 0 is |1| = 1.
# The distance from 4 to 0 is |4| = 4.
# The distance from 8 to 0 is |8| = 8.
# Thus, the closest number to 0 in the array is 1.

# Example 2:

# Input: nums = [2,-1,1]
# Output: 1
# Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.

from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # First set output to first num in array
        closest = nums[0]
        
        # Loop over each number in nums
        for num in nums:
            # If dist to 0 at num is less than current closest val
            # set closest to current num
            if abs(num) < abs(closest):
                closest = num
            # Special case where current distance is same as distance at num
            # Set closest to be larger of two values
            elif abs(num) == abs(closest):
                closest = max(num, closest)

        return closest
    
# nums = [-4,-2,1,4,8]
nums = [2,-1,1]
print(Solution().findClosestNumber(nums))