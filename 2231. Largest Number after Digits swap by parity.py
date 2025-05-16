class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums=[]
        for i in str(num):
            nums.append(i)
        i=0
        even=[]
        odd=[]
        while i<len(nums):
            if int(nums[i]) % 2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
            i+=1
        even.sort(reverse=True)
        odd.sort(reverse=True)
        result=[]
        e=0
        o=0
        i=0
        while i<len(nums):
            if int(nums[i])%2==0:
                result.append(even[e])
                e+=1
            else:
                result.append(odd[o])
                o+=1
            i+=1
        string=""
        for i in result:
            string+=i
        return int(string)