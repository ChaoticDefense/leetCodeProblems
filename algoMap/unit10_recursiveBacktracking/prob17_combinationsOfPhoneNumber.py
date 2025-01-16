# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:

# Input: digits = ""
# Output: []

# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]

# I made this code without looking at any solution or hint on 1/15/2025.
# Super proud of myself as recursive backtracking has kicked my butt so far lol

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Special case: empty string
        if not digits:
            return []
        
        # Init output and builder arrays
        res, sol = [], []
        
        # Get length of valid combination
        k = len(digits)
        
        # Map digit to character list
        keymap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        # Modify input to list mapped strings
        strs = [keymap[digit] for digit in digits]

        # Recursive function
        def backtrack(i):
            # Can only have valid combo as long as length of digit string
            if len(sol) == k:
                res.append(''.join(sol[:]))
                return
            
            # Loop through current letters in string
            for j in range(len(strs[i])):
                # Add current letter in string and then move on to next string
                sol.append(strs[i][j])
                backtrack(i+1)
                sol.pop()
        
        backtrack(0)
        return res
    
digits = "232"
# digits = ""
print(Solution().letterCombinations(digits))