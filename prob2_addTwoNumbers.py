# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


from helperFunctions.linkedLists import list_to_linkedlist, linkedlist_to_list, ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize list node with dummy value (for edge case of empty lists)
        dummy = ListNode()
        # Make "constructor" node that starts at head
        tail = dummy
        
        # Carry over digit will always be either 0 or 1
        r = 0
        
        # Do normal vertical addition when there are numbers in both lists
        while l1 and l2:
            # Add the 2 numbers plus the carry over value (if there is one)
            val = r + l1.val + l2.val
            
            # If the added nums are greater than 10, carry over the 1 and place the remainder as the value
            if val >= 10:
                r = 1
                val %= 10
            else:
                r = 0
            
            # Put the value at the end of the linked list
            tail.next = ListNode(val)
            tail = tail.next
            
            # Move the pointers on both numbers
            l1 = l1.next
            l2 = l2.next
        
        # Once there are no more digits in either number, determine if there are remaining digits in the other number
        if l1:
            bigP = l1 
        elif l2:
            bigP = l2
        else:
            bigP = None
        
        # If there are remaining digits, go through them
        if bigP: 
            # Only add up digits if there is a carry over number  
            while r == 1:
                if not bigP:
                    bigP = ListNode()
                val = r + bigP.val
                if val >= 10:
                    r = 1
                    val %= 10
                else:
                    r = 0
                    
                tail.next = ListNode(val)
                tail = tail.next  
                
                bigP = bigP.next

            # Otherwise, just place remaining digits at the end
            tail.next = bigP
            
        # If equal digits and last sum >= 10, place 1 in last digit (i.e. 5+5, 6+4, etc.)
        elif r == 1:
            tail.next = ListNode(r)
               
        return dummy.next
    
l1 = list_to_linkedlist([9,9,9,9,9,9,9])
l2 = list_to_linkedlist([9,9,9,9])

s = Solution()

list_sum = linkedlist_to_list(s.addTwoNumbers(l1, l2))
print(list_sum)