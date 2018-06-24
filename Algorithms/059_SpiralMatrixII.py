class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if n == 0: return []
        matrix = [[0 for i in range(n)] for j in range(n)]
        row, col = 0, -1
        m = n
        k = 1
        while True:
            for i in range(n):
                col += 1
                matrix[row][col] = k
                k += 1
            m -= 1
            if not m: break
            for i in range(m):
                row += 1
                matrix[row][col] = k
                k += 1
            n -= 1
            if not n: break
            for i in range(n):
                col -= 1
                matrix[row][col] = k
                k += 1
            m -= 1
            if not m: break
            for i in range(m):
                row -= 1
                matrix[row][col] = k
                k += 1
            n -= 1
            if not n: break
        return matrix

        
