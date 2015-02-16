#include "leetcode.h"
class Solution {
public:
    TreeNode *sortedArrayToBST(vector<int> &num) {
        return sortedSubArrayToBST(num, 0, num.size()-1);
    }
    TreeNode *sortedSubArrayToBST(vector<int> &num, int start, int end) {
        if (start > end) 
            return NULL;
        int middle = start + (end-start)/2;
        TreeNode* root = new TreeNode(num[middle]);
        root->left = sortedSubArrayToBST(num, start, middle-1);
        root->right = sortedSubArrayToBST(num, middle+1, end);
        return root;
    }
};
int main() {

    return 0;
}

