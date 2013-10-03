#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <set>
#include <algorithm>
#include <limits.h>
using namespace std;
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode *sortedArrayToBST(vector<int> &num) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        return sortedSubArrayToBST(num, 0, num.size()-1);
    }
    TreeNode *sortedSubArrayToBST(vector<int> &num, int start, int end) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
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

