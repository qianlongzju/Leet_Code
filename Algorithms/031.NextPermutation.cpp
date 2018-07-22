class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        for (int i=nums.size()-1; i > 0; i--) {
            if (nums[i] <= nums[i-1]) {
                continue;
            }
            for (int j=nums.size()-1; j >= i; j--) {
                if (nums[j] > nums[i-1]) {
                    int temp = nums[i-1];
                    nums[i-1] = nums[j];
                    nums[j] = temp;
                    for(int p=i, q=nums.size()-1; p < q; p++, q--) {
                        int temp = nums[p];
                        nums[p] = nums[q];
                        nums[q] = temp;
                    }
                    return;
                }
            }
        }
        for(int p=0, q=nums.size()-1; p < q; p++, q--) {
            int temp = nums[p];
            nums[p] = nums[q];
            nums[q] = temp;
        }
    }
};
