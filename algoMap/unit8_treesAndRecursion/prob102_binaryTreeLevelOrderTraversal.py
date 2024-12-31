# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:

# Input: root = [1]
# Output: [[1]]

# Example 3:

# Input: root = []
# Output: []


from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Base case: root is empty
        if not root:
            return []
        
        # Init ans arrary
        ans = []
        
        # Create queue and append root since we know it will be valid
        q = deque()
        q.append(root)
        
        # Repeat until queue is empty
        while q:
            # Temp array to store nodes at current level
            level = []
            
            # Get current length of queue to determine how many times to iterate
            n = len(q)
            
            for _ in range(n):
                # Pop node from left and append to level array
                node = q.popleft()
                level.append(node.val)
                 
                # Add left and right nodes to queue if they exist
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            # Append level array to answer                    
            ans.append(level)
                
        return ans
    
    
A = TreeNode(3)
B = TreeNode(9)
C = TreeNode(20)
D = TreeNode(15)
E = TreeNode(7)

A.left = B
A.right = C
C.left = D
C.right = E

print(Solution().levelOrder(A))   
# print(Solution().levelOrder(None))          