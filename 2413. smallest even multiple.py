class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n%2==0:
            return n
        if n==1:
            return 2
        for i in range(1,n):
            if (i*n)%2==0:
                return i*n