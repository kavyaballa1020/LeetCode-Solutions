class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        for i in nums:
            divisors=set()
            for j in range(1,int(i**0.5)+1):
                if i%j==0:
                    divisors.add(j)
                    divisors.add(i//j)
                if len(divisors)>4:
                    break
            if len(divisors)==4:
                total=total+sum(divisors)
        return total