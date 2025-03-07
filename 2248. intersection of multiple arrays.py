class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        set1=set(nums[0])
        for i in nums[1:]:
            set1.intersection_update(i)
        return sorted(list(set1))
