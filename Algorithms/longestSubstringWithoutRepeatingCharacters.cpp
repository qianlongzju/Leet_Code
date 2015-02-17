#include "leetcode.h"
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        int i = 0, j = 0;
        int maxLen = 0;
        bool exist[256] = { false };
        while (j < n) {
            if (exist[s[j]]) {
                maxLen = max(maxLen, j-i);
                while (s[i] != s[j]) {
                    exist[s[i]] = false;
                    i++;
                }
                i++;
                j++;
            } else {
                exist[s[j]] = true;
                j++;
            }
        }
        maxLen = max(maxLen, n-i);
        return maxLen;
    }
};
int main(int argc, char const *argv[])
{
    vector<int> a, b;
    a.push_back(1);
    a.push_back(2);
    b.push_back(2);
    b.push_back(1);
/*  a.push_back(1);
    a.push_back(3);
    a.push_back(2);
    a.push_back(4);
    a.push_back(6);
    a.push_back(5);
    b.push_back(1);
    b.push_back(2);
    b.push_back(3);
    b.push_back(4);
    b.push_back(5);
    b.push_back(6);*/
    Solution s;
    cout << s.lengthOfLongestSubstring("wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"
) << endl;
    // while (p != NULL) {
    //  cout << p->val;
    //  p = p->left;
    // }
    //for (int i = 0; i < 3; ++i)
    //{
    //  cout << A[i];
    //}
    //cout << A[0]  << A[1] << A[2] << endl;
    return 0;
}
