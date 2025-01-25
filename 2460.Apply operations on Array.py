class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        c=0
        ls=[]
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        for i in nums:
            if i!=0:
                ls.append(i)
            else:
                c=c+1
        for i in range(c):
            ls.append(0)
        return ls