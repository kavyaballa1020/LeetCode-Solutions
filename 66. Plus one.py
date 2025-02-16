class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=int("".join(map(str,digits)))+1
        n1=str(n)
        return list(map(int,n1))
        

