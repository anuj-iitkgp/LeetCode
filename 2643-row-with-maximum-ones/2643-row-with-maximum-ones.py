class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        n = len(mat)
        # count_1 = []

        # for i in range(n):
        #     count_1.append(sum(mat[i]))
        # max_ones = max(count_1)
        # if  max_ones > 0:
        #     return [count_1.index(max_ones), max_ones]
        # return [0, 0]

        max_row_idxx = 0
        max_ones_count = -1

        for i in range(n):
            ones_in_row = sum(mat[i])
            if ones_in_row > max_ones_count:
                max_ones_count = ones_in_row
                max_row_idx = i
        return [max_row_idx, max_ones_count]
        
        