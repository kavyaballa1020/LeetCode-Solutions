class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left=0
        right=x
        ans=0
        while left<=right:
            mid=(left+right)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                left=mid+1
                ans=mid
            else:
                right=mid-1
        return ans