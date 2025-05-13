# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        current=dummy
        set1=set(nums)
        while current.next:
            if current.next.val in set1:
                current.next=current.next.next
            else:
                current=current.next
        return dummy.next

