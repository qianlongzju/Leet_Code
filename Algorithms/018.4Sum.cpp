class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int> > result;
        sort(nums.begin(), nums.end());
        set<vector<int> > quadplets;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                int k = j + 1;
                int l = n - 1;
                while (k < l) {
                    int sum_four = nums[i] + nums[j] + nums[k] + nums[l];
                    if (sum_four < target) {
                        k++;
                    } else if (sum_four > target) {
                        l--;
                    } else {
                        vector<int> temp {nums[i], nums[j], nums[k], nums[l]};
                        quadplets.insert(temp);
                        k++;
                        l--;
                    }
                }
            }
        }
        for (auto it=quadplets.begin(); it != quadplets.end(); ++it)
                result.push_back(*it);
        return result;
    }
};
