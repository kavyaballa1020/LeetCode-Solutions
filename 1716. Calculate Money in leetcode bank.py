class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=0
        monday=1
        day=monday
        for i in range(1,n+1):
            sum+=day
            if i%7==0:
                monday+=1
                day=monday
            else:
                day+=1
        return sum