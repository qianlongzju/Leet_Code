#include "leetcode.h"
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int n = s.size();
        vector<string> v;
        for (int i=1; i <= 3 && i < n; i++) {
            int a = atoi(s.substr(0, i).c_str());
            if (a > 255) {
                continue;
            }
            for (int j=i+1; j <= i+3 && j < n; j++) {
                int b = atoi(s.substr(i, j-i).c_str());
                if (b > 255) {
                    continue;
                }
                for (int k=j+1; k <= j+3 && k < n; k++) {
                    int c = atoi(s.substr(j, k-j).c_str()); 
                    if (n-k > 3) {
                        continue;
                    }
                    int d = atoi(s.substr(k, n-k).c_str()); 
                    if (c > 255 || d > 255) {
                        continue;
                    }
                    stringstream ss;
                    ss << a << "." <<  b << "." << c << "." << d;
                    string temp = ss.str();
                    if (temp.size() == n + 3) {
                        v.push_back(temp);
                    }
                }
            }
        }
        return v;
    }
};
int main() {
    Solution s;
    vector<string> v = s.restoreIpAddresses("25525511135");
    for (int i=0; i < v.size(); i++) {
        cout << v[i] << endl;
    }
    v = s.restoreIpAddresses("0279245587303");
    for (int i=0; i < v.size(); i++) {
        cout << v[i] << endl;
    }
    return 0;
}

