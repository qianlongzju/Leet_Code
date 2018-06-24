class Solution {
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        swap(nums, 0, nums.length-1);
        swap(nums, 0, k-1);
        swap(nums, k, nums.length-1);
    }
    void swap(int[] nums, int i, int j) {
        while(i < j) {
            int t = nums[i];
            nums[i] = nums[j];
            nums[j] = t;
            i++;
            j--;
        }
    }
}
