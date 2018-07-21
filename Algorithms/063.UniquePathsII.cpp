class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid) {
        int m = obstacleGrid.size();
        if (m == 0) return 0;
        int n = obstacleGrid[0].size();
        vector<vector<int> > path(m, vector<int>(n, 1));
        for (int i = 0; i < m; i ++) {
            for (int j = 0; j < n; j ++) {
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
        return path[m-1][n-1];
    }
};
