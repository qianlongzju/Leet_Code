#include "leetcode.h"
class Solution {
public:
    int minCut(string s) {
        const int len = s.size();
        int f[len+1];
        bool p[len][len];
        // the worst case is cutting by each char
        for (int i = 0; i <= len; i++)
            f[i] = len - 1 - i; // 最后一个 f[len]=-1
        for (int i = 0; i < len; i++)
            for (int j = 0; j < len; j++)
                p[i][j] = false;
        for (int i = len - 1; i >= 0; i--) {
            for (int j = i; j < len; j++) {
                if (s[i] == s[j] && (j - i < 2 || p[i + 1][j - 1])) {
                    p[i][j] = true;
                    f[i] = min(f[i], f[j + 1] + 1);
                }
            }
        }
        return f[0];
    }

    // TLE
    // int minCut(string s) {
    //     // Note: The Solution object is instantiated only once and is reused by each test case.
    //     vector<string> output; // 一个 partition 方案
    //     int result = INT_MAX;
    //     DFS(s, 0, output, result);
    //     return result;
    // }
    // // 搜索必须以 s[start] 开头的 partition 方案
    // void DFS(string &s, int start, vector<string> &output, int &result) {
    //     if (start == s.size()) {
    //         int tmp = output.size();
    //         if (tmp < result)
    //             result = tmp;
    //         return;
    //     }
    //     for (int i = start; i < s.size(); i++) {
    //         if (isPalindrome(s, start, i)) { // 从 i 位置砍一刀
    //             output.push_back(s.substr(start, i - start + 1));
    //             DFS(s, i + 1, output, result); // 继续往下砍
    //             output.pop_back(); // 撤销上一个 push_back 的砍
    //         }
    //     }
    // }
    // bool isPalindrome(string &s, int start, int end) {
    //     while (start < end) {
    //         if (s[start] != s[end]) return false;
    //         start++;
    //         end--;
    //     }
    //     return true;
    // }
};
int main() {

    return 0;
}

