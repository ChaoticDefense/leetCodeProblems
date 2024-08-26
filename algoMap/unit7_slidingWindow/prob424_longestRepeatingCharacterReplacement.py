# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        unq_char = set(s)
        n = len(s)
        
        for char in unq_char:
            l = 0
            num_other = 0
            
            for r in range(n):
                if s[r] != char:
                    num_other += 1
                    
                while num_other > k:
                    if s[l] != char:
                        num_other -= 1
                    l += 1
                
                w = r - l + 1
                longest = max(longest, w)
            
        return longest
    
s = "ABABA"
k = 2

print(Solution().characterReplacement(s,k))