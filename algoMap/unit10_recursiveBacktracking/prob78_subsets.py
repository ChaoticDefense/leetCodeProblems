# Given an integer array nums of unique elements, return all possible
# subsets
# (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Output and tmp array that builds output
        res, sol = [], []
        
        # Get length of nums
        n = len(nums)
        
        def backtrack(i):
            # Base case: decided through all numbers in set
            if i == n:
                res.append(sol[:])
                return
        
            # First choice: Do NOT add nums[i] to sol and continue
            backtrack(i+1)
            
            # Second choice: DO add nums[i] to sol and continue
            sol.append(nums[i])
            backtrack(i+1)
            
            # After deciding to add nums[i], remove it to go back up the decision tree
            sol.pop()
        
        # Start recursion at beginning of nums           
        backtrack(0)
        return res
    
    # Time: O(2^n)
    # Space: O(n!)
    
nums = [1,2,3]
print(Solution().subsets(nums))