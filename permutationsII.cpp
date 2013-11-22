#include "leetcode.h"
class Solution {
public:
    vector<vector<int> > permuteUnique(vector<int> &num) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<vector<int> > result;
        set<vector<int> > uniqueResult;
        vector<int> temp;
        if (num.size() == 1) {
            temp.push_back(num[0]);
            result.push_back(temp);
            return result;
        }
        vector<int> sub(num.begin()+1, num.end());
        vector<vector<int> > v = permuteUnique(sub);
        for (int i=0; i < v.size(); ++i) {
            for (int j=0; j <= v[i].size(); j++) {
                temp = v[i];
                temp.insert(temp.begin()+j, num[0]);
                uniqueResult.insert(temp);
            }
        }
        for (set<vector<int> >::iterator it=uniqueResult.begin(); it!=uniqueResult.end(); ++it) {
            result.push_back(*it);
        }
        return result;
    }
};
int main() {
    Solution s;
    vector<int> in;
    in.push_back(1);
    in.push_back(1);
    in.push_back(3);
    vector<vector<int> > v;
    v = s.permuteUnique(in);
    for (int i=0; i < v.size(); ++i) {
        for (int j=0; j < v[i].size(); j++) {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
