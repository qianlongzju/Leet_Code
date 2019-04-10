class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        side = [[0] * n for i in range(m)]
        
        result = 0
        for i in range(0, m):
            if matrix[i][0] == '1':
                side[i][0] = 1
                result = 1
        for j in range(0, n):
            if matrix[0][j] == '1':
                side[0][j] = 1
                result = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    continue
                side[i][j] = min(min(side[i-1][j-1], side[i-1][j]), side[i][j-1]) + 1
                result = max(result, side[i][j])
        return result * result
