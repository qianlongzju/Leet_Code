public class Solution {
    public int[][] generateMatrix(int n) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int[][] result = new int[n][n];
        int k=1;
        for (int i=0; i < n/2; i++) {
            int step = n-1-2*i;
            for (int j=0; j < step; j++) {
                result[i][i+j] = k++;
            }
            for (int j=0; j < step; j++) {
                result[i+j][n-1-i] = k++;
            }
            for (int j=0; j < step; j++) {
                result[n-1-i][n-1-(i+j)] = k++;
            }
            for (int j=0; j < step; j++) {
                result[n-1-(i+j)][i] = k++;
            }
        }
        if (n%2 == 1) {
            result[n/2][n/2] = k++;
        }
        return result;
    }
}
