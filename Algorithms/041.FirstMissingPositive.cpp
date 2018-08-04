class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for (int i=0; i < n; i++) {
            while (nums[i] <= n  && nums[i] > 0 && nums[i] != i+1) {
                int temp = nums[nums[i]-1];
                if (temp == nums[i]) {
                    break;
                }
                nums[nums[i]-1] = nums[i];
                nums[i] = temp;
            }
        }        
        for (int i=0; i < n; i++) {
            if (nums[i] != i+1) {
                return i+1;
            }
        }
        return n+1;
    }
};
