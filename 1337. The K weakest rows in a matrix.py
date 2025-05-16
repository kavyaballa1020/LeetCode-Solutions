class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        count=[]
        for i,row in enumerate(mat):
            add=sum(row)
            count.append((add,i))
        count.sort()
        result=[]
        for i in range(k):
            result.append(count[i][1])
        return result