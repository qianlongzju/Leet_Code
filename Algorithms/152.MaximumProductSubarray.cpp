class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max_product = nums[0], min_product = nums[0], result = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            int mx = max_product, mn = min_product;
            max_product = max(max(nums[i], mx * nums[i]), mn * nums[i]);
            min_product = min(min(nums[i], mx * nums[i]), mn * nums[i]);
            result = max(result, max_product);
        }
        return result;
    }
};
