class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=[]
        for i in s:
            if i=='i':
                result.reverse()
            else:
                result.append(i)
        return ''.join(result)
        