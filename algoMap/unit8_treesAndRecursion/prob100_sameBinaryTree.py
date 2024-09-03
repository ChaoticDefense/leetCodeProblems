from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # At leaf node at both tree
        if not p and not q:
            return True
        
        # At leaf at one, but not other
        if not p or not q:
            return False
        
        # Comparing values at both roots
        if p.val != q.val:
            return False
        
        # Recursive going down both trees in the same directions
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, p.right)
    
    
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)

A.left = B
A.right = C

A2 = TreeNode(1)
B2 = TreeNode(2)
C2 = TreeNode(3)

A2.left = B2
A2.right = C2

print(Solution().isSameTree(A, A2))