public class Solution {
    private int result;
    public int totalNQueens(int n) {
        int[] num = new int[n];
        result = 0;
        solveNQueens(0, n, num);
        return result;
    }
    private void solveNQueens(int index, int n, int[] num) {
        if (index == n) {
            result ++;
            return;
        }
        for (int j=1; j <= n; ++j) {
            num[index] = j;
            if (isValid(num, index))
                solveNQueens(index+1, n, num);
        }
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
}
