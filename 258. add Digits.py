class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum=0
        r=0
        while num/10!=0:
            sum=0
            while num>0:
                r=num%10
                sum=sum+r
                num=num/10
            num=sum
        return num