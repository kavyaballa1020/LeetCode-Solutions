class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ls=[]
        for i in range(1,n+1):
            ls.append(i)
        
        s1=set(nums)
        s2=set(ls)
        s3=s2.difference(s1)
        
        list1=list(s3)

        return list1

