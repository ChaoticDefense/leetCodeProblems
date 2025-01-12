# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
        
#         A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
        
         
        
#         Example 1:
        
#         Input: s = "abc", t = "ahbgdc"
#         Output: true
        
#         Example 2:
        
#         Input: s = "axc", t = "ahbgdc"
#         Output: false
        

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Grab lengths of s and t
        s_len = len(s)
        t_len = len(t)
        
        # Pointer that will move across s
        sp = 0
        
        # Base cases: If s is empty or if the length of s is greater than t
        if s == '': return True
        if s_len > t_len: return False
        
        # Traverse through t
        for tp in range(t_len):
            # Characters match
            if t[tp] == s[sp]:
                # Reached end of s
                if sp == s_len - 1:
                    return True
                sp += 1
        
        # Did not find subsequence after traversing through t    
        return False
    
s = "abc"
t = "ahbgdc"

print(Solution().isSubsequence(s,t))