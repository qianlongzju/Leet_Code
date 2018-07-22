class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix) {
        vector<int> elements;
        if (matrix.size() == 0) return elements;
        int m = matrix.size(), n = matrix[0].size();
        int row = 0, col = -1;
        while (true) {
            for (int i = 0; i < n; i++) 
                elements.push_back(matrix[row][++col]);
            if (--m == 0) break;
            for (int i = 0; i < m; i++) 
                elements.push_back(matrix[++row][col]);
            if (--n == 0) break;
            for (int i = 0; i < n; i++) 
                elements.push_back(matrix[row][--col]);
            if (--m == 0) break;
            for (int i = 0; i < m; i++) 
                elements.push_back(matrix[--row][col]);
            if (--n == 0) break;
        }
        return elements;
    }
    /*
    vector<int> spiralOrder(vector<vector<int>> &matrix) {
        vector<int> result;
        int m = matrix.size();
        if (m == 0) {
            return result;
        }
        int n = matrix[0].size();
        if (n == 0) {
            return result;
        }
        int flag[m][n];
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
                result.push_back(matrix[i][j]);
                j++;
            }
            j--;
            i++;
            while (i < m && flag[i][j] == 0) {
                flag[i][j] = 1;
                result.push_back(matrix[i][j]);
                i++;
            }
            i--;
            j--;
            while (j >= 0 && flag[i][j] == 0) {
                flag[i][j] = 1;
                result.push_back(matrix[i][j]);
                j--;
            }
            j++;
            i--;
            while (i >= 0 && flag[i][j] == 0) {
                flag[i][j] = 1;
                result.push_back(matrix[i][j]);
                i--;
            }
            i++;
            j++;
        }
        return result;
    }
    */
};
