class Solution {
public:
    void setZeroes(vector<vector<int> > &matrix) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int M = matrix.size();
        int N = matrix[0].size();
        bool setFirstRowZeroes = false;
        bool setFirstColZeroes = false;
        for (int i=0; i < M && !setFirstColZeroes; i++) {
            if (matrix[i][0] == 0) {
                setFirstColZeroes = true;
            }
        }
        for (int j=0; j < N && !setFirstRowZeroes; j++) {
            if (matrix[0][j] == 0) {
                setFirstRowZeroes = true;
            }
        }
        for (int i=1; i < M; i++) {
            for (int j=1; j < N; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        for (int i=1; i < M; i++) {
            if (matrix[i][0] == 0) {
                for (int j=1; j < N; j++) {
                    matrix[i][j] = 0;
                }
            }
        }
        for (int j=1; j < N; j++) {
            if (matrix[0][j] == 0) {
                for (int i=1; i < M; i++) {
                    matrix[i][j] = 0;
                }
            }
        }
        if (setFirstRowZeroes) {
            for (int j=0; j < N; j++) {
                matrix[0][j] = 0;
            }
        }
        if (setFirstColZeroes) {
            for (int i=0; i < M; i++) {
                matrix[i][0] = 0;
            }
        }
        
    }
};
