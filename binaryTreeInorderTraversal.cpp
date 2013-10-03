/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> v;
        vector<TreeNode*> stack;
        TreeNode *p = root;
        while (!stack.empty() || p != NULL) {
            if (p != NULL) {
                stack.push_back(p);
                p = p->left;
            }
            else {
                p = stack.back();
                stack.pop_back();
                v.push_back(p->val);
                p = p->right;
            }
        }
        return v;
    }
    vector<int> inorderTraversal_recursive(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<int> v;
        if (root == NULL) {
            return v;
        }
        vector<int> left = inorderTraversal_recursive(root->left);
        for (int i=0; i < left.size(); i++) {
            v.push_back(left[i]);
        }
        v.push_back(root->val);
        vector<int> right = inorderTraversal_recursive(root->right);
        for (int i=0; i < right.size(); i++) {
            v.push_back(right[i]);
        }
        return v;
    }
};
