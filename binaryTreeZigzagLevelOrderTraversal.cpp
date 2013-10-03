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
    vector<vector<int> > zigzagLevelOrder(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<vector<int> > result;
        if (root == NULL) {
            return result;
        }
        vector<int> v;
        vector<TreeNode*> stack;
        vector<TreeNode*> next_level_stack;
        stack.push_back(root);
        bool flag = false;
        while (!stack.empty()) {
            TreeNode* p = stack.front();
            stack.erase(stack.begin());
            if (flag) {
                v.insert(v.begin(), p->val);
            }
            else {
                v.push_back(p->val);
            }
            if (p->left != NULL) {
                next_level_stack.push_back(p->left);
            }
            if (p->right != NULL) {
                next_level_stack.push_back(p->right);
            }
            if (stack.empty()) {
                stack = next_level_stack;
                next_level_stack.clear();
                result.push_back(v);
                v.clear();
                flag = !flag;
            }
        }
        return result;
    }
};
