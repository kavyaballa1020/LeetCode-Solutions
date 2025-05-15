class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        n1=0
        n2=1
        if n==0:
            return 0
        elif n==1:
            return 1
        
        while n>1:
            n3=n1+n2
            n1=n2
            n2=n3
            n=n-1
        return n3
