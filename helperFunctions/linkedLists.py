# Definition for singly-linked list.
class ListNode:
    # Initializes as (0 - > None)
    # If a value argument is passed, initializes as (val -> None)
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

# Converts linked lists back to regular lists
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result