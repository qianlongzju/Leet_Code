class Solution {
public:
    int sumNumbers(TreeNode *root) {
        return sumNumbersToLeaf(root, 0);
    }
    int sumNumbersToLeaf(TreeNode *root, int s) {
        if (root == NULL) {
            return s;
        }
        if (root->left == NULL && root->right == NULL) {
            return s*10 + root->val;
        }
        int sum = 0;
        if (root->left != NULL) {
            sum += sumNumbersToLeaf(root->left, s*10+root->val);
        }
        if (root->right != NULL) {
            sum += sumNumbersToLeaf(root->right, s*10+root->val);
        }
        return sum;
    }
};
