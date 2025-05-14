class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls=s.split(" ")
        for i in range(len(ls)):
            ls[i]=ls[i][::-1]
        return " ".join(ls)