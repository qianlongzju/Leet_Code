#include <iostream>
#include <vector>
#include "string"
using namespace std;
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int m = obstacleGrid.size();
        if (m == 0) {
            return 0;
        }
        if (obstacleGrid[0][0] == 1) {
            return 0;
        }
        int n = obstacleGrid[0].size();
        vector<vector<int> > path(m, vector<int>(n, 1));
        int i=0, j=0;
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
};
int main(int argc, char const *argv[])
{
    vector<vector<int> > obstacleGrid(3, vector<int>(3, 0));
    obstacleGrid[1][1] = 1;
    Solution s;
    cout << s.uniquePathsWithObstacles(obstacleGrid) << endl;
    return 0;
}
