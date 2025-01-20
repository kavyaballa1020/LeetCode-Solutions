class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum=min(nums)
        maximum=max(nums)
        ls=[]
        for i in range(1,minimum+1):
            if maximum % i == 0 and minimum % i == 0:
                ls.append(i)
        return max(ls)