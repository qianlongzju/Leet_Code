class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if matrix == [] or matrix[0] == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        mapping = {}
        visited = set()
        def dfs(i, j):
            diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            maximum = 0
            for di, dj in diff:
                ii, jj = i + di, j + dj
                if 0 <= ii < m and 0 <= jj < n and matrix[ii][jj] < matrix[i][j]:
                    if (ii, jj) in mapping:
                        maximum = max(maximum, mapping[(ii, jj)])
                    else:
                        maximum = max(maximum, dfs(ii, jj))
            mapping[(i, j)] = maximum + 1
            return maximum + 1
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in mapping:
                    dfs(i, j)
        return max(mapping.values())
