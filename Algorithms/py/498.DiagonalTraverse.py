class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [] or matrix[0] == []:
            return []
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        result = []
        direction = 0
        diff = [(-1, 1), (1, 0), (1, -1), (0, 1)]
        while True:
            result.append(matrix[i][j])
            if len(result) == m * n:
                break
            i += diff[direction][0]
            j += diff[direction][1]
            while i < 0 or i >= m or j < 0 or j >= n:
                direction = (direction + 1) % 4
                i += diff[direction][0]
                j += diff[direction][1]
            if direction == 1 or direction == 3:
                direction = (direction + 1) % 4
        return result
