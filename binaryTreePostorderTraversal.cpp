#include "leetcode.h"
class Solution {
public:
    vector<int> postorderTraversal(TreeNode *root) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        vector<int> v;
        if (root == NULL)
            return v;
        stack<TreeNode*> stack;
        stack.push(root);
        TreeNode *prevNode = NULL;
        while (!stack.empty()) {
            TreeNode *currNode = stack.top();
            if (prevNode == NULL || prevNode->left == currNode || 
                    prevNode->right == currNode) {
                if (currNode->left != NULL) 
                    stack.push(currNode->left);
                else if (currNode->right != NULL) {
                    stack.push(currNode->right);
                }
            }
            else if (currNode->left == prevNode) {
                if (currNode->right != NULL)
                    stack.push(currNode->right);
            }
            else {
                v.push_back(currNode->val);
                stack.pop();
            }
            prevNode = currNode;
        }
        return v;
    }

    // recursive version
    //vector<int> postorderTraversal(TreeNode *root) {
    //    // IMPORTANT: Please reset any member data you declared, as
    //    // the same Solution instance will be reused for each test case.
    //    vector<int> v;
    //    if (root == NULL) {
    //        return v;
    //    }
    //    vector<int> left = postorderTraversal(root->left);
    //    for (int i=0; i < left.size(); i++) {
    //        v.push_back(left[i]);
    //    }
    //    vector<int> right = postorderTraversal(root->right);
    //    for (int i=0; i < right.size(); i++) {
    //        v.push_back(right[i]);
    //    }
    //    v.push_back(root->val);
    //    return v;
    //}
};
int main() {
    Solution s;

    return 0;
}

