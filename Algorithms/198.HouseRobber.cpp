class Solution {
public:
    int rob(vector<int>& nums) {
        std::map<int, int> m;
        return rob(nums, 0, m);
    }
    int rob(vector<int>& nums, int index, std::map<int, int>& map) {
        if (index >= nums.size())
            return 0;
        if (map.find(index) != map.end())
            return map.find(index)->second;
        int v = max(nums[index] + rob(nums, index+2, map), rob(nums, index+1, map));
        map[index] = v;
        return v;
    }
};
