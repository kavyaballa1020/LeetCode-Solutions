class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        # n=int(num)
        # while n %10==0:
        #     n=n/10
        # return str(n)
        
        a=num.rstrip("0")
        return a