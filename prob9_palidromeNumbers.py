class Solution:
    def isPalindrome(self, x: int) -> bool:
        numStr = str(x)
        return numStr == numStr[::-1]
    
s = Solution()
print(s.isPalindrome(3663))