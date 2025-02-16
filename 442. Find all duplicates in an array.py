class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq=Counter(nums)
        ls=[]
        for i in nums:
            if freq[i]==2 and i not in ls:
                ls.append(i)
        return ls