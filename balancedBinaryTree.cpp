#include "leetcode.h"
class Solution {
public:
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
    //bool isBalanced(TreeNode *root) {
    //    if (height(root) == -1) {
    //        return false;
    //    }
    //    else {
    //        return true;
    //    }
    //}
    //int height(TreeNode *root) {
    //    if (root == NULL) {
    //        return 0;
    //    }
    //    else {
    //        int left = height(root->left);
    //        if (left == -1) {
    //            return -1;
    //        }
    //        int right = height(root->right);
    //        if (right == -1) {
    //            return -1;
    //        }
    //        if (left == right && left >= 0) {
    //            return 1+left;
    //        }
    //        else if (left+1 == right && left >= 0) {
    //            return 1 + right;
    //        }
    //        else if (right+1 == left && right >= 0) {
    //            return 1 + left;
    //        }
    //        else {
    //            return -1;
    //        }
    //    }
    //}
};
int main() {
    return 0;
}
