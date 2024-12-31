# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Build up array to essentially convert BST into sorted array
        ans = [];
        
        # In order traversal: Left, Node, Right 
        def inOrder(root):
            if not root:
                return None
        
            inOrder(root.left)
            ans.append(root.val) # Add node val to array
            inOrder(root.right)
        
            
        inOrder(root)
        
        # Kth smallest number will be k-1 index in ans array
        return ans[k-1]
    
A = TreeNode(3)
B = TreeNode(1)
C = TreeNode(4)
D = TreeNode(2)

A.left = B
A.right = C
B.right = D

k = 2
print(Solution().kthSmallest(A,k))
