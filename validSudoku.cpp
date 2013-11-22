#include "leetcode.h"
class Solution {
public:
    bool isValidSudoku(vector<vector<char> > &board) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int num[9];
        for (int i=0; i < 9; ++i) {
            for (int j=0; j < 9; ++j) {
                num[j] = 0;
            }
            for (int j=0; j < 9; ++j) {
                if (board[i][j] != '.') {
                    int digit = board[i][j] - '0';
                    if (num[digit-1] == 1) {
                      //  cout << "i: " << i << " j: " << j << endl;
                        return false;
                    } else {
                        num[digit-1] = 1;
                    }
                }
            }
            for (int j=0; j < 9; ++j) {
                num[j] = 0;
            }
            for (int j=0; j < 9; ++j) {
                if (board[j][i] != '.') {
                    int digit = board[j][i] - '0';
                    if (num[digit-1] == 1) {
                     //   cout << "j: " << j << " i: " << i << endl;
                        return false;
                    } else {
                        num[digit-1] = 1;
                    }
                }
            }
        }
        for (int i=0; i < 3; ++i) {
            for (int j=0; j < 3; ++j) {
                for (int k=0; k < 9; ++k) {
                    num[k] = 0;
                }
                for (int k=0; k < 3; ++k) {
                    for (int l=0; l < 3; ++l) {
                        if (board[i*3+k][j*3+l] == '.') {
                            ;
                        } else {
                            int digit = board[i*3+k][j*3+l] - '0';
                            if (num[digit-1] == 1) {
                    //            cout << "i: " << i << " j: " << j << " k: " << k << " l: " << l << endl;
                                return false;
                            } else {
                                num[digit-1] = 1;
                            }
                        }
                    }
                }
            }
        }
        return true;
    }
};
int main() {
    Solution s;
    string a[] = {"..5.....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."};
    vector<vector<char> > v;
    v.push_back(vector<char>(a[0].begin(), a[0].end()));
    v.push_back(vector<char>(a[1].begin(), a[1].end()));
    v.push_back(vector<char>(a[2].begin(), a[2].end()));
    v.push_back(vector<char>(a[3].begin(), a[3].end()));
    v.push_back(vector<char>(a[4].begin(), a[4].end()));
    v.push_back(vector<char>(a[5].begin(), a[5].end()));
    v.push_back(vector<char>(a[6].begin(), a[6].end()));
    v.push_back(vector<char>(a[7].begin(), a[7].end()));
    v.push_back(vector<char>(a[8].begin(), a[8].end()));
    cout << s.isValidSudoku(v) << endl;
    return 0;
}

