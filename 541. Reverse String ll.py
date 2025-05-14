class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ls=list(s)
        for i in range(0,len(ls),2*k):
            ls[i:i+k]=reversed(ls[i:i+k])
        return ''.join(ls)