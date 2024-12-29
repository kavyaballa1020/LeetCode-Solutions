class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s1=""
        for i in s:
            if i.isalnum():
                s1=s1+i
        return s1==s1[::-1]
