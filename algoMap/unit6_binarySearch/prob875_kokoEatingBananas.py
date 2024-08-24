# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23

from typing import *

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Set L and R to 1 and max(piles), respectively
        # Min is 1 banana/hr, max is whatever max pile there is
        L = 1
        R = max(piles)
        
        # Binary search over L and R
        while L < R:
            k = L + ((R-L) // 2)
            
            # Test current eating speed
            time = 0
            for pile in piles:
               time += -(-pile // k) # Ceiling of integer division
            
            if time <= h:
                R = k # Found new minimum, but we dont know if to the left will work
            else:
                L = k + 1 # current k did not work, move L to k + 1
            
        return R
    
piles = [3,6,7,11]
h = 8

print(Solution().minEatingSpeed(piles,h))