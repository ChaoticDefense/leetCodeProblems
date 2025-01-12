# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:

# Input: head = [1], n = 1
# Output: []

# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)    
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Make dummy node that points at head
        dummy = ListNode()
        dummy.next = head
        
        # Starting at dummy node
        slow = fast = dummy
        
        # Starting at dummy node, so have fast have a gap of n+1 from slow
        for _ in range(n+1):
            fast = fast.next
        
        # Keep looping until fast reaches end of list   
        while fast:
            slow = slow.next
            fast = fast.next
           
        # Have the next node at slow be the next-next node, effectively removing the nth node 
        slow.next = slow.next.next
        
        # Return new head
        return dummy.next
    
A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
D = ListNode(4)
E = ListNode(5)

A.next = B
B.next = C
C.next = D
D.next = E

n = 2
print(Solution().removeNthFromEnd(A,n))