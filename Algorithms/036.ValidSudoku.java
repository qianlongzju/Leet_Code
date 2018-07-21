public class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[] used = new boolean[9];
        for (int i=0; i < 9; ++i) {
            for (int j=0; j < 9; j++)
                used[j] = false;
            for (int j=0; j < 9; ++j)
                if (!check(board[i][j], used))
                    return false;
            for (int j=0; j < 9; j++)
                used[j] = false;
            for (int j=0; j < 9; ++j)
                if (!check(board[j][i], used))
                    return false;
        }
        for (int i=0; i < 3; ++i)
            for (int j=0; j < 3; ++j) {
                for (int m=0; m < 9; m++)
                    used[m] = false;
                for (int k=0; k < 3; ++k)
                    for (int l=0; l < 3; ++l)
                        if (!check(board[i*3+k][j*3+l], used))
                            return false;
            }
        return true;
    }
    private boolean check(char c, boolean used[]) {
        if (c == '.') return true;
        if (used[c-'1']) return false;
        return used[c-'1'] = true;
    }
}
