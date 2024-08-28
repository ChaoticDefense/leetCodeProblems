from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = [0]
        
        # Helper fucntion to keep track of height of current root
        def height(root):
            if not root:
                return 0
            
            # Check left, then right
            leftDepth = height(root.left)
            rightDepth = height(root.right)
            
            # Current diameter is leftDepth + rightDepth
            max_d[0] = max(max_d[0], leftDepth + rightDepth)
            
            # Return height of current root
            return 1 + max(leftDepth, rightDepth)
            
        
        height(root)
        
        return max_d[0]
    
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5) 

A.left = B
A.right = C
B.left = D
B.right = E

print(Solution().diameterOfBinaryTree(A))