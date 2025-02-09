class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        sum1=(n*(n+1))//2
        freq=Counter(nums)
        duplicate=0
        for i in nums:
            if freq[i]==2:
                duplicate=i
                break
        r=sum1-(sum(nums)-duplicate)
        return [duplicate,r]