class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Init output and pointers
        longest = 0
        l = 0
        n = len(s)
        
        # keep track of seen characters
        seen_chars = set()
        
        # Loop over string
        for r in range(n):
            # Invalid condition: character at r has already been seen
            # Move l (shrink window) until the character at r no longer in set
            while s[r] in seen_chars:
                seen_chars.remove(s[l])
                l += 1
            
            # Add character at r to the set
            seen_chars.add(s[r])
            
            # Window size, compare to longest
            w = r - l + 1
            longest = max(longest, w)
        
        return longest

# s = "abcabcbb"
s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))