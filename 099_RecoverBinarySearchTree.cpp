#include "leetcode.h"
class Solution {
public:
    void recoverTree(TreeNode *root) {
        TreeNode *pre = NULL;
        TreeNode *node1 = NULL;
        TreeNode *node2 = NULL;
        recoverTree(root, pre, node1, node2);
        int temp = node1->val;
        node1->val = node2->val;
        node2->val = temp;
    }
    void recoverTree(TreeNode *root, TreeNode* &pre, TreeNode* &node1, 
            TreeNode* &node2) {
        if (root == NULL) {
            return;
        }
        recoverTree(root->left, pre, node1, node2);
        if (pre != NULL && root->val < pre->val) {
            if (node1 == NULL) {
                node1 = pre;
                node2 = root;
            } else {
                node2 = root;
            }
        }
        pre = root;
        recoverTree(root->right, pre, node1, node2);
    }
};
