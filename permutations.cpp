#include <iostream>
#include <string>
#include <stack>
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
class Solution {
public:
    vector<vector<int> > permute(vector<int> &num) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<vector<int> > result;
        vector<int> temp;
        if (num.size() == 1) {
            temp.push_back(num[0]);
            result.push_back(temp);
            return result;
        }
        vector<int> sub(num.begin()+1, num.end());
        vector<vector<int> > v = permute(sub);
        for (int i=0; i < v.size(); ++i) {
            for (int j=0; j <= v[i].size(); j++) {
                temp = v[i];
                temp.insert(temp.begin()+j, num[0]);
                result.push_back(temp);
            }
        }
        return result;
    }
};
int main() {
    Solution s;
    vector<int> in;
    in.push_back(1);
    in.push_back(2);
    in.push_back(3);
    vector<vector<int> > v;
    v = s.permute(in);
    for (int i=0; i < v.size(); ++i) {
        for (int j=0; j < v[i].size(); j++) {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
