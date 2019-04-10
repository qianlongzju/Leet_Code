class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        paths = [[1 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    paths[i][j] = 0
                elif i and j:
                    paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
                elif i:
                    paths[i][j] = paths[i - 1][j]
                elif j:
                    paths[i][j] = paths[i][j - 1]
        return paths[m - 1][n - 1]
