# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        slow = prev = fast = head
        for i in range(k-1):
            prev=prev.next
        fast=prev.next
        while fast:
            fast=fast.next
            slow=slow.next
        slow.val, prev.val= prev.val, slow.val
        return head