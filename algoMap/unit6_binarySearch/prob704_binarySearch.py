from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        L = 0
        R = N - 1
        
        while L <= R:
            M = L +((R-L) // 2)
            if nums[M] == target:
                return M
            elif nums[M] < target:
                L = M + 1
            else:
                R = M - 1
        
        
        return -1
   
nums = [-1,0,3,5,9,12]
target = 9

print(Solution().search(nums, target))