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
        
        D = defaultdict(list)
        for a, b in prerequisites:
            D[a].append(b)
            
        visited = [0] * numCourses
        
        def dfs(node):
            for nei_node in D[node]:
                pass
        
        for i in range(numCourses):
            if visited[i] == 0:
                visited[i] = 1  

        
        
        
        # seen = set()
        # seen.add(0)
        
        # def dfs(node):
        #     if not D[node]:
        #         return True
            
            
            
        #     for nei_node in D[node]:
        #         if nei_node not in seen:
        #             seen.add(nei_node)
        #             dfs(nei_node)
                    
        # dfs(0)
        # return len(seen) == numCourses

# numCourses = 2
# prerequisites = [[1,0]]

# numCourses = 2
# prerequisites = [[1,0],[0,1]]

numCourses = 3
prerequisites = [[0,1], [1,2]]
print(Solution().canFinish(numCourses, prerequisites))