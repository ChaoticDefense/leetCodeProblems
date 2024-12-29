# from ...helperFunctions.binaryTrees import TreeNode

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Post Order Traversal
        # Can also do the swapping before navigating tree
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        root.left, root.right = root.right, root.left
        
        return root
    
A = TreeNode(4)
B = TreeNode(2)
C = TreeNode(7)
D = TreeNode(1)
E = TreeNode(3)
F = TreeNode(6)
G = TreeNode(9)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G

print(Solution().invertTree(A))