class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even=[]
        odd=[]
        i = 0
        while i < len(nums):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
            i += 1
        even.sort()
        odd.sort(reverse=True)
        e=0
        o=0
        result=[]
        for i in range(len(nums)):
            if i%2==0:
                result.append(even[e])
                e+=1
            else:
                result.append(odd[o])
                o+=1
        return result