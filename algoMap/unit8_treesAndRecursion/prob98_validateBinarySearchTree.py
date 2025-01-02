# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

#     The left
#     subtree
#     of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

 

# Example 1:

# Input: root = [2,1,3]
# Output: true

# Example 2:

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Global variable to keep track of status of BST, assume True initially
        isValid = [True]
        
        # In order traversal: Left, Node, Right 
        def inOrder(root, minimum, maximum):
            # At leaf, just return
            if not root:
                return
            
            # When going to the left, the local maximum will be the current root val
            # Local minimum does not change
            inOrder(root.left, minimum, root.val)
            
            # Process Node Here
            # Node vals must be increasing from in order traversal, and unique
            # If BST is already false just skip processing
            if root.val >= maximum or root.val <= minimum or isValid[0] is False:
                isValid[0] = False
                return
            
            # When going to the right  
            inOrder(root.right, root.val, maximum)
                
        inOrder(root, float('-inf'), float('inf'))
        
        return isValid[0]
    
A = TreeNode(2)
B = TreeNode(1)
C = TreeNode(3)

A.left = B
A.right = C

print(Solution().isValidBST(A))