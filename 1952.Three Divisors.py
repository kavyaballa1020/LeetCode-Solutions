class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count=count+1
        return count==3