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
    vector<string> anagrams(vector<string> &strs) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<string> result;
        string temp;
        if (num.size() == 1) {
            temp ;
            result.push_back(temp);
            return result;
        }
        set<string> tempResult;
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

    return 0;
}

