class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        for (int j=0; j < 32; ++j) {
            int tmp = 0;
            int bitOps = 1 << j;
            for (int i=0; i < nums.size(); ++i) {
                if (nums[i] & bitOps) {
                    tmp ++;
                }
            }
            result += (tmp%3) << j;
        }
        return result;
    }
};
