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
