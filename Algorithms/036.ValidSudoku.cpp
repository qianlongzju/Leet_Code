class Solution {
public:
    bool isValidSudoku(vector<vector<char> > &board) {
        bool used[9];
        for (int i=0; i < 9; ++i) {
            fill(used, used+9, false);
            for (int j=0; j < 9; ++j)
                if (!check(board[i][j], used))
                    return false;
            fill(used, used+9, false);
            for (int j=0; j < 9; ++j)
                if (!check(board[j][i], used))
                    return false;
        }
        for (int i=0; i < 3; ++i)
            for (int j=0; j < 3; ++j) {
                fill(used, used+9, false);
                for (int k=0; k < 3; ++k)
                    for (int l=0; l < 3; ++l)
                        if (!check(board[i*3+k][j*3+l], used))
                            return false;
            }
        return true;
    }
private:
    bool check(char c, bool used[]) {
        if (c == '.') return true;
        if (used[c-'1']) return false;
        return used[c-'1'] = true;
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
