# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:

# Input: lists = []
# Output: []

# Example 3:

# Input: lists = [[]]
# Output: []

from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        # Init heap
        heap = []
        
        # Push heads of each list into heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        # Create dummy node for output   
        dummy = ListNode()
        curr = dummy
        
        # Keep looping until heap is depleted     
        while heap:
            # Pop off smallest node and unpack index and actual node ref
            _, i, node = heapq.heappop(heap)
            
            # Put node next in output chain
            curr.next = node
            curr = curr.next
            
            # Move to next node from head that was put in output
            node = node.next
            
            # If next node is not None, push to the heap
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        # Return output of actual list    
        return dummy.next
        

# Converts a list [1,2,3] to linked list (1->2->3)
def list_to_linkedlist(arr):
    # If empty list, return None
    if not arr:
        return None
    # Head is the beginning pointer which contains whole list
    # Initializes as arr[0] -> None
    head = ListNode(arr[0])
    
    # Create "builder pointer" that starts at the head of the linked list (starts with value and next of head)
    current = head
    
    # Iterate over the rest of the values in arr which "builds" the linked list
    for val in arr[1:]:
        # For iterations of current, current.next is equal to None, but then constructs a new list node with the value at arr which then points to None
        current.next = ListNode(val)
        # Move current to the newly constructed list node, then repeat
        current = current.next
     
    # The entire time, head has been growing its linked list thanks to the constructor "current"
    return head    

lists = [[1,4,5],[1,3,4],[2,6]]

for i in range(len(lists)):
    lists[i] = list_to_linkedlist(lists[i])
    
print(Solution().mergeKLists(lists))