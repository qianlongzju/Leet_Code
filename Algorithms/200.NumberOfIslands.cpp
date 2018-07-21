class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for(int i=0; i < grid.size(); i++) {
            for(int j=0; j < grid[i].size(); j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    count++;
                }
            }
        }
        return count;
    }
    void dfs(vector<vector<char>>& grid, int i, int j) {
        grid[i][j] = '0';
        for (int a=-1; a <= 1; a++) {
            int b = 0;
            int ii = i + a;
            int jj = j + b;
            if (ii >= 0 && jj >= 0 && ii < grid.size() && jj < grid[i].size() && grid[ii][jj] == '1') {
                dfs(grid, ii, jj);
            }
        }
        for (int b=-1; b <= 1; b++) {
            int a = 0;
            int ii = i + a;
            int jj = j + b;
            if (ii >= 0 && jj >= 0 && ii < grid.size() && jj < grid[i].size() && grid[ii][jj] == '1') {
                dfs(grid, ii, jj);
            }
        }
    }
};
