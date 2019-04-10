class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mapping;
        for (int i = 0; i < nums.size(); i++)
            mapping[nums[i]] = i;
        for (int i = 0; i < nums.size(); i++) {
            int gap = target - nums[i];
            if (mapping.find(gap) != mapping.end() &&
                    mapping[gap] != i) {
                return vector<int>{i, mapping[gap]};
            }
        }
    }
};
