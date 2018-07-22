class Solution {
public:
    int totalNQueens(int n) {
        int num[n];
        memset(num, 0, sizeof(num));
        int result = 0;
        solveNQueens(0, n, num, result);
        return result;
    }
    void solveNQueens(int index, int n, int *num, int& result) {
        if (index == n) {
            result ++;
            return;
        }
        for (int j=1; j <= n; ++j) {
            num[index] = j;
            if (isValid(num, index))
                solveNQueens(index+1, n, num, result);
        }
    }
    bool isValid(int *num, int index) {
        for (int i=0; i < index; ++i) {
            if (num[i] == num[index] || abs(num[i] - num[index]) == abs(i - index))
                return false;
        }
        return true;
    }
    /*
    int totalNQueens(int n) {
        vector<int> num;
        for (int i = 0; i < n; i++) {
            num.push_back(i);
        }
        int result = 0;
        vector<vector<int>> permutations;
        permute(num, 0, permutations);
        for (int i = 0; i < permutations.size(); i++) {
            if (isValid(permutations[i])) {
                result ++;
            }
        }
        return result;
    }
    bool isValid(vector<int> permutation) {
        for (int i=0; i < permutation.size(); i++) {
            for (int j=i+1; j < permutation.size(); j++) {
                if (j-i == permutation[j]-permutation[i]) {
                    return false;
                }
                if (j-i == permutation[i]-permutation[j]) {
                    return false;
                }
            }
        }
        return true;
    }
    void permute(vector<int>& num, int index,
            vector<vector<int>>& result) {
        if (num.size() == index) {
            result.push_back(num);
            return;
        }
        for (int i=index; i < num.size(); ++i) {
            int temp = num[i];
            num[i] = num[index];
            num[index] = temp;
            permute(num, index+1, result);
            temp = num[i];
            num[i] = num[index];
            num[index] = temp;
        }
    }
    */
};
