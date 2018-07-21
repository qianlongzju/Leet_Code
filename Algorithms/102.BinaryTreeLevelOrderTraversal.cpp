class Solution {
public:
    vector<vector<int> > levelOrder(TreeNode *root) {
        vector<vector<int> > result;
        if (root == NULL) {
            return result;
        }
        vector<int> v;
        vector<TreeNode*> stack;
        vector<TreeNode*> next_level_stack;
        stack.push_back(root);
        while (!stack.empty()) {
            TreeNode* p = stack.front();
            stack.erase(stack.begin());
            v.push_back(p->val);
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
            }
        }
        return result;
    }
};
