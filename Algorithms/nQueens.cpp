#include "leetcode.h"
class Solution {
public:
    vector<vector<string> > solveNQueens(int n) {
        vector<int> num(n, 0);
        vector<vector<string> > result;
        solveNQueens(n, num, result, 0);
        return result;
    }
    void solveNQueens(int n, vector<int> &num, vector<vector<string> > &result, int level) {
        if (level == n) {
            result.push_back(getBoard(num));
            return;
        }
        for (int j=1; j <= n; ++j) {
            num[level] = j;
            if (isValid(num, level))
                solveNQueens(n, num, result, level+1);
        }
    }
    bool isValid(vector<int> &num, int index) {
        for (int i=0; i < index; ++i) {
            if (num[i] == num[index])
                return false;
            if (abs(num[i] - num[index]) == (index - i))
                return false;
        }
        return true;
    }
    vector<string> getBoard(vector<int> &num) {
        vector<string> board;
        for (int i=0; i < num.size(); i++) {
            string s = "";
            for (int j=0; j < num.size(); j++) {
                if (j+1 == num[i]) {
                    s += "Q";
                } else {
                    s += ".";
                }
            }
            board.push_back(s);
        }
        return board;
    }
    /*
    vector<vector<string> > solveNQueens(int n) {
        vector<int> num(n, 0);
        vector<vector<string> > result;
        solveNQueens(n, num, result);
        return result;
    }
    void solveNQueens(int n, vector<int> &num, vector<vector<string> > &result) {
        for (int i=0; i < n; ++i) {
            if (num[i] != 0)
                continue;
            for (int j=1; j <= n; ++j) {
                num[i] = j;
                if (isValid(num, i))
                    solveNQueens(n, num, result);
            }
            num[i] = 0;
            return;
        }
        result.push_back(getBoard(num));
    }
    bool isValid(vector<int> &num, int index) {
        for (int i=0; i < index; ++i) {
            if (num[i] == num[index])
                return false;
            if (abs(num[i] - num[index]) == (index - i))
                return false;
        }
        return true;
    }
    vector<string> getBoard(vector<int> &num) {
        vector<string> board;
        for (int i=0; i < num.size(); i++) {
            string s = "";
            for (int j=0; j < num.size(); j++) {
                if (j+1 == num[i]) {
                    s += "Q";
                } else {
                    s += ".";
                }
            }
            board.push_back(s);
        }
        return board;
    }
    */
    /*
    // naive solution: tle
    vector<vector<string> > solveNQueens(int n) {
        vector<int> num;
        for (int i = 0; i < n; i++) {
            num.push_back(i);
        }
        vector<vector<string> > result;
        vector<vector<int> > permutations;
        permute(num, 0, permutations);
        for (int i = 0; i < permutations.size(); i++) {
            if (isValid(permutations[i])) {
                result.push_back(getSolution(permutations[i]));
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
    vector<string> getSolution(vector<int> permutation) {
        vector<string> result;
        for (int i=0; i < permutation.size(); i++) {
            string s = "";
            for (int j=0; j < permutation.size(); j++) {
                if (j == permutation[i]) {
                    s += "Q";
                } else {
                    s += ".";
                }
            }
            result.push_back(s);
        }
        return result;
    }
    void permute(vector<int> &num, int index,
            vector<vector<int> > &result) {
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
int main() {
    Solution s;
    vector<vector<string> > v = s.solveNQueens(4);
    for (int i=0; i < v.size(); i++) {
        for (int j=0; j < v[i].size(); j++) {
            cout << v[i][j] << endl;
        }
        cout << endl;
    }
    return 0;
}
