# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

# Given n, calculate F(n).

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


class Solution:
    def fib(self, n: int) -> int:
        # # Naive recursive
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1

        # # F(n) = F(n-1) + F(n-2)
        # return self.fib(n-1) + self.fib(n-2)
        
        # # Top-down memoization
        # # Make cache of base cases
        # cache = {0: 0, 1: 1}
        
        # def f(x):
        #     # If num already in cache, just return cache[num]
        #     if x in cache:
        #         return cache[x]
        #     else:
        #         # Otherwise calculate fib num at current num
        #         cache[x] = f(x-1) + f(x-2)
        #         return cache[x]
            
        # # # Call helper func on n
        # # return f(n)
        
        # # Bottom-up tabulation
        # # Base cases
        # if n == 0 or n == 1:
        #     return n
        
        # # Pre-allocate array of nums (n+1 long because 0-based)
        # dp = [0] * (n + 1)
        
        # # Set init values from base cases
        # dp[0] = 0
        # dp[1] = 1
        
        # # Loop starting from index 2 to exclusive n+1, building value at i
        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        
        # # Return value at n    
        # return dp[n]
        
        # Bottom-up tabulation (constant space)
        # Base cases
        if n == 0 or n == 1:
            return n
        
        # Set init values from base cases
        prev = 0
        curr = 1
        
        # Loop starting from index 2 to exclusive n+1, building value at i
        for i in range(2, n+1):
            # Constant space, set prev val to curr and curr to prev + curr
            prev, curr = curr, prev+curr
        
        # Curr after looping is fib(n)
        return curr
    
n = 6
print(Solution().fib(n))