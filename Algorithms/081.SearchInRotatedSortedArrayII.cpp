class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int left = 0; 
        int right = nums.size() - 1;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (target == nums[middle]) {
                return true;
            } else if (target == nums[left]) {
                return true;
            } else if (target == nums[right]) {
                return true;
            } else if (nums[middle] > nums[left]) {
                if (target < nums[middle] && target > nums[left])
                    right = middle - 1;
                else
                    left = middle + 1;
            } else if (nums[middle] < nums[left]) {
                if (target > nums[middle] && target < nums[right])
                    left = middle + 1;
                else
                    right = middle - 1;
            } else 
                left ++;
        }
        return false;
    }
};
