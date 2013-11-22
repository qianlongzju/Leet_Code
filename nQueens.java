import java.util.*;
public class Solution {
    public ArrayList<String[]> solveNQueens(int n) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int[] num = new int[n];
        for (int i=0; i < n; i++) {
            num[i] = 0;
        }
        ArrayList<String[]> result = new ArrayList<String[]>();
        solveNQueens(n, num, result);
        return result;
    }
    void solveNQueens(int n, int[] num, ArrayList<String[]> result) {
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
        result.add(getBoard(num));
    }
    boolean isValid(int[] num, int index) {
        for (int i=0; i < index; ++i) {
            if (num[i] == num[index])
                return false;
            if ((num[i] - num[index]) == (i - index))
                return false;
            if ((num[i] - num[index]) == (index - i))
                return false;
        }
        return true;
    }
    String[] getBoard(int[] num) {
        String[] board = new String[num.length];
        for (int i=0; i < num.length; i++) {
            String s = "";
            for (int j=0; j < num.length; j++) {
                if (j+1 == num[i]) {
                    s += "Q";
                } else {
                    s += ".";
                }
            }
            board[i] = s;
        }
        return board;
    }
}
