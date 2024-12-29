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
        
        # Get length of strings
        n1 = len(s1)
        n2 = len(s2)
        
        # Base check, s2 cannot be longer than s1
        if n1 > n2:
            return False
        
        # Build up hash set for s1 and initial hash set for s2
        for i in range(n1):
            h1[ord(s1[i]) - ord('a')] += 1
            h2[ord(s2[i]) - ord('a')] += 1
        
        # Initial check if s2 contains permutation of s1    
        if h1 == h2:
            return True
        
        # Start at next character index and loop until end of s2   
        for i in range(n1, n2):
            # Move sliding window that is n1 wide
            h2[ord(s2[i]) - ord('a')] += 1 # Add char at i to s2 hash set
            h2[ord(s2[i-n1]) - ord('a')] -= 1 # Remove left char
            
            
            if h1 == h2:
                return True
        
                                                                                                                                                                                                                                 
        return False
    
    # Time: O(n2) Space: O(1)
    
    
s1 = "ab"
s2 = "eidboaooo"
print(Solution().checkInclusion(s1, s2))