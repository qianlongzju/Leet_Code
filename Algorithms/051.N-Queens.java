class Solution {
    public List<List<String>> solveNQueens(int n) {
        int[] nums = new int[n];
        for (int i=0; i < n; i++) {
            nums[i] = 0;
        }
        List<List<String>> result = new ArrayList<List<String>>();
        solveNQueens(n, nums, result, 0);
        return result;
    }
    void solveNQueens(int n, int[] nums, List<List<String>> result, int level) {
        if (level == n) {
            result.add(getBoard(nums));
            return;
        }
        for (int j=1; j <= n; ++j) {
            nums[level] = j;
            if (isValid(nums, level))
                solveNQueens(n, nums, result, level+1);
        }
    }
    boolean isValid(int[] nums, int index) {
        for (int i=0; i < index; ++i) {
            if (nums[i] == nums[index])
                return false;
            if (Math.abs(nums[i] - nums[index]) == (index - i))
                return false;
        }
        return true;
    }
    List<String> getBoard(int[] nums) {
        List<String> board = new ArrayList<>();
        for (int i=0; i < nums.length; i++) {
            String s = "";
            for (int j=0; j < nums.length; j++) {
                if (j+1 == nums[i]) {
                    s += "Q";
                } else {
                    s += ".";
                }
            }
            board.add(s);
        }
        return board;
    }
}
