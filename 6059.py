class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        if grid[0][0] != '(':
            return False
        self.visited = set()
        return self.path(grid, len(grid[0]), len(grid), 0, 0, 1, 0, grid[0][0])

    def path(self, grid, n, m, i, j, left, right, p):
        if i == m-1 and j == n-1:
            return left == right
        left_res = False
        right_res = False
        if i+1 < m:
            new_left, new_right = left, right
            if grid[i+1][j] == '(':
                new_left += 1
            else:
                new_right += 1
            if new_left >= new_right:
                if (i+1, j, new_left, new_right) not in self.visited:
                    self.visited.add((i+1, j, new_left, new_right))
                    left_res = self.path(grid, n, m, i+1, j, new_left, new_right, p + grid[i+1][j])
        if j+1 < n:
            new_left, new_right = left, right
            if grid[i][j+1] == '(':
                new_left += 1
            else:
                new_right += 1
            if new_left >= new_right:
                if (i, j+1, new_left, new_right) not in self.visited:
                    self.visited.add((i, j+1, new_left, new_right))
                    right_res = self.path(grid, n, m, i, j+1, new_left, new_right, p + grid[i][j+1])
        return left_res or right_res
