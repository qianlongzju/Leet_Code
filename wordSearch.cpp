#include "leetcode.h"
class Solution {
public:
    // dfs
    bool exist(vector<vector<char> > &board, string word) {
        int m = board.size();
        int n = board[0].size();
        vector<vector<bool> > visited(m, vector<bool>(n, false));
        for (int i=0; i < m; ++i) {
            for (int j=0; j < n; ++j) {
                if (dfs(0, i, j, word, board, visited))
                    return true;
            }
        }
        return false;
    }
    bool dfs(int index, int i, int j, string &word, 
            vector<vector<char> > &board, vector<vector<bool> > &visited) {
        if (index == word.size())
            return true;
        if (i < 0 || j < 0 || i >= board.size() || j >= board[0].size())
            return false;
        if (board[i][j] != word[index])
            return false;
        if (visited[i][j])
            return false;
        visited[i][j] = true;
        bool result = dfs(index+1, i-1, j, word, board, visited) ||
            dfs(index+1, i+1, j, word, board, visited) ||
            dfs(index+1, i, j-1, word, board, visited) ||
            dfs(index+1, i, j+1, word, board, visited);
        visited[i][j] = false;
        return result;
    }
};
int main() {
    Solution s;
    vector<vector<char> > board;
    vector<char> a, b, c;
    a.push_back('A');
    a.push_back('B');
    a.push_back('C');
    a.push_back('E');
    b.push_back('S');
    b.push_back('F');
    b.push_back('C');
    b.push_back('S');
    c.push_back('A');
    c.push_back('D');
    c.push_back('E');
    c.push_back('E');
    board.push_back(a);
    board.push_back(b);
    board.push_back(c);
    cout << s.exist(board, "ABCCED") << endl;
    cout << s.exist(board, "SEE") << endl;
    cout << s.exist(board, "ABCB") << endl;

    return 0;
}

