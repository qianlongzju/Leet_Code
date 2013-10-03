public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int m = obstacleGrid.length;
        if (m == 0) {
            return 0;
        }
        if (obstacleGrid[0][0] == 1) {
            return 0;
        }
        int n = obstacleGrid[0].length;
        int[][] path = new int[m][n];
        int i=0, j=0;
        for (i=0; i < m; i ++) {
            for (j=0; j < n; j ++) {
                path[i][j] = 1;
            }
        }
        for (i=0; i < m; i ++) {
            for (j=0; j < n; j ++) {
                if (obstacleGrid[i][j] == 1) {
                    path[i][j] = 0;
                }
                else if (i > 0 && j > 0) {
                    path[i][j] = path[i-1][j] + path[i][j-1];
                }
                else if (i > 0) {
                    path[i][j] = path[i-1][j];
                }
                else if (j > 0) {
                    path[i][j] = path[i][j-1];
                }
            }
        }
        return path[i-1][j-1];
    }
}