class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index={}
        for i, value in enumerate(nums):
            if value in index and i-index[value]<=k:
                return True
            index[value]=i
        return False