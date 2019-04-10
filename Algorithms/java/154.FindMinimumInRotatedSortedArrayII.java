public class Solution {
    public int findMin(int[] nums) {
        int start = 0, end = nums.length-1;
        while (start < end && nums[start] >= nums[end]) {
            int mid = start + (end - start) / 2;
            if (nums[mid] > nums[end]) {
                start = mid + 1;
            } else if (nums[mid] < nums[end]) {
                end = mid;
            } else {
                start++;
            }
        }
        return nums[start];
    }
    /*
    public int findMin(int[] nums) {
        return findMin(nums, 0, nums.length-1);
    }
    private int findMin(int[] nums, int start, int end) {
        if (start == end)
            return nums[start];
        if (nums[start] < nums[end])
            return nums[start];
        int mid = start + (end - start) / 2;
        if (nums[start] == nums[end])
            return findMin(nums, start+1, end);
        if (nums[mid] >= nums[start])
            return findMin(nums, mid+1, end);
        return findMin(nums, start, mid);
    }
    */
}
