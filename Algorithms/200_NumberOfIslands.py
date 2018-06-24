class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
    
    def dfs(self, grid, i, j):
        grid[i][j] = '0'
        for a in range(-1, 2):
            b = 0
            ii = i + a
            jj = j + b
            if ii >= 0 and jj >= 0 and ii < len(grid) and jj < len(grid[i]) and grid[ii][jj] == '1':
                self.dfs(grid, ii, jj)
        for b in range(-1, 2):
            a = 0
            ii = i + a
            jj = j + b
            if ii >= 0 and jj >= 0 and ii < len(grid) and jj < len(grid[i]) and grid[ii][jj] == '1':
                self.dfs(grid, ii, jj)
        
