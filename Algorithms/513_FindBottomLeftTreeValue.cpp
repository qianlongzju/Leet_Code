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
    int findBottomLeftValue(TreeNode* root) {
        deque<TreeNode*> cur_level, next_level;
        cur_level.push_back(root);
        int value = root->val;
        while(!cur_level.empty()) {
            TreeNode* node = cur_level.front();
            cur_level.pop_front();
            if (node->left != NULL) next_level.push_back(node->left);
            if (node->right != NULL) next_level.push_back(node->right);
            if (cur_level.empty()) {
                cur_level = next_level;
                if (!cur_level.empty())
                    value = cur_level.front()->val;
                next_level.clear();
            }
        }
        return value;
    }
};
