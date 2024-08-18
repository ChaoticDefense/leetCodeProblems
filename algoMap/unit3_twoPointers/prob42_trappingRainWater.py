# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

class Solution:
    def trap(self, height: list[int]) -> int:
        totalWater = 0
        n = len(height)
        
        L = [0] * n
        R = [0] * n
        maxL = 0
        maxR = 0
        for i in range(1,n):
            maxL = max(maxL, height[i - 1])
            L[i] = maxL
            j = -i - 1
            maxR = max(maxR, height[j + 1])
            R[j] = maxR
            
        for i in range(n):
            water = min(L[i], R[i]) - height[i]
            totalWater += water if water > 0 else 0
        
        return totalWater
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))