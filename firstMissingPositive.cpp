#include <iostream>
#include <string>
#include <sstream>
#include <stack>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <limits.h>
#include <stdlib.h>
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
class Solution {
public:
    int firstMissingPositive(int A[], int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        for (int i=0; i < n; i++) {
            while (A[i] <= n  && A[i] > 0 && A[i] != i+1) {
                int temp = A[A[i]-1];
                if (temp == A[i]) {
                    break;
                }
                A[A[i]-1] = A[i];
                A[i] = temp;
            }
        }        
        for (int i=0; i < n; i++) {
            if (A[i] != i+1) {
                return i+1;
            }
        }
        return n+1;
    }
};
int main() {
    Solution s;
    int a[] = {1, 2, 0};
    cout << s.firstMissingPositive(a, 3) << endl;
    int b[] = {3, 4, -1, 1};
    cout << s.firstMissingPositive(b, 4) << endl;
    int c[] = {1, 1};
    cout << s.firstMissingPositive(c, 2) << endl;
    return 0;
}

