class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.size() == 0 || matrix[0].size() == 0)
            return false;
        int low = 0;
        int high = matrix.size() - 1;
        int middle;
        while (low < high) {
            middle = low + (high - low)/2;
            if (matrix[middle][0] > target) {
                high = middle - 1;
            } else if (matrix[middle][0] < target) {
                low = middle + 1;
            } else {
                return true;
            }
        }
        int row;
        if (matrix[low][0] > target) {
           row  = low - 1;
           if (row < 0) {
               return false;
           }
        } else {
            row = low;
        }
        low = 0;
        high = matrix[row].size() - 1;
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
};
