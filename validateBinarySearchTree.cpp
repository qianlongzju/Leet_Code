#include "leetcode.h"
class Solution {
public:
    bool isValidBST(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        return validBST(root, false, 0, false, 0);
    }
    bool validBST(TreeNode *root, bool minBound, int min, bool maxBound, int max) {
        if (root == NULL) {
            return true;
        }
        if (minBound) {
            if (min >= root->val) {
                return false;
            }
        }
        if (maxBound) {
            if (max <= root->val) {
                return false;
            }
        }
        if (root->left == NULL && root->right == NULL) {
            return true;
        }
        if (root->left == NULL && root->right != NULL) {
            return validBST(root->right, true, root->val, maxBound, max);
        }
        if (root->left != NULL && root->right == NULL) {
            return validBST(root->left, minBound, min, true, root->val);
        }
        if (root->left != NULL && root->right != NULL) {
            return validBST(root->left, minBound, min, true, root->val) && validBST(root->right, true, root->val, maxBound, max);
        }
    }
};
