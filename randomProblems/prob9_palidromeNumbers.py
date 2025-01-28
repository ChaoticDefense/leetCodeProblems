# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         numStr = str(x)
#         return numStr == numStr[::-1]
    
# s = Solution()
# print(s.isPalindrome(3663))

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers can't be palindromes
        # Multiples of 10 can't be palindromes either
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Loop over last half of number and compare it to first half
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
        return x == revertedNumber or x == revertedNumber // 10

s = Solution()
print(s.isPalindrome(725))