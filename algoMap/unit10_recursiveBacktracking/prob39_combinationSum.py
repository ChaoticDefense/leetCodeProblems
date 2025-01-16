# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
# frequency
# of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:

# Input: candidates = [2], target = 1
# Output: []

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Init output and builder arrays
        res, sol = [], []
        # Get length of nums
        n = len(candidates)
        
        # Keep track of current sum of builder array
        curr_sum = 0
        
        # Recursive function
        def backtrack(i, curr_sum):
            # Base case: current sum equals target
            if curr_sum == target:
                res.append(sol[:])
                return
            # Base case: went over target or reached end of anums
            if curr_sum > target or i == n:
                return
            
            # Keep adding current number to builder array, adding to current sum
            # Either adding to target sum or over
            sol.append(candidates[i])
            curr_sum += candidates[i]
            backtrack(i, curr_sum)
            
            # After adding, remove and subtract from current sum
            sol.pop()
            curr_sum -= candidates[i]
            
            # Don't add number and move on to next number
            backtrack(i+1, curr_sum)
            
        backtrack(0, curr_sum)
        return res

candidates = [2,3,6,7]
target = 7
print(Solution().combinationSum(candidates, target))