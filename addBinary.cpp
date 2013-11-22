#include "leetcode.h"
class Solution {
public:
    string addBinary(string a, string b) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int m = a.size();
        int n = b.size();
        int p = 0, i;
        string s;
        for (i=0; i < m && i < n; i++) {
            int q = a[m-1-i] - '0' + b[n-1-i] - '0' + p;
            p = q / 2;
            if (q%2 == 1) {
                s.insert(0, 1, '1');
            }
            else {
                s.insert(0, 1, '0');
            }
        }
        for (; i < m; i++) {
            int q = a[m-1-i] - '0' + p;
            p = q / 2;
            if (q%2 == 1) {
                s.insert(0, 1, '1');
            }
            else {
                s.insert(0, 1, '0');
            }
        }
        for (; i < n; i++) {
            int q = b[n-1-i] - '0' + p;
            p = q / 2;
            if (q%2 == 1) {
                s.insert(0, 1, '1');
            }
            else {
                s.insert(0, 1, '0');
            }
        }
        if (p != 0) {
            s.insert(0, 1, '1');
        }
        return s;
    }
};
int main() {
    Solution s;
    string a("11");
    string b("1");
    cout << s.addBinary(a, b) << endl;
    return 0;
}
