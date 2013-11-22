#include "leetcode.h"
class Solution {
public:
    bool isSameTree(TreeNode *p, TreeNode *q) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (p == NULL && q != NULL) {
            return false;
        }
        if (p != NULL && q == NULL) {
            return false;
        }
        if (p == NULL && q == NULL) { 
            return true;
        }
        if (p->val != q->val) {
            return false;
        }
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
