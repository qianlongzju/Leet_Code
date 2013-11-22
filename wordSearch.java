import java.util.*;
public class Solution {
    public boolean exist(char[][] board, String word) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int m = board.length;
        int n = board[0].length;
        boolean[][] visited = new boolean[m][n];
        for (int i=0; i < m; ++i) {
            for (int j=0; j < n; ++j) {
                visited[i][j] = false;
            }
        }
        for (int i=0; i < m; ++i) {
            for (int j=0; j < n; ++j) {
                if (dfs(0, i, j, word, board, visited))
                    return true;
            }
        }
        return false;
    }
    boolean dfs(int index, int i, int j, String word, 
            char[][] board, boolean[][] visited) {
        if (index == word.length())
            return true;
        if (i < 0 || j < 0 || i >= board.length || j >= board[0].length)
            return false;
        if (board[i][j] != word.charAt(index))
            return false;
        if (visited[i][j])
            return false;
        visited[i][j] = true;
        boolean result = dfs(index+1, i-1, j, word, board, visited) ||
            dfs(index+1, i+1, j, word, board, visited) ||
            dfs(index+1, i, j-1, word, board, visited) ||
            dfs(index+1, i, j+1, word, board, visited);
        visited[i][j] = false;
        return result;
    }
}
