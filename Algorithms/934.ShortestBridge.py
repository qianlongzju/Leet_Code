class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        island, visited = set(), set()
        row, col = len(A), len(A[0])
        def find_island(i, j):
            q = [(i, j)]
            island.add((i, j))
            while q:
                i, j = q.pop(0)
                for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < row and 0 <= jj < col and A[ii][jj] == 1 and (ii, jj) not in island:
                        q.append((ii, jj))
                        island.add((ii, jj))
        
        find_first_island = False
        for i in range(row):
            for j in range(col):
                if A[i][j] == 1:
                    find_island(i, j)
                    find_first_island = True
                    break
            if find_first_island:
                break
                
        q = list(island)
        step = 0
        while q:
            size = len(q)
            for k in range(size):
                i, j = q.pop(0)
                for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    ii, jj = i + di, j + dj
                    if ii < 0 or ii >= row:
                        continue
                    if jj < 0 or jj >= col:
                        continue
                    if (ii, jj) in visited or (ii, jj) in island:
                        continue
                    if A[ii][jj] == 1:
                        return step
                    q.append((ii, jj))
                    visited.add((ii, jj))
            step += 1
