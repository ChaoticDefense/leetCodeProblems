# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int:
        # # This problem is essentially fibonacci with different base cases?
        # # Base cases:
        # if n == 1 or n == 2:
        #     return n
        
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # # Top-down memoization
        # cache = {1: 1, 2: 2}
        
        # def f(x):
        #     if x not in cache:
        #         cache[x] = f(x-1)+ f(x-2)
        #     return cache[x]
            
        # return f(n)
        
        # # Bottom-up tabulation
        # if n == 1 or n == 2:
        #     return n
        
        # dp = [0] * n
        # dp[0] = 1
        # dp[1] = 2
        
        # for i in range(2,n):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[-1]
        
        # Bottom-up constant space
        if n == 1 or n == 2:
            return n
        
        prev = 1
        curr = 2
        
        for i in range(2,n):
            prev, curr = curr, prev + curr
            
        return curr
    
n = 45
print(Solution().climbStairs(n))