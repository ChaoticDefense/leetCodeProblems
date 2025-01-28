# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

# Example 1:

# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

# Example 2:

# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

# Example 3:

# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    def __str__(self):
        return str(self.val)

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Make dictionary to map old nodes to new nodes
        old_to_new = {}
        
        # Iterative BFS
        # Add current node to queue and seen set
        q = deque()
        q.append(node)
        
        seen = set()
        seen.add(node)
        
        # Make hashmap of list pointing to new list
        while q:
            # Pop current node from old graph from queue
            curr = q.popleft()
            
            # Make a new node that has same value as old node
            old_to_new[curr] = Node(val=curr.val)
            
            # Loop through neighbors of old node and traverse them if we haven't seen them yet
            for nei in curr.neighbors:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
        
        # Now we have a map of old nodes to new nodes.
        # Loop through the map, and point neighbors of new node using the map         
        for old, new in old_to_new.items():
            new.neighbors = [old_to_new[nei] for nei in old.neighbors] if old.neighbors else []
        
        # Return ref to new node    
        return old_to_new[node]
    
    
adjList = [[2,4],[1,3],[2,4],[1,3]]
# adjList = []
def createGraph(adjList):
    if not adjList:
        return None

    # Create a list of Node objects (1-based index)
    nodes = [Node(i + 1) for i in range(len(adjList))]
    
    # Connect each node to its neighbors
    for i, neighbors in enumerate(adjList):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]

    # Return the first node as the starting point of the graph
    return nodes[0]

g = createGraph(adjList)
print(Solution().cloneGraph(g))