/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        if (root == NULL)
            return result;
        result.push_back(root->val);
        deque<TreeNode*> cur_level, next_level;
        cur_level.push_front(root);
        while(!cur_level.empty()) {
            TreeNode* node = cur_level.front();
            cur_level.pop_front();
            if (node->left != NULL) next_level.push_back(node->left);
            if (node->right != NULL) next_level.push_back(node->right);
            if (cur_level.empty()) {
                cur_level = next_level;
                next_level.clear();
                if (!cur_level.empty())
                    result.push_back(cur_level.back()->val);
            }
        }
        return result;
    }
};
