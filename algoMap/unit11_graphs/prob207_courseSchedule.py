# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Convert edge graph to adjacency graph
        D = defaultdict(list)
        for a, b in prerequisites:
            D[a].append(b)
    
        # Constants for the state of each course
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        # Make array of states for each course
        states = [UNVISITED] * numCourses
        
        # Recursive function
        def dfs(node):
            # Get state of current node
            state = states[node]
            
            # At a course we already visited and know we can finish
            if state == VISITED:
                return True
            
            # At a course we currently still visiting
            # We found a loop in the courses, therefore cannot
            # complete all courses
            elif state == VISITING:
                return False
            
            # At a course that's unvisited, set state to visiting
            states[node] = VISITING
            
            # Check each neighbor if there's a loop
            for nei_node in D[node]:
                if not dfs(nei_node):
                    return False
            
            # No problems found from current node, set to visited and return True   
            states[node] = VISITED
            return True
        
        # Iterate over each node in graph 
        for i in range(numCourses):
            # If there's a problem at any node, return False
            if not dfs(i):
                return False
        
        # No problems found
        return True

# numCourses = 2
# prerequisites = [[1,0]]

# numCourses = 2
# prerequisites = [[1,0],[0,1]]

numCourses = 3
prerequisites = [[0,1], [1,2]]
print(Solution().canFinish(numCourses, prerequisites))