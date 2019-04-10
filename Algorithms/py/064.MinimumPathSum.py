class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i and j:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
                elif i:
                    grid[i][j] += grid[i-1][j]
                elif j:
                    grid[i][j] += grid[i][j-1]
        return grid[m-1][n-1]
