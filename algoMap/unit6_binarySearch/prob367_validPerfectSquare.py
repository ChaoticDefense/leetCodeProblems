# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

 

# Example 1:

# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

# Example 2:

# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Start L and R range between 1 and num // 2
        L = 1
        R = -(-num // 2) # Ceiling of integer division of 2
        
        # Binary search over number range, checking square of middle
        while L <= R:
            M = L + ((R-L) // 2)
            if M**2 == num:
                return True
            elif M**2 < num:
                L = M + 1
            else:
                R = M - 1
        
        return False

num = 16
print(Solution().isPerfectSquare(num))