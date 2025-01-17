# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 

# Example 1:

# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2

# Example 2:

# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.

from typing import List
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Speical case: source is destination
        if source == destination:
            return True
        
        # Map graph using a default dict
        D = defaultdict(list)
        for u, v in edges:
            # Bi-driectional graph
            D[u].append(v)
            D[v].append(u)
        
        # Make a set of seen nodes so we dont double visit  
        seen = set()
        seen.add(source)
        
        # # Method 1: DFS Recursion
        # def dfs(node):
        #     if node == destination:
        #         return True
            
        #     # Get neighbors from current node and loop through them
        #     for nei_node in D[node]:
        #         # If we havent seen neighbor, add it and go to it
        #         if nei_node not in seen:
        #             seen.add(nei_node)
        #             if dfs(nei_node):
        #                 return True
                    
        #     # Came back to source and didnt find dest, return False
        #     return False
        
        # return dfs(source)
    
        # # Method 2: DFS Iterative with Stack
        # # Add source to stack
        # stack = [source]
        
        # # Loop until stack is empty
        # while stack:
        #     # Pop from stack and check it
        #     node = stack.pop()
        #     if node == destination:
        #         return True
            
        #     # Very similar to DFS Recursive, except we add neighbors to stack
        #     for nei_node in D[node]:
        #         if nei_node not in seen:
        #             seen.add(nei_node)
        #             stack.append(nei_node)
                    
        # # Looked through all paths from source and didn't find dest
        # return False
    
        # Method 3: BFS with Dequeue
        q = deque()
        q.append(source)
        
        # VERY similar to DFS iterative, only diff is popping from left
        while q:
            node = q.popleft()
            if node == destination:
                return True
            
            for nei_node in D[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    q.append(nei_node)
                    
        return False
        
                    
                
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

# n = 6
# edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
# source = 0
# destination = 5

print(Solution().validPath(n, edges, source, destination))