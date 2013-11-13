#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <set>
#include <map>
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
        map<string, vector<string> > m;
        string temp;
        for (int i=0; i < strs.size(); ++i) {
            temp = strs[i];
            sort(temp.begin(), temp.end());
            if (m.find(temp) == m.end()) {
                //m[temp] = new vector<string>(1, strs[i]);
                vector<string> a;
                a.push_back(strs[i]);
                m[temp] = a;
            } else {
                m[temp].push_back(strs[i]);
            }
        }
        for (map<string, vector<string> >::iterator it=m.begin(); it != m.end(); it++) {
            if (it->second.size() > 1) {
                result.insert(result.begin(), it->second.begin(), it->second.end());
            }
        }
        return result;
    }
};
int main() {

    return 0;
}

