class Solution {
public:
    int maxPathSum(TreeNode *root) {
        int max_path_sum = INT_MIN;
        maxPathSum(root, max_path_sum); 
        return max_path_sum;
    }
    int maxPathSum(TreeNode *root, int& max_path_sum) {
        if (root == NULL) return 0;
        int left = maxPathSum(root->left, max_path_sum);
        int right = maxPathSum(root->right, max_path_sum);
        max_path_sum = max(max_path_sum, left + right + root->val);
        int ret = root->val + max(left, right);
        return ret > 0? ret:0;
    }
};
