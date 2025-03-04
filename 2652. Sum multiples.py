class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        ls=[]
        for i in range(1,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                ls.append(i)
        return sum(ls)