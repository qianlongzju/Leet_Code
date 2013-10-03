public class Solution {
    public int minPathSum(int[][] grid) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int i=0, j=0;
        for (i=0; i < grid.length; i++) {
            for (j=0; j < grid[0].length; j++) {
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
}
