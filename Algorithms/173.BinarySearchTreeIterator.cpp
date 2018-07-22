class BSTIterator {
private:
    stack<TreeNode *> path;
public:
    BSTIterator(TreeNode *root) {
        while (root != NULL) {
            path.push(root);
            root = root->left;
        }
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return path.size() != 0;
    }

    /** @return the next smallest number */
    int next() {
        TreeNode *result = path.top();
        path.pop();
        TreeNode *temp = result->right;
        while (temp != NULL) {
            path.push(temp);
            temp = temp->left;
        }
        return result->val; 
    }
};
