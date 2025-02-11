# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

# Example 1:

# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2

# Example 2:

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1

# Example 3:

# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1

from typing import List
import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minTimes = {}
        
        # Make adjacency list
        g = defaultdict(list)
        for u, v, w in times:
            g[u].append((v,w))
        
        # Djikstra's Algorithm
        # Add source node and cost to get there (which is 0) to heap
        heap = [(0, k)]
        
        # Loop until heap is empty
        while heap:
            # Pop from heap, getting distance from source to current node
            d, node = heapq.heappop(heap)
            # If we have been here before skip
            if node not in minTimes:
                # Otherwise add cost to get here from source to dictionary
                minTimes[node] = d
                
                # Loop through neighbor nodes and care only if we haven't been to them
                for nei, cost in g[node]:
                    if nei not in minTimes:
                        # Push to heap the neighbor and the TOTAL cost from the source to the current node
                        heapq.heappush(heap, (cost + d, nei))
        
        # This problem asks for the minimum time to reach all nodes from source, otherwise -1 if we can't reach all nodes
        return max(minTimes.values()) if len(minTimes) == n else -1
    
times = [[1,2,1],[1,4,4],[2,3,1],[2,5,10],[3,1,4],[5,4,4]]
n = 5
k = 1 

print(Solution().networkDelayTime(times,n,k))