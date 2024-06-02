from helperFunctions.linkedLists import list_to_linkedlist, linkedlist_to_list, ListNode

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next

# Convert lists to linked lists
l1 = list_to_linkedlist([1, 2, 4])
l2 = list_to_linkedlist([1, 3, 4])

s = Solution()
merged_head = s.mergeTwoLists(l1, l2)

# Convert the merged linked list back to a list for easy printing
merged_list = linkedlist_to_list(merged_head)
print(merged_list)