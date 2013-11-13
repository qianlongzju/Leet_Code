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
    vector<vector<string> > solveNQueens(int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<int> num;
        for (int i = 0; i < n; i++) {
            num.push_back(i);
        }
        vector<vector<string> > result;
        vector<vector<int> > permutations;
        permute(num, 0, permutations);
        for (int i = 0; i < permutations.size(); i++) {
            if (isValid(permutations[i])) {
                result.push_back(getSolution(permutations[i]));
            }
        }
        return result;
    }
    vector<string> getSolution(vector<int> permutation) {
        vector<string> result;
        for (int i=0; i < permutation.size(); i++) {
            string s = "";
            for (int j=0; j < permutation.size(); j++) {
                if (j == permutation[i]) {
                    s += "Q";
                } else {
                    s += ".";
                }
            }
            result.push_back(s);
        }
        return result;
    }
    bool isValid(vector<int> permutation) {
        for (int i=0; i < permutation.size(); i++) {
            for (int j=i+1; j < permutation.size(); j++) {
                if (j-i == permutation[j]-permutation[i]) {
                    return false;
                }
                if (j-i == permutation[i]-permutation[j]) {
                    return false;
                }
            }
        }
        return true;
    }
    void permute(vector<int> &num, int index,
            vector<vector<int> > &result) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (num.size() == index) {
            result.push_back(num);
            return;
        }
        for (int i=index; i < num.size(); ++i) {
            int temp = num[i];
            num[i] = num[index];
            num[index] = temp;
            permute(num, index+1, result);
            temp = num[i];
            num[i] = num[index];
            num[index] = temp;
        }
    }
};
int main() {
    Solution s;
    vector<vector<string> > v = s.solveNQueens(4);
    for (int i=0; i < v.size(); i++) {
        for (int j=0; j < v[i].size(); j++) {
            cout << v[i][j] << endl;
        }
        cout << endl;
    }
    return 0;
}

