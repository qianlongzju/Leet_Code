class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k %= nums.size();
        swap(nums, 0, nums.size()-1);
        swap(nums, 0, k-1);
        swap(nums, k, nums.size()-1);
    }
    void swap(vector<int>& nums, int i, int j) {
        while(i < j) {
            int t = nums[i];
            nums[i] = nums[j];
            nums[j] = t;
            i++;
            j--;
        }
    }
};
