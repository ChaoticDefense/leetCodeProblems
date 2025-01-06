# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

from typing import List
import heapq

class Solution:
    # Max Heap Solution
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # Make max heap
    #     for i in range(len(nums)):
    #         nums[i] = -nums[i]
            
    #     heapq.heapify(nums)
        
    #     # Pop off max value until kth largest is left
    #     for i in range(k-1):
    #         heapq.heappop(nums)
        
    #     # First remaining num is largest
    #     return -nums[0]
    
    # Min Heap Solution
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        
        for num in nums:
            if len(arr) < k:
                heapq.heappush(arr, num)
            else:
                heapq.heappushpop(arr, num)
        
        return heapq.heappop(arr)
    
nums = [3,2,1,5,6,4]
k = 2

# nums = [3,2,3,1,2,4,5,5,6]
# k = 4

print(Solution().findKthLargest(nums, k))