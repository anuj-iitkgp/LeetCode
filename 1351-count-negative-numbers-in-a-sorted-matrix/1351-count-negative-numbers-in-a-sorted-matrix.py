class Solution(object):
    def countNegatives(self, grid):
        n = len(grid)
        m = len(grid[0])

        ans = []
        for i in range(n):
            ans += grid[i]
        
        return sum(1 for num in ans if num < 0)




        # ans = 0
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] < 0:
        #             ans += 1
        # return ans
        