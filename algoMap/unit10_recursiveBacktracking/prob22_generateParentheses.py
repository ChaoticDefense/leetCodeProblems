# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:

# Input: n = 1
# Output: ["()"]

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Init output and builder arrays
        res, sol = [], []
        
        # Keep track of number of open and number of close, both equal to n
        num_open = [n] 
        num_close = [n]
        
        # Recursive function
        def backtrack():
            # Base case: length of sol is 2*n (for every open there is a close)
            # and all opens and closes were used up
            if len(sol) == 2 * n and num_open[0] == 0 and num_close[0] == 0:
                res.append(''.join(sol))
                return
            # Used too many opens or used more closes than opens
            if num_open[0] < 0 or num_close[0] < num_open[0]:
                return
            
            # Add an open
            sol.append('(')
            num_open[0] -= 1
            backtrack()
            sol.pop()
            num_open[0] += 1
            
            # Add a close
            sol.append(')')
            num_close[0] -= 1
            backtrack()
            sol.pop()
            num_close[0] += 1
            
        
        backtrack()
        return res
    
n = 4
print(Solution().generateParenthesis(n))