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
#include <math.h>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
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
    bool search(int A[], int n, int target) {
        // left typing your C/C++ solution below
        // DO NOT write int main() function
        int left = 0; 
        int right = n - 1;
        while (left <= right) {
            int middle = left + (right - left) / 2;
            // cout << middle << endl;
            if (target == A[middle]) {
                return true;
            } else if (target == A[left]) {
                return true;
            } else if (target == A[right]) {
                return true;
            } else if (A[middle] > A[left]) {
                if (target > A[middle]) {
                    left = middle + 1;
                } else {
                    if (target > A[left]) {
                        right = middle - 1;
                    } else {
                        left = middle + 1;
                    }
                }
            } else if (A[middle] < A[left]) {
                if (target < A[middle]) {
                    right = middle - 1;
                } else {
                    if (target > A[right]) {
                        right = middle - 1;
                    } else {
                        left = middle + 1;
                    }
                }
            }
            else {
                left ++;
            }
        }
        return false;
    }
};
int main() {
    Solution s;
    int A[] = {1, 1, 3, 1};
    cout << s.search(A, 4, 3) << endl;
    cout << "A" << endl;
    int B[] = {1, 3, 1, 1, 1};
    cout << s.search(B, 5, 3) << endl;
    return 0;
}

