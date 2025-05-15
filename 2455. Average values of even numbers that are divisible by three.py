class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls=[]
        for i in nums:
            if i%3==0 and i%2==0:
                ls.append(i)
        if not ls:
            return 0
        return sum(ls)//len(ls)