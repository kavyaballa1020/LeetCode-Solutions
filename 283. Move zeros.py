class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                nums[pos]=nums[i]
                if pos!=i:
                    nums[i]=0
                pos=pos+1

