/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
private:
	stack<TreeNode*> path;
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

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */
