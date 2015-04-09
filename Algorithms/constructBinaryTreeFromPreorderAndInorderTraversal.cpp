#include "leetcode.h"
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
int main(int argc, char const *argv[])
{
    vector<int> a, b;
    a.push_back(1);
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
    b.push_back(6);
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
