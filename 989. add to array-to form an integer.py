class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        num1=int("".join(map(str,num)))
        sum=num1+k
        return list(map(int,str(sum)))