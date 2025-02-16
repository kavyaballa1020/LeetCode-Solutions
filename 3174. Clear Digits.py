class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls=[]
        for i in s:
            if i.isdigit():
                if ls:
                    ls.pop()
            else:
                ls.append(i)
        return "".join(ls)

