class Solution {
public:
    void sortColors(vector<int>& nums) {
        int i, j;
        int n = nums.size();
        for (i = 0; i < n; i++)
            if (nums[i] != 0)
                break;
        for (j = n-1; j >= 0; j--)
            if (nums[j] != 2)
                break;
        int k = i;
        while (k <= j) {
            if (nums[k] == 0) {
                int temp = nums[i];
                nums[i] = nums[k];
                nums[k] = temp;
                i ++;
            }
            else if (nums[k] == 2) {
                int temp = nums[j];
                nums[j] = nums[k];
                nums[k] = temp;                
                j --;
            }
            else {
                k++;
            } 
            if (k <= i)
                k = i;
        }
    }
};
