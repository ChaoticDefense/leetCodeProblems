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
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Convert edge graph to adjacency graph
        D = defaultdict(list)
        for a, b in prerequisites:
            D[a].append(b)
    
        # # Constants for the state of each course
        # UNVISITED = 0
        # VISITING = 1
        # VISITED = 2

        # # Make array of states for each course
        # states = [UNVISITED] * numCourses
        
        # # Recursive function
        # def dfs(node):
        #     # Get state of current node
        #     state = states[node]
            
        #     # At a course we already visited and know we can finish
        #     if state == VISITED:
        #         return True
            
        #     # At a course we currently still visiting
        #     # We found a loop in the courses, therefore cannot
        #     # complete all courses
        #     elif state == VISITING:
        #         return False
            
        #     # At a course that's unvisited, set state to visiting
        #     states[node] = VISITING
            
        #     # Check each neighbor if there's a loop
        #     for nei_node in D[node]:
        #         if not dfs(nei_node):
        #             return False
            
        #     # No problems found from current node, set to visited and return True   
        #     states[node] = VISITED
        #     return True
        
        # # Iterate over each node in graph 
        # for i in range(numCourses):
        #     # If there's a problem at any node, return False
        #     if not dfs(i):
        #         return False
        
        # # No problems found
        # return True

        # BFS Solution:
        # Keeping track of how many nodes we visited
        count = 0
        
        # Keep track of how many nodes point to the current node
        # This is known as "in-degree"
        indegrees = [0] * numCourses
        for i in range(numCourses):
            for j in D[i]:
                indegrees[j] += 1
        
        # Init a queue and append only the nodes with 0 indegrees
        # AKA "source nodes"        
        q = deque([i for i in range(numCourses) if indegrees[i] == 0])

        # Keep looping while queue is not empty
        while q:
            # Pop node from stack and add 1 to visited count
            node = q.popleft()
            count += 1
            
            # Loop through neighbors
            for nei in D[node]:
                # Decrement one from indegrees to keep track we are visiting
                # current neighbor from current node
                indegrees[nei] -= 1
                
                # If we have processed all indegrees of neighbor,
                # add it to the queue because it is now essentially
                # a "source node"
                if indegrees[nei] == 0:
                    q.append(nei)
        
        # After processing the whole graph, check if the number of nodes
        # we visited equal the number of nodes in graph
        return count == numCourses


# numCourses = 2
# prerequisites = [[1,0]]

# numCourses = 2
# prerequisites = [[1,0],[0,1]]

# numCourses = 3
# prerequisites = [[0,1], [1,2]]

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]] 
print(Solution().canFinish(numCourses, prerequisites))