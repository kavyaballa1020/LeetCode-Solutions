class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n=len(nums)
        for i in range(0,n):
            if target==nums[i]:
                return i
        return -1