#include "leetcode.h"
class Solution {
public:
    int maxDepth(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (root == NULL) {
            return 0;
        }
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        if (leftDepth < rightDepth) {
            return 1 + rightDepth;
        }
        else {
            return 1 + leftDepth;
        }
    }
};
