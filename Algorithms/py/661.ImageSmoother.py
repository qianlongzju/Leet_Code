class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(M), len(M[0])
        result = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                s, count = 0, 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ii, jj = i+di, j+dj
                        if 0 <= ii < m and 0 <= jj < n:
                            s += M[ii][jj]
                            count += 1
                result[i][j] = s // count
        return result
