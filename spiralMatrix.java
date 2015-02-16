public class Solution {
    public ArrayList<Integer> spiralOrder(int[][] matrix) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        int m = matrix.length;
        if (m == 0) {
            return result;
        }
        int n = matrix[0].length;
        if (n == 0) {
            return result;
        }
        int[][] flag = new int[m][n];
        for (int i=0; i < m; i++) {
            for (int j=0; j < n; j++) {
                flag[i][j] = 0;
            }
        }
        int i=0, j=0;
        while (true) {
            if (i < 0 || i >= m || j < 0 || j >= n || flag[i][j] == 1) {
                break;
            }
            while (j < n && flag[i][j] == 0) {
                flag[i][j] = 1;
                result.add(matrix[i][j]);
                j++;
            }
            j--;
            i++;
            while (i < m && flag[i][j] == 0) {
                flag[i][j] = 1;
                result.add(matrix[i][j]);
                i++;
            }
            i--;
            j--;
            while (j >= 0 && flag[i][j] == 0) {
                flag[i][j] = 1;
                result.add(matrix[i][j]);
                j--;
            }
            j++;
            i--;
            while (i >= 0 && flag[i][j] == 0) {
                flag[i][j] = 1;
                result.add(matrix[i][j]);
                i--;
            }
            i++;
            j++;
        }
        return result;
    }
}
