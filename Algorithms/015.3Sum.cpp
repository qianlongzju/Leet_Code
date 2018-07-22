class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        set<vector<int>> triplets;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            while (i > 0 && i < n && nums[i] == nums[i-1])
                i++;
            int j = i + 1;
            int k = n - 1;
            while (j < k) {
                int total = nums[i] + nums[j] + nums[k];
                if (total < 0) {
                    j++;
                    while (j < k && nums[j] == nums[j-1])
                        j++;
                } else if (total > 0) {
                    k--;
                    while (k > j && nums[k] == nums[k+1])
                        k--;
                } else {
                    triplets.insert({ nums[i], nums[j], nums[k]});
                    j++;
                    while (j < k && nums[j] == nums[j-1])
                        j++;
                    k--;
                    while (k > j && nums[k] == nums[k+1])
                        k--;
                }
            }
        }
        for (auto it=triplets.begin(); it != triplets.end(); ++it)
                result.push_back(*it);
        return result;
    }
};
