public class Solution {
    public List<String[]> solveNQueens(int n) {
        int[] num = new int[n];
        for (int i=0; i < n; i++) {
            num[i] = 0;
        }
        List<String[]> result = new ArrayList<String[]>();
        solveNQueens(n, num, result, 0);
        return result;
    }
    void solveNQueens(int n, int[] num, List<String[]> result, int level) {
        if (level == n) {
            result.add(getBoard(num));
            return;
        }
        for (int j=1; j <= n; ++j) {
            num[level] = j;
            if (isValid(num, level))
                solveNQueens(n, num, result, level+1);
        }
    }
    boolean isValid(int[] num, int index) {
        for (int i=0; i < index; ++i) {
            if (num[i] == num[index])
                return false;
            if (Math.abs(num[i] - num[index]) == (index - i))
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
