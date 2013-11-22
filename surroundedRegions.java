import java.util.*;
public class Solution {
    public void solve(char[][] board) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int m = board.length;
        if (m == 0)
            return;
        int n = board[0].length;
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
    void bfs(char[][] board, int i, int j) {
        int n = board[0].length;
        LinkedList<Integer> q = new LinkedList<Integer>();
        visit(board, i, j, q);
        while (!q.isEmpty()) {
            int x = q.remove();
            int ii = x / n;
            int jj = x % n;
            visit(board, ii-1, jj, q);
            visit(board, ii+1, jj, q);
            visit(board, ii, jj-1, q);
            visit(board, ii, jj+1, q);
        }
    }
    void visit(char[][] board, int i, int j, LinkedList<Integer> q) {
        int m = board.length;
        int n = board[0].length;
        if (i < 0 || j < 0 || i >= m || j >= n || board[i][j] != 'O')
            return;
        board[i][j] = '+';
        q.add(i * n + j);
    }
}
