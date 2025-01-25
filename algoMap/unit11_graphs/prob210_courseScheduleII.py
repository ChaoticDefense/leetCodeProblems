# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]

from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Convert edge graph to adjacency graph
        D = defaultdict(list)
        for u, v in prerequisites:
            D[u].append(v)
            
        # # The input of prerequisites [a_i, b_i] mean that b_i needs to be completed first
        # # I.e [0,1] would look like 1 -> 0
    
        # # Constants for the state of each course
        # UNVISITED = 0
        # VISITING = 1
        # VISITED = 2

        # # Make array of states for each course
        # states = [UNVISITED] * numCourses
        
        # # Init output array
        # ans = []
        
        # # DFS function on each node
        # def dfs(node):
        #     # Get current state
        #     state = states[node]
            
        #     # If we already know we can take the course, just return
        #     if state == VISITED:
        #         return True
            
        #     # We found a node we're currently visiting
        #     # Therefore we found a loop
        #     if state == VISITING:
        #         return False
            
        #     # Node is unvisited, set to visiting
        #     states[node] = VISITING
            
        #     # Do DFS on each of the neighbor nodes
        #     for nei in D[node]:
        #         if not dfs(nei):
        #             return False
            
        #     # After searching all neighbors and didn't find a cycle,
        #     # add current node to order list and mark as visited
        #     ans.append(node)
        #     states[node] = VISITED
        #     return True
        
        # # Do DFS on each node    
        # for i in range(numCourses):
        #     if not dfs(i):
        #         # Found a cycle, can't do topological sort
        #         return []
        
        # # In a NORMAL topological sort, we would return ans[::-1] because
        # # we append the "last" node first, but since this problem has
        # # essentially v -> u, instead of normally u -> v, we just return the
        # # normal list  
        # return ans
    
    
        # BFS Solution:
        # Keeping track of how many nodes we visited
        order = []
        
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
            # Pop node from stack and add node to order list
            node = q.popleft()
            order.append(node)
            
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
        return order[::-1] if len(order) == numCourses else []
    
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]] 
print(Solution().findOrder(numCourses, prerequisites))