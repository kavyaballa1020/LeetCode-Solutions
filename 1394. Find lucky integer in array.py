class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lucky=-1
        for i in set(arr):
            if arr.count(i)==i:
                lucky=max(lucky,i)
        return lucky
