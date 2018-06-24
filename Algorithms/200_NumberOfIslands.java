class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for(int i=0; i < grid.length; i++) {
            for(int j=0; j < grid[i].length; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    count++;
                }
            }
        }
        return count;
    }
    void dfs(char[][] grid, int i, int j) {
        grid[i][j] = '0';
        for (int a=-1; a <= 1; a++) {
            int b = 0;
            int ii = i + a;
            int jj = j + b;
            if (ii >= 0 && jj >= 0 && ii < grid.length && jj < grid[i].length && grid[ii][jj] == '1') {
                dfs(grid, ii, jj);
            }
        }
        for (int b=-1; b <= 1; b++) {
            int a = 0;
            int ii = i + a;
            int jj = j + b;
            if (ii >= 0 && jj >= 0 && ii < grid.length && jj < grid[i].length && grid[ii][jj] == '1') {
                dfs(grid, ii, jj);
            }
        }
    }
}
