class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ls=[]
        freq=Counter(nums)
        for i in nums:
            if freq[i]==1:
                ls.append(i)
        return ls

        