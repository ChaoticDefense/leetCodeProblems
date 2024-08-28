from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Global variable maintaining status of balanced tree
        balanced = [True]
        
        # Function to get height of current root
        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            # Check left nodes first recursively
            # If after left node checks and tree is not balanced,
            # just return dummy value since it's pointless to continue
            leftHeight = height(root.left)
            if balanced[0] is False:
                return 0
            
            # Check right nodes (same optimization as above)
            rightHeight = height(root.right)
            if balanced[0] is False:
                return 0
            
            # Normal balanced check, height of left and right
            # does not differ by more than 1
            if abs(leftHeight - rightHeight) > 1:
                balanced[0] = False
                return 0
            
            # Return height of current root for further checks
            return 1 + max(leftHeight, rightHeight)
        
        # Only run subfunction on root, recursion happens within it
        height(root)
        
        # Return global variable (whether it changed or not)
        return balanced[0]
    
A = TreeNode(3)
B = TreeNode(9)
C = TreeNode(20)
D = TreeNode(15)
E = TreeNode(7)

A.left = B
A.right = C
C.left = D
C.right = E

print(Solution().isBalanced(A))