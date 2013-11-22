#include "leetcode.h"
class Solution {
public:
    int minPathSum(vector<vector<int> > &grid) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int i, j;
        for (i=0; i < grid.size(); i++) {
            for (j=0; j < grid[0].size(); j++) {
                if (i > 0 && j >0) {
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1]);
                }
                else if (i > 0) {
                    grid[i][j] += grid[i-1][j];
                }
                else if (j > 0) {
                    grid[i][j] += grid[i][j-1];
                }
            }
        }
        return grid[i-1][j-1];
    }
    int min(int a, int b) {
        if (a > b) {
            return b;
        }
        else {
            return a;
        }
    }
};
int main(int argc, char const *argv[])
{
    vector<vector<int> > v;
    vector<int> a;
    a.push_back(0);
    v.push_back(a);
    Solution s;
    cout << s.minPathSum(v) << endl;
    return 0;
}
