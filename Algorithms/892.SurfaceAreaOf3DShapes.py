class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        area = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    continue
                area += 2
                for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if nr < 0 or nc < 0 or nr >= N or nc >= N or grid[nr][nc] == 0:
                        nval = 0
                    else:
                        nval = grid[nr][nc]
                    area += max(grid[r][c] - nval, 0)
        return area
