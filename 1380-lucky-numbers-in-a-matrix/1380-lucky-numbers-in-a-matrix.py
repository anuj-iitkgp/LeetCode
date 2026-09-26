class Solution(object):
    def luckyNumbers(self, matrix):
        transpose = [list(row) for row in zip(*matrix)]
        n, m = len(matrix), len(transpose)
        rmin = [min(matrix[i]) for i in range(n)]
        cmax = [max(transpose[i]) for i in range(m)]
        ans = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == rmin[i] and matrix[i][j] == cmax[j]:
                    ans.append(matrix[i][j])
        return ans
        