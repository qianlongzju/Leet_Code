#include "leetcode.h"
class Solution {
public:
    void flatten(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        flat(root);
    }
    TreeNode* flat(TreeNode* root) {
        if (root == NULL) 
            return root;
        if (root->left != NULL) {
            TreeNode* right = root->right;
            TreeNode* left = flat(root->left);
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
int main() {
    TreeNode a(1);
    TreeNode b(2);
    TreeNode c(3);
    TreeNode d(1);
    TreeNode e(1);
    a.left = &b;
    b.left = &c;
    Solution s;
    s.flatten(&a);
    return 0;
}
