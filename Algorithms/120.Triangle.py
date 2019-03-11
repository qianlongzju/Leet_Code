class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal_1(self, triangle):
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

    def minimumTotal(self, triangle):
        dp = triangle[-1][:]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
                #triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return dp[0]
