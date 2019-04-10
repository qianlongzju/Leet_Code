class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0)
            return false;
        int low = 0;
        int high = matrix.length - 1;
        int middle;
        while (low < high) {
            middle = low + (high - low)/2;
            if (matrix[middle][0] > target) {
                high = middle - 1;
            }
            else if (matrix[middle][0] < target) {
                low = middle + 1;
            } else {
                return true;
            }
        }
        int row;
        if (matrix[low][0] > target) {
           row  = low-1;
           if (row < 0) {
               return false;
           }
        } else {
            row = low;
        }
        low = 0;
        high = matrix[row].length - 1;
        while (low <= high) {
            middle = low + (high - low)/2;
            if (matrix[row][middle] > target) {
                high = middle - 1;
            } else if (matrix[row][middle] < target) {
                low = middle + 1;
            } else {
                return true;
            }
        }
        return false;
    }
}
