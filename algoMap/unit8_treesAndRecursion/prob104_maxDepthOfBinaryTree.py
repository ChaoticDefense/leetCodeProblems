from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: 
        if not root: return 0
        
        # Post order traversal DFS, starting with left node
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        # Return 1 plus the max depth between left and right
        return 1 + max(leftDepth, rightDepth)