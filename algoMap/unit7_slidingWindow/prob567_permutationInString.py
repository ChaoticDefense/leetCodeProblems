# Given two strings s1 and s2, return true if s2 contains a
# permutation
# of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:     
        # Init hash sets, 26 long each
        # Each spot correlates to number of letters, from a to z
        h1 = [0] * 26
        h2 = [0] * 26
        
        n1 = len(s1)
        n2 = len(s2)
        
        l = 0
        
        for r in range(n1):
            h1[ord(s1[r]) - ord('a')] += 1
            h2[ord(s2[r]) - ord('a')] += 1
            
        for r in range(r,n2):
            if h1 == h2:
                return True
            
            
            h2[ord(s2[r]) - ord('a')] += 1
            
            h2[ord(s2[l]) - ord('a')] -= 1
            l += 1
                                                                                                                                                                                                                                 
        return False
    
    
s1 = "ab"
s2 = "eidboaooo"
print(Solution().checkInclusion(s1,s2))