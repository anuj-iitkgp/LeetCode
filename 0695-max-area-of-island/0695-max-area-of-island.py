class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])
        ans = 0
        def dfs(r, c, ones):
            nonlocal ans
            if r >= row or r < 0 or c < 0 or c >= col or grid[r][c] != 1:
                return ones
            
            ones += 1

            ans = max(ans, ones)
            grid[r][c] = 0
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for x, y in directions:
                ones = dfs(x + r, y + c, ones)
            return ones
  

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    dfs(r, c, 0)
        return ans