class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n=len(arr)
        freq=Counter(arr)
        occurences=freq.values()
        return len(occurences)==len(set(occurences))
      
        