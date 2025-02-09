class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        even=[]
        odd=[]
        freq=Counter(s)
        for i in s:
            if freq[i]%2==0:
                even.append(freq[i])
            else:
                odd.append(freq[i])
        return max(odd)-min(even)

      