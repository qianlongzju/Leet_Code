public class Solution {
    private int result;
    public int totalNQueens(int n) {
        int[] nums = new int[n];
        result = 0;
        solveNQueens(0, n, nums);
        return result;
    }
    private void solveNQueens(int index, int n, int[] nums) {
        if (index == n) {
            result ++;
            return;
        }
        for (int j=1; j <= n; ++j) {
            nums[index] = j;
            if (isValid(nums, index))
                solveNQueens(index+1, n, nums);
        }
    }
    boolean isValid(int[] nums, int index) {
        for (int i=0; i < index; ++i) {
            if (nums[i] == nums[index])
                return false;
            if ((nums[i] - nums[index]) == (i - index))
                return false;
            if ((nums[i] - nums[index]) == (index - i))
                return false;
        }
        return true;
    }
}
