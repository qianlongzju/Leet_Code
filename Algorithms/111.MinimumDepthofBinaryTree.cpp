class Solution {
public:
    int minDepth(TreeNode *root) {
        if (root == NULL) {
            return 0;
        }
        int leftDepth = minDepth(root->left);
        int rightDepth = minDepth(root->right);
        if (leftDepth == 0) {
            return 1 + rightDepth;
        }
        if (rightDepth == 0) {
            return 1 + leftDepth;
        }
        if (leftDepth < rightDepth) {
            return 1 + leftDepth;
        }
        else {
            return 1 + rightDepth;
        }
    }
};
