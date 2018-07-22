class Solution {
public:
    vector<int> largestValues(TreeNode *root) {
        vector<int> result;
        if (root == NULL) return result;
        deque<TreeNode *> cur_level, next_level;
        cur_level.push_back(root);
        int maximum = root->val;
        while(!cur_level.empty()) {
            TreeNode *node = cur_level.front();
            cur_level.pop_front();
            maximum = max(maximum, node->val);
            if (node->left != NULL) next_level.push_back(node->left);
            if (node->right != NULL) next_level.push_back(node->right);
            if (cur_level.empty()) {
                result.push_back(maximum);
                if (next_level.empty()) break;
                cur_level = next_level;
                next_level.clear();
                maximum = cur_level.front()->val;
            }
        }
        return result;
    }
};
