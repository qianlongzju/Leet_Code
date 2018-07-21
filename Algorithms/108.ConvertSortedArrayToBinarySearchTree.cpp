class Solution {
public:
    TreeNode *sortedArrayToBST(vector<int> &num) {
        return sortedArrayToBST(num, 0, num.size()-1);
    }
    TreeNode *sortedArrayToBST(vector<int> &num, int start, int end) {
        if (start > end) return NULL;
        int middle = start + (end-start)/2;
        TreeNode* root = new TreeNode(num[middle]);
        root->left = sortedArrayToBST(num, start, middle-1);
        root->right = sortedArrayToBST(num, middle+1, end);
        return root;
    }
};
