class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        f=Counter(s)
        for i in range(0,len(s)-1):
            if int(s[i])==f[s[i]] and int(s[i+1])==f[s[i+1]] and s[i]!=s[i+1]:
                return s[i]+s[i+1]
              
        
        return ""

