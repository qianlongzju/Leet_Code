class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == [] or grid[0] == []:
            return 0
        neighbours = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                p = 4
                for di, dj in neighbours:
                    ii, jj = i+di, j+dj
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 1:
                        p -= 1
                perimeter += p
        return perimeter
