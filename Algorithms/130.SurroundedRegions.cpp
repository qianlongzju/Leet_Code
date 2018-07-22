class Solution {
public:
    // 广搜。从上下左右四个边界往里走,凡是能碰到的'O',都是跟边界接壤的,应该保留
    void solve(vector<vector<char>>& board) {
        int m = board.size();
        if (m == 0)
            return;
        int n = board[0].size();
        for (int i=0; i < m; ++i) {
            bfs(board, i, 0);
            bfs(board, i, n-1);
        }
        for (int j=1; j < n-1; ++j) {
            bfs(board, 0, j);
            bfs(board, m-1, j);
        }
        for (int i=0; i < m; ++i) {
            for (int j=0; j < n; ++j) {
                if (board[i][j] == 'O')
                    board[i][j] = 'X';
                else if (board[i][j] == '+')
                    board[i][j] = 'O';
            }
        }
    }
    void bfs(vector<vector<char>> &board, int i, int j) {
        int n = board[0].size();
        queue<int> q;
        visit(board, i, j, q);
        while (!q.empty()) {
            int x = q.front(); q.pop();
            int ii = x / n;
            int jj = x % n;
            visit(board, ii-1, jj, q);
            visit(board, ii+1, jj, q);
            visit(board, ii, jj-1, q);
            visit(board, ii, jj+1, q);
        }
    }
    void visit(vector<vector<char>> &board, int i, int j, queue<int> &q) {
        int m = board.size();
        int n = board[0].size();
        if (i < 0 || j < 0 || i >= m || j >= n || board[i][j] != 'O')
            return;
        board[i][j] = '+';
        q.push(i * n + j);
    }
};
