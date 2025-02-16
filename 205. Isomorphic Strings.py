class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # s1=[]
        # t1=[]
        # for i in s:
        #     s1.append(s.index(i))
        # for j in t:
        #     t1.append(t.index(j))
        # return s1==t1

        return len(set(s))==len(set(t))==len(set(zip(s,t)))

        

