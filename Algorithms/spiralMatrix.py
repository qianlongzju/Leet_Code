class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        elements = []
        if len(matrix) == 0: return elements
        m, n = len(matrix), len(matrix[0])
        row, col = 0, -1
        while True:
            for i in range(n):
                col += 1
                elements.append(matrix[row][col])
            m -= 1
            if not m: break
            for i in range(m):
                row += 1
                elements.append(matrix[row][col])
            n -= 1
            if not n: break
            for i in range(n):
                col -= 1
                elements.append(matrix[row][col])
            m -= 1
            if not m: break
            for i in range(m):
                row -= 1
                elements.append(matrix[row][col])
            n -= 1
            if not n: break
        return elements
