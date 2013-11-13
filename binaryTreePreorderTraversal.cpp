#include "leetcode.h"
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector< pair<double,ii> > vdii;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
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
    vector<int> preorderTraversal(TreeNode *root) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        vector<int> v;
        stack<TreeNode*> stack;
        TreeNode *p = root;
        while (!stack.empty() || p != NULL) {
            if (p != NULL) {
                v.push_back(p->val);
                if (p->right != NULL)
                    stack.push(p->right);
                p = p->left;
            }
            else {
                p = stack.top();
                stack.pop();
            }
        }
        return v;
    }

    // recursive version
    //vector<int> preorderTraversal(TreeNode *root) {
    //    // IMPORTANT: Please reset any member data you declared, as
    //    // the same Solution instance will be reused for each test case.
    //    vector<int> v;
    //    if (root == NULL) {
    //        return v;
    //    }
    //    v.push_back(root->val);
    //    vector<int> left = preorderTraversal(root->left);
    //    for (int i=0; i < left.size(); i++) {
    //        v.push_back(left[i]);
    //    }
    //    vector<int> right = preorderTraversal(root->right);
    //    for (int i=0; i < right.size(); i++) {
    //        v.push_back(right[i]);
    //    }
    //    return v;
    //}
};
int main() {
    Solution s;

    return 0;
}

