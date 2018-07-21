class Solution {
public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        return buildTreeDriver(preorder, 0, preorder.size()-1, inorder, 0, inorder.size()-1);
    }
    TreeNode *buildTreeDriver(vector<int> &preorder, int preStart, int preEnd, vector<int> &inorder, int inStart, int inEnd) {
        if (preStart > preEnd) {
            return NULL;
        }
        if (preStart == preEnd) {
            return new TreeNode(preorder[preStart]);
        }
        int rootVal = preorder[preStart];
        int rootIndex = 0;
        for (int i = inStart; i <= inEnd; ++i)
        {
            if (inorder[i] == rootVal) {
                rootIndex = i;
                break;
            }
        }
        TreeNode* root = new TreeNode(rootVal);
        root->left = buildTreeDriver(preorder, preStart+1, preStart+rootIndex-inStart, inorder, inStart, rootIndex-1);
        root->right = buildTreeDriver(preorder, preStart+rootIndex-inStart+1, preEnd, inorder, rootIndex+1, inEnd);
        return root;
    }
};
