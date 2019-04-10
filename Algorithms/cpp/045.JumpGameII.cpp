class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int maxIndex = 0;
        int steps[n];
        for (int i=0; i < n; i++) {
            steps[i] = INT_MAX;
        }
        steps[0] = 0;
        for (int i=0; i < n && i <= maxIndex; i++) {
            for (int j=maxIndex+1; j <= i+nums[i] && j < n; j++) {
                if (steps[i]+1 < steps[j]) {
                    steps[j] = steps[i] + 1;
                }
            }
            if (i+nums[i] < maxIndex) {
                continue;
            }
            maxIndex = i + nums[i];
            if (maxIndex >= n-1) {
                break;
            }
        }
        return steps[n-1];
    }
};
