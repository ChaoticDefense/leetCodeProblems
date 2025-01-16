# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

 

# Example 1:

# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

# Example 2:

# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Init output and builder arrays
        res, sol = [], []
        
        # Recursive function
        def backtrack(x):
            # Base case: Len of sol equal to k, found a combination
            if len(sol) == k:
                res.append(sol[:])
                return

            # Check how many numbers we have left to check and how many we still need
            # to make a valid combination
            left = x
            still_need = k - len(sol)
            
            # If we have more than we need, we can afford to skip adding the number for now
            if left > still_need:
                backtrack(x-1)
            
            # Add the number and process
            sol.append(x)
            backtrack(x-1)
            sol.pop()
        
        backtrack(n)
        return res
    
n = 4
k = 4
print(Solution().combine(n,k))