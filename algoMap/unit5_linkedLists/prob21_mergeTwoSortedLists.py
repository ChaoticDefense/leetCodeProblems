# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:

# Input: list1 = [], list2 = []
# Output: []

# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create dummy node as a starting point and place curr there
        dummy = ListNode()
        curr = dummy
        
        # Make pointers that traverse list1 and list2
        l1 = list1
        l2 = list2
        
        # Loop while both l1 and l2 are not None
        while l1 and l2:
            # Place whichever node has lesser value onto output list
            # Whichever list was used, move its respective pointer
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            # No matter which was used, move curr to build output list   
            curr = curr.next
        
        # If l2 finished traversal and l1 has nodes left, just place remaining l1 nodes 
        if l1:
            curr.next = l1
        elif l2: # Likewise for l2
            curr.next = l2
         
        # List was built with head at dummy.next       
        return dummy.next