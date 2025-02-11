# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

# Example 1:

# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 

# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.

# Example 2:

# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18

from typing import List
import heapq
from collections import deque

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Init minCost
        minCost = 0
        # Get length of points
        n = len(points)
        
        # Add first point cost to get to this point (which is 0) and index
        heap = [(0,0)]
        
        # Make a set of points we have been to
        seen = set()
        
        # Loop until we have been to all of the points
        while len(seen) < n:
            # Pop current point distance (from other point) and index from heap
            # Pops the smallest distance point
            d, i = heapq.heappop(heap)
            
            # Check if we have been here before
            if i not in seen:
                minCost += d
                seen.add(i)
                # Get x and y coords of point
                x, y = points[i]
                
                # Loop through all other points in list that are not current point
                for p in range(n):
                    if p == i:
                        continue
                    # Get distance to other points from current point and add them to the heap
                    x_p, y_p = points[p]
                    tmpDist = abs(x_p - x) + abs(y_p - y)
                    heapq.heappush(heap, (tmpDist, p))
        
        # After we have been to each point, the minimum cost will be the shortest dist to connect each point           
        return minCost
    
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

print(Solution().minCostConnectPoints(points))