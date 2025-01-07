# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:

# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

 

# Constraints:

#     The number of nodes in the list is in the range [0, 300].
#     -100 <= Node.val <= 100
#     The list is guaranteed to be sorted in ascending order.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start at head and keep head intact
        curr = head
        
        # Keep looping until both curr and curr.next are not None
        while curr and curr.next:
            # If next node val is same as current,
            # Move next node to be next-next node
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else: # Only move to next node if current not same val as next
                curr = curr.next
        
        # Return head of linked list
        return head