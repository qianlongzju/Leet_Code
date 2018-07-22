class Solution {
public:
    TreeNode *sortedArrayToBST(vector<int>& nums) {
        return sortedArrayToBST(nums, 0, nums.size()-1);
    }
    TreeNode *sortedArrayToBST(vector<int>& nums, int start, int end) {
        if (start > end) return NULL;
        int middle = start + (end-start)/2;
        TreeNode *root = new TreeNode(nums[middle]);
        root->left = sortedArrayToBST(nums, start, middle-1);
        root->right = sortedArrayToBST(nums, middle+1, end);
        return root;
    }
};
