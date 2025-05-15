class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        n1=0
        n2=1
        n3=1
        while n!=2:
            n4=n1+n2+n3
            n1=n2
            n2=n3
            n3=n4
            n-=1
        return n4