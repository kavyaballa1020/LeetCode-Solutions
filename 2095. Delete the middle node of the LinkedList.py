# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None
        current=head
        count=0
        while current:
            count+=1
            current=current.next
        current=head
        mid=count//2
        current=head
        for i in range(mid-1):
            current=current.next
        current.next=current.next.next
        return head
            

        