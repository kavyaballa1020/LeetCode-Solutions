class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq=Counter(nums)
        for i in nums:
            if freq[i]==1:
                return i

