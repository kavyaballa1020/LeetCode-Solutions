class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        r=[]
        s=[]
        for i in nums:
            if i%2==0:
                r.append(i)
            else:
                s.append(i)
        return r+s