class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        n=len(nums)
        for j in range(1,n):
            if nums[j] != nums[j-1]:
                nums[i]=nums[j]
                i=i+1
        return i



        