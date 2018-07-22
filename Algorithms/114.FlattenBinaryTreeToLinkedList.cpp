class Solution {
public:
    void flatten(TreeNode *root) {
        flat(root);
    }
    TreeNode *flat(TreeNode *root) {
        if (root == NULL) 
            return root;
        if (root->left != NULL) {
            TreeNode *right = root->right;
            TreeNode *left = flat(root->left);
            left->right = root->right;
            root->right = root->left;
            root->left = NULL;
            if (right != NULL)
                return flat(right);
            else 
                return left;
        } else if (root->right != NULL) {
            return flat(root->right);
        }
        return root;
    }
};
