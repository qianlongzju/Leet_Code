class Solution {
public:
    int findMin(vector<int>& nums) {
        int start = 0, end = nums.size()-1;
        while (start < end && nums[start] > nums[end]) {
            int mid = start + (end - start)/2;
            if (nums[mid] > nums[end]) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return nums[start];
    }
    /*
    public:
    int findMin(vector<int>& nums) {
        return findMin(nums, 0, nums.size()-1);
    }
    private:
    int findMin(vector<int>& nums, int start, int end) {
        if (start == end)
            return nums[start];
        if (nums[start] < nums[end])
            return nums[start];
        int mid = start + (end - start) / 2;
        if (nums[mid] >= nums[start])
            return findMin(nums, mid+1, end);
        return findMin(nums, start, mid);
    }
    */
};
