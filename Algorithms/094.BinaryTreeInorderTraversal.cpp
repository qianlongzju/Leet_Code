class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> v;
        stack<TreeNode*> stack;
        TreeNode *p = root;
        while (!stack.empty() || p != NULL) {
            if (p != NULL) {
                stack.push(p);
                p = p->left;
            }
            else {
                p = stack.top();
                stack.pop();
                v.push_back(p->val);
                p = p->right;
            }
        }
        return v;
    }
    /*
    // recursive
    vector<int> inorderTraversal(TreeNode *root) {
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
    */
};
