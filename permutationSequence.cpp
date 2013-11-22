#include "leetcode.h"
class Solution {
public:
    string getPermutation(int n, int k) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        string permutation;
        vector<int> s;
        for (int i=1; i <= n; i++) {
            s.push_back(i);
        }
        getPermutation(s, k, permutation);
        return permutation;
    }
    void getPermutation(vector<int>& s, int k, string& permutation) {
        if (s.size() == 1) {
         //   cout << "final k:" << k << endl;
            permutation.push_back(s[0] + '0');
            return;
        }
        int p = 1;
        //for (int i=0; i < s.size(); ++i) {
        //    cout << s[i] << " ";
        //}
        //cout << endl;
        for (int i=2; i <= s.size()-1; i++) {
            p = p*i;
        }
        //cout << "p: " << p << ", k:" << k << endl;
        int a = s[(k-1)/p];
        permutation.push_back(a + '0');
        k -= ((k-1)/p)*p;
        //cout << "a: " << a  << ", k:" << k << endl;
        //for (int i=0; i < s.size(); ++i) {
        //    cout << s[i] << " ";
        //}
        //cout << endl;
        s.erase(find(all(s), a));
        //for (int i=0; i < s.size(); ++i) {
        //    cout << s[i] << " ";
        //}
        //cout << endl;
        getPermutation(s, k, permutation);
    }
};
int main() {
    Solution s;
    cout << s.getPermutation(3, 1) << endl;
    cout << s.getPermutation(3, 2) << endl;
    cout << s.getPermutation(3, 3) << endl;
    cout << s.getPermutation(3, 4) << endl;
    cout << s.getPermutation(3, 5) << endl;
    cout << s.getPermutation(3, 6) << endl;
    return 0;
}

