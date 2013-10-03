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
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<int> a;
        return path_sum(root, sum, a);
    }
    vector<vector<int> > path_sum(TreeNode *root, int sum, vector<int> path) {
        vector<vector<int> > v;
        vector<vector<int> > p;
        if (root == NULL) {
            return v;
        }
        path.push_back(root->val);
        if (root->left == NULL && root->right == NULL && root->val == sum) {
            v.push_back(path);
            return v;
        }
        p = path_sum(root->left, sum-(root->val), path);
        for (int i=0; i < p.size(); i++) {
            v.push_back(p[i]);
        }
        p = path_sum(root->right, sum-(root->val), path);
        for (int i=0; i < p.size(); i++) {
            v.push_back(p[i]);
        }
        return v;
    }
};
