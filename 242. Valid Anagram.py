class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq1=Counter(s)
        freq2=Counter(t)
        if len(s)==len(t):
            if freq1==freq2:
                return True
        return False

        