class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0
        self.visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in self.visited:
                    maxArea = max(maxArea, self.bfs(grid, i, j))
        return maxArea
        
    def bfs(self, grid, i, j):
        area = 0
        q = [(i, j)]
        while q:
            i_0, j_0 = q.pop(0)
            self.visited.add((i_0, j_0))
            area += 1
            for ii, jj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                i, j = i_0 + ii, j_0 + jj
                if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1 and (i, j) not in self.visited and (i, j) not in q:
                    q.append((i, j))
        return area
        
