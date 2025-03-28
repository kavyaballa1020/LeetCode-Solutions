class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if ((nums[i] | nums[j]) & 1) == 0:
        #             return True
        # return False

        count=0
        for i in nums:
            if i%2==0:
                count+=1
            if count==2:
                return True
        return False