#include "leetcode.h"
class Solution {
public:
    vector<vector<int> > combine(int n, int k) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<vector<int> > result;
        vector<int> path;
        combine(n, k, 1, path, result);
        return result;
    }
    void combine(int n, int k, int min, vector<int> path, 
            vector<vector<int> > &result) {
        if (path.size() == k) {
            result.push_back(path);
            return;
        }
        if (min > n) {
            return;
        }
        combine(n, k, min+1, path, result);
        path.push_back(min);
        combine(n, k, min+1, path, result);
    }
    //vector<vector<int> > combine(int n, int k) {
    //    // Start typing your C/C++ solution below
    //    // DO NOT write int main() function
    //    vector<vector<int> > result;
    //    for (int i=0; i < pow(2, n); i++) {
    //        vector<int> v;
    //        int j = i;
    //        int p = 1;
    //        int q = 0;
    //        while (j != 0) {
    //            if (j & 0x01) {
    //                v.push_back(p);
    //                q ++;
    //            }
    //            p ++;
    //            j >>= 1;
    //        }
    //        if (k == q) {
    //            result.push_back(v);
    //        }
    //    }
    //    return result;
    //}
};
int main() {
    Solution s;
    vector<vector<int> > v = s.combine(4, 2);
    for (int i=0; i < v.size(); i++) {
        for (int j=0; j < v[i].size(); j++) {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}

