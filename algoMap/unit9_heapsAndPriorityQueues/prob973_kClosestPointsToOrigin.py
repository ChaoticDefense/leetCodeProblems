# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

# Example 1:

# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.

from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Init Heap
        heap = []
        
        # Loop through each point
        for point in points:
            x = point[0]
            y = point[1]
            
            # Get distance from origin at current point
            # Do not need to do sqrt since each value can be compared without it
            dist = x**2 + y**2
            
            # Using a max heap that is only k big
            if len(heap) < k:
                heapq.heappush(heap, (-dist, point))
            else: # Once heap is k big, pop off largest distance every time we push to heap
                heapq.heappushpop(heap, (-dist, point))
        
        # Returning only points, not their distances
        return [point for _, point in heap]
    
# points = [[1,3],[-2,2]]
# k = 1

points = [[3,3],[5,-1],[-2,4]]
k = 2

print(Solution().kClosest(points,k))