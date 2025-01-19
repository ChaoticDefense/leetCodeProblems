# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0
        m, n = len(grid), len(grid[0])
        
        # Iterative DFS
        # Loop through grid until land is found
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # increase total by 1
                    total += 1
                    
                    # Add current land to stack
                    stack = [(i,j)]
                    
                    # Loop until no more in stack
                    while stack:
                        # Get coords from stack
                        a, b = stack.pop()
                        
                        # If current coords are out of bounds or isn't land, just continue
                        if a >= m or a < 0 or b >= n or b < 0 or grid[a][b] != "1":
                            continue
                        
                        # We're at land within bounds.
                        # Mark it as sen by changing to water
                        grid[a][b] = "0"
                        
                        # All adjacent squares to stack and check them
                        stack.append((a+1,b))
                        stack.append((a-1,b))
                        stack.append((a,b+1))
                        stack.append((a,b-1))
        
        return total
    
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(Solution().numIslands(grid))