class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        M = len(matrix)
        N = len(matrix[0])
        setFirstRowZeroes = False
        setFirstColZeroes = False
        for i in range(M):
            if matrix[i][0] == 0:
                setFirstColZeroes = True
                break
        for j in range(N):
            if matrix[0][j] == 0:
                setFirstRowZeroes = True
                break
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, M):
            if matrix[i][0] == 0:
                for j in range(1, N):
                    matrix[i][j] = 0
        for j in range(1, N):
            if matrix[0][j] == 0:
                for i in range(1, M):
                    matrix[i][j] = 0
        if setFirstRowZeroes:
            for j in range(N):
                matrix[0][j] = 0
        if setFirstColZeroes:
            for i in range(M):
                matrix[i][0] = 0
        return matrix
