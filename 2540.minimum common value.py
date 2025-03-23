class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        set1=set(nums1)
        set2=set(nums2)
        ls=list(set1.intersection(set2))
        if ls:
            return min(ls)
        else:
            return -1