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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: 
        if not root: return 0
        
        # Post order traversal DFS, starting with left node
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        # Return 1 plus the max depth between left and right
        return 1 + max(leftDepth, rightDepth)
    
    

A = TreeNode(3)
B = TreeNode(9)
C = TreeNode(20)
D = TreeNode(15)
E = TreeNode(7)

A.left = B
A.right = C
C.left = D
C.right = E

print(Solution().maxDepth(A))