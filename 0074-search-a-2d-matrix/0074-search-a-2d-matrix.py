class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """


        n = len(matrix)
        m = len(matrix[0])
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] == target:
        #             return True
        # return False

        # Time Complexity O(m*n)
        low = 0
        high = m * n - 1
        while low <= high:
            mid = low + (- low + high) // 2

            if matrix[mid / m][mid %m] == target:
                return True
            elif matrix[mid / m][mid %m] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
            