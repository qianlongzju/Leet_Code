class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            step = 1
            while r+step < m and step < n:
                if matrix[r+step][step] != matrix[r][0]:
                    return False
                step += 1
        for c in range(1, n):
            step = 1
            while step < m and c+step < n:
                if matrix[step][c+step] != matrix[0][c]:
                    return False
                step += 1
        return True
