class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        ls=[]
        current=0
        for i in nums:
            current=(current*2+i)%5
            ls.append(current==0)
        return ls