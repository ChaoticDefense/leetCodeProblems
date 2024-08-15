# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:

# Input: text = "nlaebolko"
# Output: 1

# Example 2:

# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:

# Input: text = "leetcode"
# Output: 0

from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = 'balloon'
        h = defaultdict(int)
        for char in text:
            if char in 'balloon':
                h[char] += 1
                
        if any(c not in h for c in balloon):
            return 0
        else:
            return min(h['b'], h['a'], h['l'] // 2, h['o'] // 2, h['n'])
    
# text = "nlaebolko"
# text = "leetcode"
text = "loonbalxballpoon"
print(Solution().maxNumberOfBalloons(text))