# Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
# palindrome
#  that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.


# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         hashmap = {char: s.count(char) for char in s}
        
#         num = 0
#         odd_found = False
#         for counts in hashmap.values():
#             if counts % 2 == 0:
#                 num += counts
#             else:
#                 odd_found = True
#                 num += counts - 1
 
        
#         return num + 1 if odd_found else num

class Solution:
    def longestPalindrome(self, s: str) -> int:
        seenChar = set()

        length = 0
        
        for char in s:
            if char in seenChar:
                length += 2
                seenChar.remove(char)
            else:
                seenChar.add(char)
        
        if seenChar:
            length += 1
            
        return length
        
        
    
s = "abccccdd"
print(Solution().longestPalindrome(s))