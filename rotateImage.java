public class Solution {
    public void rotate(int[][] matrix) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int n = matrix.length;
        for (int i=0; i < n/2; i++) {
            for (int j=0; j < n/2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n-1-j][i];
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j];
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i];
                matrix[j][n-1-i] = temp;
            }
        }
        if (n%2 == 1) {
            for (int i=0; i < n/2; i++) {
                int temp = matrix[i][n/2];
                matrix[i][n/2] = matrix[n/2][i];
                matrix[n/2][i] = matrix[n-1-i][n/2];
                matrix[n-1-i][n/2] = matrix[n/2][n-1-i];
                matrix[n/2][n-1-i] = temp;
            }
        }
    }
}
