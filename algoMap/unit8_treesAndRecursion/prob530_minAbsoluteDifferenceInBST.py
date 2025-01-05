# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

# Example 1:

# Input: root = [4,2,6,1,3]
# Output: 1

# Example 2:

# Input: root = [1,0,48,null,null,12,49]
# Output: 1

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        # Init output
        minDiff = [float('inf')]
        
        # Going to convert BST into sorted array to access last 2 elements
        arr = []
        
        # In order traversal: Left, Node, Right 
        def inOrder(root):
            if not root:
                return None
        
            inOrder(root.left)
            arr.append(root.val) # Add node val to array
            
            # Minimum difference is going to be between adjacent elements
            if len(arr) > 1:
                minDiff[0] = min(minDiff[0], arr[-1] - arr[-2])
                
            inOrder(root.right)
            
        inOrder(root)
        
        return minDiff[0]
    
    
A = TreeNode(4)
B = TreeNode(2)
C = TreeNode(6)
D = TreeNode(1)
E = TreeNode(3)

A.left = B
A.right = C
B.left = D
B.right = E

print(Solution().getMinimumDifference(A))