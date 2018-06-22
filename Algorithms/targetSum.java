class Solution {
    public int findTargetSumWays(int[] nums, int S) {
        return findTargetSumWays(nums, 0, nums.length-1, S);
    }
    private int findTargetSumWays(int[] nums, int start, int end, int S) {
        if (start > end) {
            if (S == 0) return 1;
            else return 0;
        }
        return findTargetSumWays(nums, start+1, end, S+nums[start]) + findTargetSumWays(nums, start+1, end, S-nums[start]);
    }
}
