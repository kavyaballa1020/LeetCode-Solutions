class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        list1 = list(num)
        even=0
        odd=0
        for i in range(0,len(list1)):
            if i%2==0:
                even=even+int(list1[i])
            else:
                odd=odd+int(list1[i])
        if even==odd:
            return True
        else:
            return False