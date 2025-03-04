class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum=max(nums)
        for i in nums:
            if maximum != i and maximum < 2*i:
                return -1
        return nums.index(maximum)