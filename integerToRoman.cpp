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
    string intToRoman(int num) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function    
        string s;
        while (num != 0) {
            if (num >= 1000) {
                s += "M";
                num -= 1000;
            } else if (num >= 900) {
                s += "CM";
                num -= 900;
            } else if (num >= 500) {
                s += "D";
                num -= 500;
            } else if (num >= 400) {
                s += "CD";
                num -= 400;
            } else if (num >= 100) {
                s += "C";
                num -= 100;
            } else if (num >= 90) {
                s += "XC"; 
                num -= 90;
            } else if (num >= 50) {
                s += "L";
                num -= 50;
            } else if (num >= 40) {
                s += "XL";
                num -= 40;
            } else if (num >= 10) {
                s += "X";
                num -= 10;
            } else if (num >= 9) {
                s += "IX";
                num -= 9;
            } else if (num >= 5) {
                s += "V";
                num -= 5;
            } else if (num >= 4) {
                s += "IV";
                num -=4;
            } else if (num > 0) {
                s += "I";
                num -= 1;
            }
        }
        return s;
    }
};
int main() {
    Solution s;
    cout << s.intToRoman(1000) << endl;
    return 0;
}

