#include "leetcode.h"
class Solution {
public:
    bool isValidBST(TreeNode *root) {
        return validBST(root, false, 0, false, 0);
    }
    bool validBST(TreeNode *root, bool minBound, int min, bool maxBound, int max) {
        if (root == NULL)
            return true;
        if (minBound && min >= root->val)
            return false;
        if (maxBound && max <= root->val)
            return false;
        return validBST(root->left, minBound, min, true, root->val) 
            && validBST(root->right, true, root->val, maxBound, max);
    }
};
