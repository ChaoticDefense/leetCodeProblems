# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Building min heap from scratch
        heap = []
        
        # Counter object to count items in array
        counter = Counter(nums)
        
        # Build min heap that has only k number of items in it, sorted by count
        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))
        
        return [h[1] for h in heap]
    
    
nums = [1,1,1,2,2,3]
k = 2

print(Solution().topKFrequent(nums, k))