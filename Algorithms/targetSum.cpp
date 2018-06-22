class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        return findTargetSumWays(nums, 0, nums.size()-1, S);
    }
    int findTargetSumWays(vector<int>& nums, int start, int end, int S) {
        if (start > end) {
            return S == 0;
        }
        return findTargetSumWays(nums, start+1, end, S+nums[start]) + findTargetSumWays(nums, start+1, end, S-nums[start]);
    }
};
