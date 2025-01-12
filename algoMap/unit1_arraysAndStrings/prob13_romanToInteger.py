# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer.


class Solution:
    def romanToInt(self, s: str) -> int:
        # Map Numerals to numbers
        keymap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000  
        }
        
        # Start index at end of numeral and work backwards
        i = len(s) - 1
        total = 0
        
        while i > 0:
            # If numeral val is greater than one before it
            # Add the difference to total
           if keymap[s[i]] > keymap[s[i-1]]:
               total += keymap[s[i]] - keymap[s[i-1]]
               i -= 2
           else:
               # Add value at current numeral
               total += keymap[s[i]]
               i -= 1
               
        # If we're at beginning of string, add its value     
        if i == 0:
            total += keymap[s[i]]
        
        return total
    
s = 'LVIII'
print(Solution().romanToInt(s))