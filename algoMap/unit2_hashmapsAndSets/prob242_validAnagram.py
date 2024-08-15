# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Init counter hashmap
        counts = {}
        
        # Build counter of characters in s
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        
        # Check every char in t        
        for char in t:
            if char not in counts: # char is not in chars of s, not anagram
                return False
            elif counts[char] == 1: # Only one char left found, next time we have none, so just remove from hashmap
                del counts[char]
            else: # Decrease count of available chars
                counts[char] -= 1
            
        return not counts # If hashmap is empty, then used all chars, is anagram. If remaining characters, not an anagram
    
s = "raaaat"
t = "taaar"

print(Solution().isAnagram(s, t))
