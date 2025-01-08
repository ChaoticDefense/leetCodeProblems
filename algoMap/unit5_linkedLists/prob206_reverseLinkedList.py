# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:

# Input: head = [1,2]
# Output: [2,1]

# Example 3:

# Input: head = []
# Output: []

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create two pointers: prev at None and curr at head
        prev = None
        curr = head
        
        # Keep looping until curr has been at each node
        while curr:
            # Move a temp pointer to the next node before doing anything
            t = curr.next
            
            # Change current node next to be previous node
            curr.next = prev
            
            # Current is now the new previous
            prev = curr
            
            # Move curr forward
            curr = t
        
        # At the end of looping prev is new head of reverse list
        return prev
    

A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
D = ListNode(4)
E = ListNode(5)

A.next = B
B.next = C
C.next = D
D.next = E

print(Solution().reverseList(A))