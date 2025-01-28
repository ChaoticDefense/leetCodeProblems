# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

# Example 1:

# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

# Example 2:

# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.


from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        # # BFS
        # # Make queues and sets for all spaces that can flow into respective ocean
        # p_que = deque()
        # p_seen = set()
        
        # a_que = deque()
        # a_seen = set()
        
        # # These 4 for loops initially creates the sets of all spaces that can flow into
        # # either Pacific or Atlantic Ocean
        # # Also adding to queues for respective ocean
        # for j in range(n):
        #     p_que.append((0,j))
        #     p_seen.add((0,j))
            
        # for i in range(1,m):
        #     p_que.append((i,0))
        #     p_seen.add((i,0))
            
        # for j in range(n):
        #     a_que.append((m-1,j))
        #     a_seen.add((m-1,j))
            
        # for i in range(0,m-1):
        #     a_que.append((i,n-1))
        #     a_seen.add((i,n-1))

        # # Helper function ran on both sets that can flow into respective ocean
        # def get_coords(q: deque, seen: set):
        #     # Loop until q is empty
        #     while q:
        #         # Pop current coords from queue
        #         i, j = q.popleft()
        #         # Look at each adjacent space from current space
        #         # Vector is list of directions to change 
        #         for i_off, j_off in [(0,1), (1,0), (-1,0), (0,-1)]: # Right, Down, Left, Up
        #             i_new, j_new = i + i_off, j + j_off
        #             # Check if we are in bounds, we can flow water from the current neighbor, and we have not seen neighbor before
        #             if 0 <= i_new < m and 0 <= j_new < n and heights[i_new][j_new] >= heights[i][j] and (i_new, j_new) not in seen:
        #                 # Add neighbor to queue to be processed further and to seen set
        #                 q.append((i_new,j_new))
        #                 seen.add((i_new,j_new))
                        
        #     # Return the set of all spaces that can flow into the ocean
        #     return seen
        
        # # Get set of all spaces that can flow into Pacific Ocean
        # p_coords = get_coords(p_que,p_seen)
        
        # # Get set of all spaces that can flow into Atlantic Ocean
        # a_coords = get_coords(a_que,a_seen)
        
        # # Return intersection of both sets (which spaces are in both sets)
        # return list(p_coords.intersection(a_coords))
        
        # # DFS Recursive
        # p_seen = set()
        # a_seen = set()
            
        # # Recursive function
        # def dfs(i,j,h,seen):
        #     # Base case: Out of bounds, curr space less than previous, or we've been here before
        #     if i < 0 or i >= m or j < 0 or j >= n or heights[i][j] < h or (i,j) in seen:
        #         return
            
        #     # Add current space to list that can flow into ocean
        #     seen.add((i,j))
        #     for i_off, j_off in [(0,1), (1,0), (-1,0), (0,-1)]: # Right, Down, Left, Up
        #         i_new, j_new = i + i_off, j + j_off
        #         dfs(i_new,j_new,heights[i][j],seen)
           
        # # Only start DFS on boundaries of the oceans 
        # for i in range(m):
        #     dfs(i,0,heights[i][0],p_seen) # Pacific left
        #     dfs(i,n-1, heights[i][n-1],a_seen) # Atlantic right
            
        # for j in range(n):
        #     dfs(0,j,heights[0][j],p_seen) # Pacific top
        #     dfs(m-1,j,heights[m-1][j],a_seen) # Atlantic bottom
            
        # return list(p_seen.intersection(a_seen))
        
        # DFS Iterative
        p_seen, a_seen = set(), set()
        p_stack, a_stack = [], []
        
        for j in range(n):
            p_stack.append((0,j))
            p_seen.add((0,j))
            
        for i in range(1,m):
            p_stack.append((i,0))
            p_seen.add((i,0))
            
        for j in range(n):
            a_stack.append((m-1,j))
            a_seen.add((m-1,j))
            
        for i in range(0,m-1):
            a_stack.append((i,n-1))
            a_seen.add((i,n-1))
    
        # Helper function ran on both sets that can flow into respective ocean
        def get_coords(s: List, seen: set):
            # Loop until s is empty
            while s:
                # Pop current coords from stack
                i, j = s.pop()
                # Look at each adjacent space from current space
                # Vector is list of directions to change 
                for i_off, j_off in [(0,1), (1,0), (-1,0), (0,-1)]: # Right, Down, Left, Up
                    i_new, j_new = i + i_off, j + j_off
                    # Check if we are in bounds, we can flow water from the current neighbor, and we have not seen neighbor before
                    if 0 <= i_new < m and 0 <= j_new < n and heights[i_new][j_new] >= heights[i][j] and (i_new, j_new) not in seen:
                        # Add neighbor to queue to be processed further and to seen set
                        s.append((i_new,j_new))
                        seen.add((i_new,j_new))
                        
            # Return the set of all spaces that can flow into the ocean
            return seen
        
        a_coords = get_coords(a_stack,a_seen)
        p_coords = get_coords(p_stack,p_seen)
        
        return list(a_coords.intersection(p_coords))
    

heights = [[1,2,2,3,5],
           [3,2,3,4,4],
           [2,4,5,3,1],
           [6,7,1,4,5],
           [5,1,1,2,4]]

print(Solution().pacificAtlantic(heights))