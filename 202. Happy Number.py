class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        set1=set()
        sum=0
        r=0
        while n!=1 and n not in set1:
            sum=0
            set1.add(n)
            while n>0:
                r=n%10
                sum=sum+r*r
                n=n/10
            n=sum
        if n==1:
            return True
        else:
            return False