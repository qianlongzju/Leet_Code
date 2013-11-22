#include "leetcode.h"
class Solution {
public:
    bool wordBreak(string s, unordered_set<string> &dict) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int n = s.size();
        bool wb[n];
        memset(wb, false, n);
        for (int i=0; i < n; ++i) {
            if (wb[i] == false && dict.find(s.substr(0, i+1)) != dict.end()) {
                wb[i] = true;
            }
            if (wb[i] == true) {
                if (i == n-1) {
                    return true;
                }
                for (int j=i+1; j < n; ++j) {
                    if (wb[j] == false && dict.find(s.substr(i+1, (j+1)-(i+1))) != dict.end()) {
                        wb[j] = true;
                    }
                    if (j == n-1 && wb[j] == true) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
};
int main() {
    Solution s;
    unordered_set<string> dict;
    dict.insert("leet");
    dict.insert("code");
    cout << s.wordBreak("leetcode", dict) << endl;
    return 0;
}

