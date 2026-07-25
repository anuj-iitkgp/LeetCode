class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # n = len(matrix)
        # m = len(matrix[0])
        # zero_row = [False] * n
        # zero_col = [False] * m

        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] == 0:
        #             zero_row[i] = True
        #             zero_col[j] = True

        # for i in range(n):
        #     for j in range(m):
        #         if zero_row[i] or zero_col[j]:
        #             matrix[i][j] = 0
        # return matrix  
        # Time Complexity O(m * n) and Space Complexity O(m + n)

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.helper(matrix, i - 1, j, "U")
                    self.helper(matrix, i + 1, j, "D")
                    self.helper(matrix, i, j - 1, "L")
                    self.helper(matrix, i , j + 1, "R")
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "*":
                    matrix[i][j] = 0
        return matrix

    def helper(self, matrix, m, n, direction):
        if (0 <= m < len(matrix)) and (0 <= n < len(matrix[0])) and matrix[m][n] != 0:
            matrix[m][n] = "*"

            if direction == "U":
                self.helper(matrix, m - 1, n, "U")
            elif direction == "D":
                self.helper(matrix, m + 1, n, "D")
            elif direction == "L":
                self.helper(matrix, m, n - 1, "L")
            else:
                self.helper(matrix, m , n + 1, "R")
