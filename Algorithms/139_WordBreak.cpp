#include "leetcode.h"
class Solution {
public:
    bool wordBreak(string s, vector<string> &wordDict) {
        int n = s.size();
        bool wb[n];
        memset(wb, false, n);
        for (int i = 0; i < n; ++i) {
            if (wb[i] == false && find(begin(wordDict), end(wordDict), s.substr(0, i+1)) != wordDict.end())
                wb[i] = true;
            if (wb[i] == true) {
                if (i == n-1) return true;
                for (int j = i+1; j < n; ++j) {
                    if (wb[j] == false && 
                            find(begin(wordDict), end(wordDict), s.substr(i+1, (j+1)-(i+1))) != wordDict.end())
                        wb[j] = true;
                    if (j == n-1 && wb[j] == true) return true;
                }
            }
        }
        return false;
    }
};
int main() {
    Solution s;
    vector<string> dict;
    dict.push_back("leet");
    dict.push_back("code");
    cout << s.wordBreak("leetcode", dict) << endl;
    return 0;
}
