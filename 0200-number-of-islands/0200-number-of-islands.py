from collections import deque
class Solution(object):
    def numIslands(self, grid):

# with the help of BFS
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    dr, dc = dr + row, dc + col

                    if (dr < 0 or dc < 0 or dr >= rows or dc >= cols or grid[dr][dc] == "0" ):
                        continue
                    
                    q.append((dr, dc))
                    grid[dr][dc] = "0"
                    






        # traverse all the cell of the grid

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands


# Time complexity: O(m*n)
# Space complexity: O(min(m, n))