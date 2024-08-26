from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        shortest = float('inf')
        curr_sum = 0
        
        l = 0
        
        for r in range(len(nums)):
            curr_sum += nums[r]
            
            while curr_sum >= target:
                w = r - l + 1
                shortest = min(shortest, w)
                curr_sum -= nums[l]
                l += 1
        
        return shortest if shortest != float('inf') else 0

# target = 7
# nums = [2,3,1,2,4,3]   

target = 11
nums = [1,4,4]  
print(Solution().minSubArrayLen(target, nums))