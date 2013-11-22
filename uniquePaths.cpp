#include "leetcode.h"
public class Solution {
    public int uniquePaths(int m, int n) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int[][] path = new int[m][n];
        int i=0, j=0;
        for (i=0; i < m; i ++) {
            for (j=0; j < n; j ++) {
                path[i][j] = 1;
            }
        }
        for (i=0; i < m; i ++) {
            for (j=0; j < n; j ++) {
                if (i > 0 && j > 0) {
                    path[i][j] = path[i-1][j] + path[i][j-1];
                }
            }
        }
        return path[i-1][j-1];
    }
}
