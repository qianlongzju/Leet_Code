class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
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
