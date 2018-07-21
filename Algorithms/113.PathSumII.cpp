class Solution {
public:
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
        vector<vector<int> > result;
        vector<int> path;
        path_sum(root, sum, path, result);
        return result;
    }
    void path_sum(TreeNode *root, int sum, vector<int> &path, 
            vector<vector<int> > &result) {
        if (root == NULL) {
            return;
        }
        path.push_back(root->val);
        if (root->left == NULL && root->right == NULL && root->val == sum) {
            result.push_back(path);
            path.pop_back();
            return;
        }
        path_sum(root->left, sum-(root->val), path, result);
        path_sum(root->right, sum-(root->val), path, result);
        path.pop_back();
    }
    /*
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
        vector<int> path;
        return path_sum(root, sum, path);
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
    */
};
