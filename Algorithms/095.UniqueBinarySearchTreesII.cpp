class Solution {
public:
    vector<TreeNode *> generateTrees(int n) {
        return generateTreesSub(1, n);    
    }
    vector<TreeNode *> generateTreesSub(int start, int end) {
        vector<TreeNode *> result;
        if (start > end) {
            result.push_back(NULL);
            return result;
        }
        TreeNode* root;
        if (start == end) {
            root = new TreeNode(start);
            result.push_back(root);
            return result;
        }
        for (int i=start; i <= end; i++) {
            vector<TreeNode *> left = generateTreesSub(start, i-1);
            vector<TreeNode *> right = generateTreesSub(i+1, end);
            for (int j=0; j< left.size(); j++) {
                for (int k=0; k < right.size(); k++) {
                    root = new TreeNode(i);
                    root->left = left[j];
                    root->right = right[k];
                    result.push_back(root);
                }
            }
        }
        return result;
    }
};
