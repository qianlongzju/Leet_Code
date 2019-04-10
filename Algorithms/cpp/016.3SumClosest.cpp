class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int lowestGap = INT_MAX;
        int closestSum = 0;
        for (int i = 0; i < n; i++) {
            while (i > 0 && i < n && nums[i] == nums[i-1])
                i++;
            int j = i + 1;
            int k = n - 1;
            while (j < k) {
                int total = nums[i] + nums[j] + nums[k];
                int gap = abs(target - total);
                if (gap < lowestGap) {
                    lowestGap = gap;
                    closestSum = total;
                }
                if (total < target) {
                    j++;
                    while (j < k && nums[j] == nums[j-1])
                        j++;
                } else if (total > target) {
                    k--;
                    while (k > j && nums[k] == nums[k+1])
                        k--;
                } else
                    return closestSum;
            }
        }
        return closestSum;
    }
};
