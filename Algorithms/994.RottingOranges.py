class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = []
        minutes = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
        next_q = []
        visited = set()
        minute = 0
        while q:
            print q, next_q
            for i, j in q:
                minutes[i][j] = minute
                visited.add((i, j))
                for ii, jj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    new_i, new_j = i + ii, j + jj
                    if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]):
                        continue
                    if (new_i, new_j) in visited or (new_i, new_j) in next_q or (new_i, new_j) in q:
                        continue
                    if grid[new_i][new_j] != 1:
                        continue
                    next_q.append((new_i, new_j))
            minute += 1
        
            q, next_q = next_q, []
        max_minutes = 0
        print minutes
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if minutes[i][j] == -1:
                        return -1
                    max_minutes = max(max_minutes, minutes[i][j])
        return max_minutes
