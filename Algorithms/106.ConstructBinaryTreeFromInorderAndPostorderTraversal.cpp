class Solution {
public:
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
        return buildTreeDriver(inorder, 0, inorder.size()-1, postorder, 0, postorder.size()-1);
    }
    TreeNode *buildTreeDriver(vector<int> &inorder, int inStart, int inEnd, vector<int> &postorder, int postStart, int postEnd) {   
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
        TreeNode* root = new TreeNode(rootVal);
        root->left = buildTreeDriver(inorder, inStart, rootIndex-1, postorder, postStart, postStart+(rootIndex-inStart)-1);
        root->right = buildTreeDriver(inorder, rootIndex+1, inEnd, postorder, postStart+(rootIndex-inStart), postEnd-1);
        return root;
    }
};
int main(int argc, char const *argv[])
{
    vector<int> a, b;
    a.push_back(1);
    a.push_back(2);
    b.push_back(2);
    b.push_back(1);
/*  a.push_back(1);
    a.push_back(3);
    a.push_back(2);
    a.push_back(4);
    a.push_back(6);
    a.push_back(5);
    b.push_back(1);
    b.push_back(2);
    b.push_back(3);
    b.push_back(4);
    b.push_back(5);
    b.push_back(6);*/
    Solution s;
    TreeNode* p = s.buildTree(a, b);
    // while (p != NULL) {
    //  cout << p->val;
    //  p = p->left;
    // }
    //for (int i = 0; i < 3; ++i)
    //{
   //   cout << A[i];
    //}
    //cout << A[0]  << A[1] << A[2] << endl;
    return 0;
}
