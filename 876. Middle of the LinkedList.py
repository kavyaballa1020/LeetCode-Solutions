# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current=head
        count=0
        while current:
            count=count+1
            current=current.next
        current=head
        i=0
        while current:
            if i>=(count/2):
                return current
            else:
                current=current.next
            i+=1
