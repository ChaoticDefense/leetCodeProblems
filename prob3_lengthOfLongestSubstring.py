# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        
        # Sliding window technique, having two indices of l and r, both starting at 0
        l = 0
        
        # Create a set to keep track of non-repeating characters in the sliding window
        charSet = set()
        
        # Iterate the right part of the sliding window over the length of the string
        for r in range(len(s)):
            # If r index encounters a repeat letter, keep moving left part of window until no more repeating chars
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            # Add r index letter to unique letter set
            charSet.add(s[r])
            
            # Compare the current max length to the length of the sliding window
            maxLen = max(maxLen, r - l + 1)
        return maxLen



# Below solution is exceeded memory limit on LeetCode
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        
#         maxLen = 0
        
#         substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s) + 1)]
        
#         for option in substrings:
#             length = 0
#             hashmap = {}
#             for letter in option:
#                 if letter in hashmap:
#                     break
#                 hashmap[letter] = 1
#                 length += 1
#             if length > maxLen:
#                 maxLen = length    

#         return maxLen
    
    
    
print(Solution().lengthOfLongestSubstring("pneumonoultramicroscopicsilicovolcanoconiosis"))
