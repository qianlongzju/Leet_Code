class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int maxIndex = 0;
        for (int i=0; i < n && i <= maxIndex; i++) {
            if (i+nums[i] < maxIndex) {
                continue;
            }
            maxIndex = i + nums[i];
            if (maxIndex >= n-1) {
                return true;
            }
        }
        return false;
    }
};
