from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Fixed sliding window
        n = len(nums)
        curr_sum = 0
        
        # Building up fixed window, getting current sum of the window
        for i in range(k):
            curr_sum += nums[i]
        
        # Find first average by dividing sum of window by length of window
        max_avg = curr_sum / k
        
        # Move window until reaching end of array, updating sum and max average
        for i in range(k,n):
            # when moving window, add number at i, but subtract by number that just left window
            curr_sum += nums[i]
            curr_sum -= nums[i-k]
            
            max_avg = max(max_avg, curr_sum / k)
        
        return max_avg
    
nums = [1,12,-5,-6,50,3]
k = 4

print(Solution().findMaxAverage(nums,k))