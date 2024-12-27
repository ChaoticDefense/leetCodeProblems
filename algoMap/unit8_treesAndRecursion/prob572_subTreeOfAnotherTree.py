# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

# Example 1:

# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:

# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

 

# Constraints:

#     The number of nodes in the root tree is in the range [1, 2000].
#     The number of nodes in the subRoot tree is in the range [1, 1000].
    
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkTree(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return checkTree(p.left, q.left) and checkTree(p.right, q.right)
        
        def has_subTree(root):
            if not root:
                return False
            
            return  has_subTree(root.left) or has_subTree(root.right, subRoot)
        
        return has_subTree(root, subRoot)
    
    
A = TreeNode(3)
B = TreeNode(4)
C = TreeNode(5)
D = TreeNode(1)
E = TreeNode(2)

A.left = B
A.right = C
B.left = D
B.right = E

print(Solution().isSubtree(A,B))