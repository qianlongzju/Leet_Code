class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        result = [[0] * n for _ in range(m)]
        walls_a = [[0] * n for _ in range(m)]
        guards_a = [[0] * n for _ in range(m)]
        q = []
        #walls = set((i, j) for i, j in walls)
        #guards = set((i, j) for i , j in guards)
        for i, j in walls:
            walls_a[i][j] = 1
        for guard in guards:
            i, j = guard
            guards_a[i][j] = 1
            for d in range(4):
                q.append((i, j, d))
        d_r = [0, -1, 1, 0]
        d_c = [1, 0, 0, -1]
        visited = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(m)]
        while q:
            i, j, d = q.pop(0)
            #print(i, j, d)
            n_i, n_j = i + d_r[d], j + d_c[d]
            if n_i < 0 or n_i >= m or n_j < 0 or n_j >= n:
                continue
            if walls_a[n_i][n_j] == 1:
                continue
            if guards_a[n_i][n_j] == 1:
                continue
            if visited[n_i][n_j][d] == 1:
                continue
            visited[n_i][n_j][d] = 1
            #visited.add((n_i, n_j, d))
            result[n_i][n_j] = 1
            q.append((n_i, n_j, d))
        #print(result)
        return m*n-len(guards)-len(walls)-sum(sum(row) for row in result)
            
