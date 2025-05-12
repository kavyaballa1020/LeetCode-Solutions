# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # current=head
        # values=[]
        # prev=None

        # while current:
        #     values.append(current.val)
        #     current=current.next
        
        # current=head
        # while current:
        #     nextnode=current.next
        #     current.next=prev
        #     prev=current
        #     current=nextnode
        
        # current =prev
        # for i in values:
        #     if i!=current.val:
        #         return False
        #     current=current.next
        # return True

        values=[]
        current=head
        while current:
            values.append(current.val)
            current=current.next
        return values==values[::-1]