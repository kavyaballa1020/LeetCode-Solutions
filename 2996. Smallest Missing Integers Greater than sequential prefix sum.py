class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                total+=nums[i]
            else:
                break
        n=set(nums)
        while total in nums:
            total+=1
        return total