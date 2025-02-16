class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq=Counter(nums)
        n=len(nums)
        ls=[]
        for i in nums:
            if freq[i]>n/2 and i not in ls:
                return i
