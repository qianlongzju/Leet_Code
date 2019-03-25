class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix == []:
            return
        m, n = len(matrix), len(matrix[0])
        self.dp = [[-1] * n for i in range(m)]
        self.dp[0][0] = matrix[0][0]
        for i in range(1, m):
            self.dp[i][0] = self.dp[i-1][0] + matrix[i][0]
        for j in range(1, n):
            self.dp[0][j] = self.dp[0][j-1] + matrix[0][j]
        for i in range(1, m):
            for j in range(1, n):
                self.dp[i][j] = matrix[i][j] + self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1]
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 > 0 and col1 > 0:
            return self.dp[row2][col2] - self.dp[row2][col1-1] - self.dp[row1-1][col2] + self.dp[row1-1][col1-1]
        elif row1 == 0 and col1 == 0:
            return self.dp[row2][col2]
        elif row1 == 0:
            return self.dp[row2][col2] - self.dp[row2][col1-1]
        else:
            return self.dp[row2][col2] - self.dp[row1-1][col2]
            
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
