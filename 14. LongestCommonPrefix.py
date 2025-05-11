class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=strs[0]
        for i in strs[1:]:
            while i.find(prefix)!=0:
                prefix=prefix[:-1]
            if not prefix:
                return ""
        return prefix