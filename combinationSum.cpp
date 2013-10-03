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
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<vector<int> > result;
        sort(candidates.begin(), candidates.end());
        int index[target];
        index[0] = candidates.size()-1;
        solve(target, candidates, index, 0, result);
        return result;
    }
    
    void solve(int target, vector<int> &candidates, int index[], 
            int n, vector<vector<int> > &result) {
        if (target < 0)
            return ;
        if (target == 0) {
            vector<int> v;
            for (int i = n; i >= 1; i--) {
                v.push_back(candidates[index[i]]);
            }
            result.push_back(v);
        }
    
        for (int i = index[n]; i >= 0; i--) {
            index[n+1] = i;
            solve(target-candidates[i], candidates, index, n+1, result);
        }
    }
    //vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
    //    // Start typing your C/C++ solution below
    //    // DO NOT write int main() function
    //    vector<vector<int> > result;
    //    sort(candidates.begin(), candidates.end());
    //    int index[target];
    //    index[0] = 0;
    //    solve(target, 0, candidates, index, 0, result);
    //    return result;
    //}
    //
    //void solve(int target, int sum, vector<int> &candidates, int index[], 
    //        int n, vector<vector<int> > &result) {
    //    if (sum > target)
    //        return;
    //    if (sum == target) {
    //        vector<int> v;
    //        for (int i=1; i <= n; i++) {
    //            v.push_back(candidates[index[i]]);
    //        }
    //        result.push_back(v);
    //    }
    //
    //    for (int i = index[n]; i < candidates.size(); i++) {
    //        index[n+1] = i;
    //        solve(target, sum + candidates[i], candidates, index, n+1, result);
    //    }
    //}
    // for further thoughts on
    // http://leetcode.com/2010/09/print-all-combinations-of-number-as-sum.html
    //vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
    //    // Start typing your C/C++ solution below
    //    // DO NOT write int main() function
    //    vector<vector<int> > result;
    //    sort(candidates.begin(), candidates.end());
    //    int index[target];
    //    index[0] = -1;
    //    solve(target, 0, candidates, index, 0, result);
    //    return result;
    //}
    //
    //void solve(int target, int sum, vector<int> &candidates, int index[], 
    //        int n, vector<vector<int> > &result) {
    //    if (sum > target)
    //        return;
    //    if (sum == target) {
    //        vector<int> v;
    //        for (int i=1; i <= n; i++) {
    //            v.push_back(candidates[index[i]]);
    //        }
    //        result.push_back(v);
    //    }
    //
    //    for (int i = index[n]+1; i < candidates.size(); i++) {
    //        index[n+1] = i+1;
    //        solve(target, sum + candidates[i+1], candidates, index, n+1, result);
    //    }
    //}
};
int main() {
    Solution s;
    vector<int> candidates;
    candidates.push_back(2);
    candidates.push_back(3);
    candidates.push_back(6);
    candidates.push_back(7);
    vector<vector<int> > v = s.combinationSum(candidates, 7);
    for (int i = 0; i < v.size(); i++) {
        for (int j = 0; j < v[i].size(); j++) {
            cout << v[i][j] << ((j == v[i].size()-1)?"":" ");
        }
        cout << endl;
    }
    return 0;
}
