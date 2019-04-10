class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(matrix), len(matrix[0])
        result = [[-1] * col for i in range(row)]
        q, visited = [], set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
                    result[i][j] = 0
        step = 0
        while q:
            step += 1
            size = len(q)
            for i in range(size):
                x, y = q.pop(0)
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < row and 0 <= yy < col and (xx, yy) not in visited:
                        result[xx][yy] = step
                        visited.add((xx, yy))
                        q.append((xx, yy))
        return result
