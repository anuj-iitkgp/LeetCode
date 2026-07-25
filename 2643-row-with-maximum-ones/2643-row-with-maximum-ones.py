class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        n = len(mat)
        count_1 = []

        for i in range(n):
            count_1.append(sum(mat[i]))
        max_ones = max(count_1)
        if  max_ones > 0:
            return [count_1.index(max_ones), max_ones]
        return [0, 0]
        
        