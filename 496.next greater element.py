class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ls = []
        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:  
                    found = True
                if found and nums2[j] > nums1[i]: 
                    ls.append(nums2[j])
                    break
            else:
                ls.append(-1)  
        return ls
