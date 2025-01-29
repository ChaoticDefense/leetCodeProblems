# You are given an m x n grid where each cell can have one of three values:

#     0 representing an empty cell,
#     1 representing a fresh orange, or
#     2 representing a rotten orange.

# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Init time and number of fresh oranges
        minTime = 0
        numFresh = 0
        
        # Get dimensions of grid
        m, n = len(grid), len(grid[0])
        
        # Constants to track state of oranges
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2
        
        # BFS method
        q = deque()
        
        # Iterate over grid once to append rotten orange spaces to queue
        # And count number of fresh oranges found
        for i in range(m):
            for j in range(n):
                if grid[i][j] == FRESH:
                    numFresh += 1
                elif grid[i][j] == ROTTEN:
                    q.append((i,j))
        
        # If after first pass we found no fresh oranges, return 0         
        if numFresh == 0: return 0
        
        # BFS until queue is empty
        while q:
            # Get current size of queue, and each round of BFS will
            # pop off that many items
            size = len(q)
            for _ in range(size):
                # Get current coords from queue
                i, j = q.popleft()
                # Check each adjacent space from rotten orange
                for i_off, j_off in [(0,1),(0,-1),(1,0),(-1,0)]:
                    i_new, j_new = i + i_off, j + j_off
                    # If found a fresh orange adjacent, add it to the queue,
                    # mark it as rotten, and decrement fresh counter
                    if 0 <= i_new < m and 0 <= j_new < n and grid[i_new][j_new] == FRESH:
                        q.append((i_new,j_new))
                        numFresh -= 1
                        grid[i_new][j_new] = ROTTEN
            
            # After each round of BFS, add one to the timer counter         
            minTime += 1  
            
        # After completing BFS, timer will be off by one
        # But if not all oranges are rotten, return -1
        return minTime - 1 if numFresh == 0 else -1
    
grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]
print(Solution().orangesRotting(grid))