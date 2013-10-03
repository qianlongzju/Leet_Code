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
    int maximalRectangle(vector<vector<char> > &matrix) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<vector<vector<int> > > record;
        for (int i = 0; i < matrix.size(); i ++) {
            vector<vector<int> > w;
            for (int j = 0; j < matrix[i].size(); j++) {
                vector<int> v;
                v.push_back(0);
                v.push_back(0);
                w.push_back(v);
            }
            record.push_back(w);
        }
        for (int i = 0; i < matrix.size(); i ++) {
            for (int j = 0; j < matrix[i].size(); j++) {
                if (matrix[i][j] == '0') {
                    continue;
                }
                if (i == 0 || j == 0) {
                    if (i > 0) {
                        record[i][j][0] = record[i-1][j][0]?record[i-1][j][0]+1:1;
                        record[i][j][1] = 1;
                    } else if (j > 0) {
                        record[i][j][1] = record[i][j-1][1]?record[i][j-1][1]+1:1;
                        record[i][j][0] = 1;
                    } else {
                        record[i][j][0] = 1;
                        record[i][j][1] = 1;
                    }
                } else {
                    record[i][j][0] = record[i-1][j][0] + 1;
                    record[i][j][1] = record[i][j-1][1] + 1;
                }
            }
        }
        int max = 0;
        for (int i = 0; i < matrix.size(); i ++) {
            for (int j = 0; j < matrix[i].size(); j++) {
                cout << record[i][j][0] << record[i][j][1] << " ";
                if (record[i][j][0] * record[i][j][1] > max) {
                    max = record[i][j][0] * record[i][j][1];
                }
            }
            cout << endl;
        }
        return max; 
    }
};
int main() {
    Solution s;
    vector<char> a;
    a.push_back('0');
    a.push_back('1');
    a.push_back('1');
    a.push_back('0');
    a.push_back('1');
    vector<char> b;
    b.push_back('1');
    b.push_back('1');
    b.push_back('0');
    b.push_back('1');
    b.push_back('0');
    vector<char> c;
    c.push_back('0');
    c.push_back('1');
    c.push_back('1');
    c.push_back('1');
    c.push_back('0');
    vector<char> d;
    d.push_back('1');
    d.push_back('1');
    d.push_back('1');
    d.push_back('1');
    d.push_back('0');
    vector<char> e;
    e.push_back('1');
    e.push_back('1');
    e.push_back('1');
    e.push_back('1');
    e.push_back('1');
    vector<char> f;
    f.push_back('0');
    f.push_back('0');
    f.push_back('0');
    f.push_back('0');
    f.push_back('0');
    vector<vector<char> > v;
    v.push_back(a);
    v.push_back(b);
    v.push_back(c);
    v.push_back(d);
    v.push_back(e);
    v.push_back(f);
    cout << s.maximalRectangle(v) << endl;

    return 0;
}

