class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        row, col = len(grid), len(grid[0])
        def dfs(x, y):
            grid[x][y] = '-1'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                xx, yy = x + dx, y + dy
                if 0 <= xx < row and 0 <= yy < col and grid[xx][yy] == '1':
                    dfs(xx, yy)

        def bfs(x, y):
            q, visited = [(x, y)], {(x, y)}
            step = 0
            while q:
                step += 1
                size = len(q)
                for i in range(size):
                    x, y = q.pop(0)
                    grid[x][y] = '-1'
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        xx, yy = x + dx, y + dy
                        if 0 <= xx < row and 0 <= yy < col and grid[xx][yy] == '1' and (xx, yy) not in visited:
                            q.append((xx, yy))
                            visited.add((xx, yy))
        count = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1':
                    bfs(x, y)
                    count += 1
        return count
