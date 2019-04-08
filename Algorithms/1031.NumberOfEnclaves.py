class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        visited = set()
        reachable = 0
        m, n = len(A), len(A[0])
        def bfs(i, j):
            visited.add((i, j))
            q = [(i, j)]
            reach = False
            current = set()
            current.add((i, j))
            while q:
                x, y = q.pop(0)
                if x == 0 or x == m-1 or y == 0 or y == n-1:
                    reach = True
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < m and 0 <= yy < n and A[xx][yy] == 1 and (xx, yy) not in visited:
                        q.append((xx, yy))
                        visited.add((xx, yy))
                        current.add((xx, yy))
            if reach:
                return len(current)
            else:
                return 0
        count = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    count += 1
                    if (i, j) not in visited:
                        reachable += bfs(i, j)
        return count - reachable
