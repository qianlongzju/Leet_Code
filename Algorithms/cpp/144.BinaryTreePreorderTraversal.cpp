class Solution {
public:
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> v;
        stack<TreeNode *> stack;
        TreeNode *p = root;
        while (!stack.empty() || p != NULL) {
            if (p != NULL) {
                v.push_back(p->val);
                if (p->right != NULL)
                    stack.push(p->right);
                p = p->left;
            }
            else {
                p = stack.top();
                stack.pop();
            }
        }
        return v;
    }

    /*
    // recursive version
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> v;
        if (root == NULL) {
            return v;
        }
        v.push_back(root->val);
        vector<int> left = preorderTraversal(root->left);
        for (int i=0; i < left.size(); i++) {
            v.push_back(left[i]);
        }
        vector<int> right = preorderTraversal(root->right);
        for (int i=0; i < right.size(); i++) {
            v.push_back(right[i]);
        }
        return v;
    }
    */
};
