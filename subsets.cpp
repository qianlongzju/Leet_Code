#include "leetcode.h"
class Solution {
public:
    vector<vector<int> > subsets(vector<int> &S) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        sort(S.begin(), S.end());        
        int n = S.size();
        //for (int i=0; i < n; i++)
        //    cout << S[i] << " ";
        //cout << endl;
        vector<vector<int> > result;
        for (int i=0; i < pow(2, n); i++) {
            vector<int> v;
            int j = i;
            int k = 0;
            while (j != 0) {
                if (j & 0x01) {
                    v.push_back(S[k]);
                }
                k ++;
                j >>= 1;
            }
            result.push_back(v);
        }
        return result;
    }
};
int main() {
    Solution s;
    vector<int> a;
    a.push_back(1);
    a.push_back(2);
    a.push_back(3);
    vector<vector<int> > v = s.subsets(a);
    for (int i=0; i < v.size(); i++) {
        for (int j=0; j < v[i].size(); j++) {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}

