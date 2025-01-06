# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

 

# Example 1:

# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
# Example 2:

# Input: stones = [1]
# Output: 1

from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        
        # Make max heap
        for i in range(n):
            stones[i] = -stones[i]
            
        heapq.heapify(stones)
        
        # Loop until there is one stone left
        while len(stones) > 1:
            
            # Pop off two largest stones
            s1 = -heapq.heappop(stones)
            s2 = -heapq.heappop(stones)
            
            # If stones are different, add difference back to heap
            if s1 != s2:
                heapq.heappush(stones, -(s1 - s2))
            # Otherwise the stones were the same, and they are both destroyed
        
        # Since we made max heap, return negative of last value
        return -stones[0] if stones else 0

stones = [2,7,4,1,8,1]
# stones = [1]
# stones = [2,2]
print(Solution().lastStoneWeight(stones))