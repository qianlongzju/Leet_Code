class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == []:
            return 0
        N = len(grid)
        area = 0
        for i in range(N):
            area += max(grid[i])
            area += N - grid[i].count(0)
        for j in range(N):
            area += max(grid[i][j] for i in range(N))
        return area
