class Solution {
public:
    TreeNode *buildTree(vector<int>& inorder, vector<int>& postorder) {
        return buildTreeDriver(inorder, 0, inorder.size()-1, postorder, 0, postorder.size()-1);
    }
    TreeNode *buildTreeDriver(vector<int>& inorder, int inStart, int inEnd, vector<int>& postorder, int postStart, int postEnd) {   
        if (postStart > postEnd || inStart > inEnd) {
            return NULL;
        }
        if (postStart == postEnd) {
            return new TreeNode(postorder[postStart]);
        }
        int rootVal = postorder[postEnd];
        int rootIndex = 0;
        for (int i = inStart; i <= inEnd; ++i)
        {
            if (inorder[i] == rootVal) {
                rootIndex = i;
                break;
            }
        }
        TreeNode *root = new TreeNode(rootVal);
        root->left = buildTreeDriver(inorder, inStart, rootIndex-1, postorder, postStart, postStart+(rootIndex-inStart)-1);
        root->right = buildTreeDriver(inorder, rootIndex+1, inEnd, postorder, postStart+(rootIndex-inStart), postEnd-1);
        return root;
    }
};
