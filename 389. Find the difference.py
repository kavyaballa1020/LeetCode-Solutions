class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        c_s=Counter(s)
        c_t=Counter(t)
        for char in c_t:
            if c_t[char]>c_s[char]:
                return char

