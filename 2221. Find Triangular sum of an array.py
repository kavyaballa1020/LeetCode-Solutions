class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums)>1:
            array=[]
            for i in range(len(nums)-1):
                sum=(nums[i]+nums[i+1])%10
                array.append(sum)
            nums=array
        return nums[0]

