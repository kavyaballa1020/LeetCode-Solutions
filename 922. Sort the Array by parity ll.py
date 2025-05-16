class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even=[]
        odd=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        
        result=[]
        for i in range(len(nums)):
            if i%2==0:
                result.append(even.pop())
            else:
                result.append(odd.pop())
        return result
