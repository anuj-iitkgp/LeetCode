class Solution(object):
    def numIslands(self, grid):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        row = len(grid)
        col = len(grid[0])
        isIsland = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

            
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r, c)
                    isIsland += 1

        return isIsland 

