# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
 # Initialize a dummy node to build the resulting linked list
        dummy = ListNode()
        current = dummy
        carry = 0
        
        # Traverse through both linked lists until all nodes and carry are processed
        while l1 or l2 or carry:
            # Get the value from l1 if available
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            
            # Get the value from l2 if available
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            
            # Calculate the sum and update the carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create a new node with the digit value and move the pointer
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next nodes in l1 and l2 if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the head of the new linked list (next to the dummy node)
        return dummy.next
# Time Complexity: O(n), where n is the maximum length of the two linked lists. We process each node once.
# Space Complexity: O(n), as we create a new linked list to store the result.