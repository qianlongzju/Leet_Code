#include "leetcode.h"
class Solution {
public:
    bool isBalanced(TreeNode *root) {
        return maxDepth(root) != -1;
    }
    int maxDepth(TreeNode *root) {
        if (root == NULL) return 0;

        int left = maxDepth(root->left);
        if (left == -1) return -1;
        int right = maxDepth(root->right);
        if (right == -1) return -1;

        return abs(left - right) <= 1? max(left, right) + 1: -1;
    }
    /*
    bool isBalanced(TreeNode *root) {
        int depth = 0;
        return isBalanced(root, depth);
    }
    bool isBalanced(TreeNode *root, int& depth) {
        if (root == NULL) {
            depth = 0;;
            return true;
        }
        int left, right;
        if (isBalanced(root->left, left) && isBalanced(root->right, right)) {
            int diff = left - right;
            if (diff <= 1 && diff >= -1) {
                depth = (left > right ? left : right) + 1;
                return true;
            }
        }
        return false;
    }
    */
};
int main() {
    return 0;
}
