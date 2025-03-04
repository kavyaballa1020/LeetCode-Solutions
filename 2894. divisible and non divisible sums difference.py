class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        ls1=[]
        ls2=[]
        for i in range(1,n+1):
            if i % m != 0:
                ls1.append(i)
            else:
                ls2.append(i)
        return sum(ls1)-sum(ls2)