class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1=[]
        for i in nums:
            x=i*i
            num1.append(x)
        num1.sort()
        return num1