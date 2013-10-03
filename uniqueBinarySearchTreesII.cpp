#include <iostream>
#include <string>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <algorithm>
#include <limits.h>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
void printTree(TreeNode* root) {
    if (root == NULL) {
        return;
    }
    queue<TreeNode *> treeNodeQueue;
    queue<char> numQueue;
    treeNodeQueue.push(root);
    while (!treeNodeQueue.empty()) {
        TreeNode* tmp = treeNodeQueue.front();
        treeNodeQueue.pop();
        if (tmp != NULL) {
            numQueue.push(tmp->val + '0');
        } else {
            numQueue.push('#');
            continue;
        }
        if (tmp->left != NULL) {
            treeNodeQueue.push(tmp->left);
        } else {
            treeNodeQueue.push(NULL);
        }
        if (tmp->right != NULL) {
            treeNodeQueue.push(tmp->right);
        } else {
            treeNodeQueue.push(NULL);
        }
    }
    while (!numQueue.empty()) {
        char c = numQueue.front();
        cout << c;
        numQueue.pop();
    }
}
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
    vector<TreeNode *> generateTrees(int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        return generateTreesSub(1, n);    
    }
    vector<TreeNode *> generateTreesSub(int start, int end) {
        vector<TreeNode *> result;
        if (start > end) {
            result.push_back(NULL);
            return result;
        }
        TreeNode* root;
        if (start == end) {
            root = new TreeNode(start);
            result.push_back(root);
            return result;
        }
        for (int i=start; i <= end; i++) {
            vector<TreeNode *> left = generateTreesSub(start, i-1);
            vector<TreeNode *> right = generateTreesSub(i+1, end);
            for (int j=0; j< left.size(); j++) {
                for (int k=0; k < right.size(); k++) {
                    root = new TreeNode(i);
                    root->left = left[j];
                    root->right = right[k];
                    result.push_back(root);
                }
            }
        }
        return result;
    }
};
int main() {
    Solution s;
    vector<TreeNode *> v = s.generateTrees(3);
    for (int i=0; i < v.size(); i++) {
        printTree(v[i]);
        cout << endl;
    }
    return 0;
}
