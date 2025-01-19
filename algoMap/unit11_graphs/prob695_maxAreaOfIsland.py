# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:

# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0

from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        # Get dimensions of grid
        m, n = len(grid), len(grid[0])
        
        # # Recursive DFS function
        # def dfs(i,j):
        #     # Out of bounds ot at water
        #     if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
        #         return 0
            
        #     # At land within bounds, add 1 to tmp area and mark current space as wate
        #     grid[i][j] = 0
            
        #     # Check each direction from current squre
        #     return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
        
        # for i in range(m):
        #     for j in range(n):
        #         # Found land
        #         if grid[i][j] == 1:
        #             # Compare current island's area with max_area seen
        #             max_area = max(max_area, dfs(i,j))
        
        # # Iterative DFS
        # for i in range(m):
        #     for j in range(n):
        #         # Found land
        #         if grid[i][j] == 1:
        #             tmp_area = 0
                    
        #             # Add current coords to stack
        #             stack = [(i,j)]
        #             while stack:
        #                 # Pop current coords from stack
        #                 a, b = stack.pop()
                        
        #                 # Out of bounds or at water
        #                 if a < 0 or a >= m or b < 0 or b >= n or grid[a][b] != 1:
        #                     continue
                        
        #                 # Mark current space as water
        #                 grid[a][b] = 0
                        
        #                 # Add 1 to current island area and check all 4 directions by adding to stack
        #                 tmp_area += 1
        #                 stack.append((a+1,b))
        #                 stack.append((a,b+1))
        #                 stack.append((a-1,b))
        #                 stack.append((a,b-1)) 
                    
        #             # Compare current island's area with max_area seen
        #             max_area = max(max_area, tmp_area)
                    
        # Iterative BFS
        for i in range(m):
            for j in range(n):
                # Found land
                if grid[i][j] == 1:
                    tmp_area = 0
                    
                    # Add current coords to queue
                    q = deque()
                    q.append((i,j))
                    while q:
                        # Pop current coords from queue
                        a, b = q.popleft()
                        
                        # Out of bounds or at water
                        if a < 0 or a >= m or b < 0 or b >= n or grid[a][b] != 1:
                            continue
                        
                        # Mark current space as water
                        grid[a][b] = 0
                        
                        # Add 1 to current island area and check all 4 directions by adding to queue
                        tmp_area += 1
                        q.append((a+1,b))
                        q.append((a,b+1))
                        q.append((a-1,b))
                        q.append((a,b-1)) 
                    
                    # Compare current island's area with max_area seen
                    max_area = max(max_area, tmp_area)
                    
        return max_area
    
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(Solution().maxAreaOfIsland(grid))