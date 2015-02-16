#include "leetcode.h"
class Solution {
public:
    vector<vector<string> > partition(string s) {
        vector<vector<string> > result;
        vector<string> output; // 一个 partition 方案
        DFS(s, 0, output, result);
        return result;
    }
    // 搜索必须以 s[start] 开头的 partition 方案
    void DFS(string &s, int start, vector<string> &output,
        vector<vector<string> > &result) {
        if (start == s.size()) {
            result.push_back(output);
            return;
        }
        for (int i = start; i < s.size(); i++) {
            if (isPalindrome(s, start, i)) { // 从 i 位置砍一刀
                output.push_back(s.substr(start, i - start + 1));
                DFS(s, i + 1, output, result); // 继续往下砍
                output.pop_back(); // 撤销上一个 push_back 的砍
            }
        }
    }
    bool isPalindrome(string &s, int start, int end) {
        while (start < end) {
            if (s[start] != s[end]) return false;
            start++;
            end--;
        }
        return true;
    }
};
int main() {

    return 0;
}

