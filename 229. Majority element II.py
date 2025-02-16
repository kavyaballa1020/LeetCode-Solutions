class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ls=[]
        freq=Counter(nums)
        for i in nums:
            if freq[i]>n/3 and i not in ls:
                ls.append(i)
        return ls

