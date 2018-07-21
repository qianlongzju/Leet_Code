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
int main() {
    TreeNode* a1 = new TreeNode(5);
    TreeNode* a2 = new TreeNode(4);
    TreeNode* a3 = new TreeNode(8);
    TreeNode* a4 = new TreeNode(11);
    TreeNode* a5 = new TreeNode(13);
    TreeNode* a6 = new TreeNode(4);
    TreeNode* a7 = new TreeNode(7);
    TreeNode* a8 = new TreeNode(2);
    TreeNode* a9 = new TreeNode(5);
    TreeNode* a10 = new TreeNode(1);
    a1->left = a2;
    a1->right = a3;
    a2->left = a4;
    a3->left = a5;
    a3->right = a6;
    a4->left = a7;
    a4->right = a8;
    a6->left = a9;
    a6->right = a10;
    Solution s;
    vector<vector<int> > v = s.pathSum(a1, 22);
    for (int i = 0; i < v.size(); ++i) {
        for (int j = 0; j < v[i].size(); j++) {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
