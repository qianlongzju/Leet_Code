class UnionFind(object):
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m*n)
        self.rank = [0] * (m*n)
        for i in range(m):
            for j in range(n):
                self.parent[i*n + j] = i*n + j
                self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = set()
        n = len(M)
        def bfs(i, j):
            visited.add(i)
            visited.add(j)
            q = [i, j]
            while q:
                k = q.pop(0)
                for h in range(n):
                    if M[k][h] == 1 and h not in visited:
                        q.append(h)
                        visited.add(h)
            
        count = 0
        for i in range(n):
            for j in range(i, n):
                if M[i][j] == 1 and i not in visited and j not in visited:
                    count += 1
                    bfs(i, j)
        return count

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        uf = UnionFind([[1] * n])
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1:
                    uf.union(i, j)
        return uf.count
