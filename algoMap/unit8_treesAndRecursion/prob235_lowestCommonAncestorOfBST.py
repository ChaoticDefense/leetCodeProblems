# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Example 2:

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Global variable, init as the root since it will always exist
        lca = [root]
        
        # Helper function
        def bstTraversal(root):
            if not root:
                return None
            
            # If current node is greater than BOTH p and q, the lowest common ancestor is to the left
            if root.val > p.val and root.val > q.val:
                bstTraversal(root.left)
            # Likewise, LCA will be to the right if less than BOTH p and q
            elif root.val < p.val and root.val < q.val:
                bstTraversal(root.right)
            else:
            # You have found the LCA since neither criteria above were met
                lca[0] = root
        
        bstTraversal(root)
        return lca[0]
    
A = TreeNode(6)
B = TreeNode(2)
C = TreeNode(8)
D = TreeNode(0)
E = TreeNode(4)
F = TreeNode(7)
G = TreeNode(9)
H = TreeNode(3)
I = TreeNode(5)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G
E.left = H
E.right = I

print(Solution().lowestCommonAncestor(A, F, F).val)