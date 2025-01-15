# Given an array nums of distinct integers, return all the possible
# permutations
# . You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:

# Input: nums = [1]
# Output: [[1]]

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Init output and builder arrays
        res, sol, = [], []
        
        # Get length of input
        n = len(nums)
        
        # Recursive function
        def backtrack():
            # Base case: Length of sol is equal to n, found permutation
            if len(sol) == n:
                res.append(sol[:])
                return
            
            # Loop through all nums during each call
            for num in nums:
                # Only add and recursive call if not already in sol
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()
        
        backtrack()
        return res
    

nums = [1,2,3,4,5]
print(Solution().permute(nums))