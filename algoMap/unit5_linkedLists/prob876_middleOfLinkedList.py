# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start slow and fast pointers at head
        slow = fast = head
        
        # Keep looping until either fast or fast.next is None
        # Fast moves twice as much as slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # When fast reaches end of list, slow is at middle node
        return slow
    
A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
D = ListNode(4)
E = ListNode(5)
F = ListNode(6)

A.next = B
B.next = C
C.next = D
D.next = E
# E.next = F

print(Solution().middleNode(A))