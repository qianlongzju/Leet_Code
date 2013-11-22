#include "leetcode.h"
class Solution {
public:
    int maxPathSum(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int temp_sum = INT_MIN;
        maxPathSum(root, temp_sum); 
        return temp_sum;
    }
    int maxPathSum(TreeNode *root, int &max) {
        if (root == NULL) {
            return 0;
        }
        int left = maxPathSum(root->left, max);
        int right = maxPathSum(root->right, max);
        if (left + right + root->val > max) {
            max = left + right + root->val;
        }
        if (left > right) {
            right = left;
        }
        right = right + root->val;
        if (right > 0) {
            return right;
        }
        return 0;
    }
};
int main() {
    Solution s;

    return 0;
}

