#include "leetcode.h"
class Solution {
public:
    vector<int> grayCode(int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vi v;
        for (int i=0; i < (1<<n); i++) {
            v.push_back((i >> 1) ^ i);
        }
        return v;
    }
};
int main() {
    Solution s;
    vi v = s.grayCode(2);
    for (int i=0; i < v.size(); ++i) {
        cout << v[i] << " ";
    }
    cout << endl;

    return 0;
}

