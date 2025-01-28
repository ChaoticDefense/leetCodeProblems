# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

#     its length is at least two, and
#     the sum of the elements of the subarray is a multiple of k.

# Note that:

#     A subarray is a contiguous part of the array.
#     An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

 
# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

# Example 2:

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        # initialize total
        total = 0
        
        # Hashmap of remainders of current total when dividing by target
        # 0 is initiualized to an index of -1 to eliminate the case of the first element in input array being a multiple of k
        # Subarray has to be length of 2 or more
        remainderMap = {0: -1} # remainder: end index
        
        """We care about finding keeping track of the remainders because when we divide the current total
        by target we get a remainder, then store it. We then add the next number in the array to the total
        and divide again. If the number we just added to the total causes a remainder we have seen before,
        then we have now added a sub array that equals a multiple of the target
        
        For example: [23, 2, 4, 6, 7], k = 6. On first iteration, 23 % 6 = 5, so we store it. Next, 23+2 = 25,
        which gives a remainder of 1, again we store it. But when we add 4, we get remainder 5 again. That
        means a valid sub array exists, because we did 23 + (2 + 4). To verify it is an actual valid subarray,
        we have to compare the size of it. We can simply do that by checking the current index versus the index
        of the found remainder."""
        
        # Loop through array and enumerate to easily keep track of index and value
        for i, n in enumerate(nums):
            # Add value to current total and mod it by k
            total += n
            r = total % k
            
            # If remainder not in map, add it
            if r not in remainderMap:
                remainderMap[r] = i
                
            # Compare length of sub array by checking current index with index found in hash map
            elif i - remainderMap[r] > 1:
                return True
        # Checked entire array and found no valid subarray   
        return False


nums = [23,2,4,6,7]
k = 6

print(Solution().checkSubarraySum(nums, k))