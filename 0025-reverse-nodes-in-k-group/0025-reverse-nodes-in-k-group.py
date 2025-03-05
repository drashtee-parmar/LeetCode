# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k == 1:
            return head  # No need to reverse if k=1 or empty list
        
        # Step 1: Count total nodes
        temp, n = head, 0
        while temp:
            n += 1
            temp = temp.next
        
        # Step 2: Dummy node for easy handling
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        curr = head

        # Step 3: Reverse k nodes at a time
        while n >= k:
            prev, tail = None, curr
            for _ in range(k):  # Reverse `k` nodes
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            # Connect the reversed segment to the previous part
            prev_group_end.next = prev
            tail.next = curr
            prev_group_end = tail  # Move prev_group_end to the last node of reversed group
            
            # Reduce count by `k`
            n -= k
        
        return dummy.next  # New head