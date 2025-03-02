class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<2:
            return False
        total=1
        sqrtt=int(math.sqrt(num))
        for i in range(2,sqrtt+1):
            if num%i==0:
                total=total+i
                if i!=(num//i):
                    total=total+(num//i)
        return total==num