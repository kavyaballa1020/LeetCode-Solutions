class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list1=[]
        for i in nums:
            if i%2==0:
                list1.append(i)
        freq=Counter(list1)
        if not list1:
            return -1
        maxVal=max(freq.values())
        minVal=None
        for i in freq:
            if freq[i]==maxVal:
                if minVal is None or i<minVal:
                    minVal=i
        return minVal

