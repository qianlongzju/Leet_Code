#include "leetcode.h"
class Solution {
public:
    bool isMatch(const char *s, const char *p) {
        bool star = false;
        int i;
        for (i=0; s[i] != '\0'; i++) {
            switch(p[i]) {
                case '?':
                    break;
                case '*':
                    star = true;
                    p += i+1;
                    s += i;
                    i = -1;
                    while (*p == '*') {
                        p ++;
                    }
                    if (*p == '\0') {
                        return true;
                    }
                    break;
                default:
                    if (s[i] != p[i]) {
                        if (star) {
                            s ++;
                            i = -1;
                        } else {
                            return false;
                        }
                    }
                    break;
            }
        }
        while (p[i] == '*') {
            i ++;
        }
        return p[i] == '\0';
    }
    // dp: MLE or runtime error
    //bool isMatch(const char *s, const char *p) {
    //    // Note: The Solution object is instantiated only once and is reused by each test case.
    //    if (s == NULL || p == NULL) {
    //        return s == p;
    //    }
    //    while ((*s != '\0') && (*p != '\0') && (*s == *p)) {
    //        s ++;
    //        p ++;
    //    }
    //    if (*s == '\0' || *p == '\0') {
    //        return *s == *p;
    //    }
    //    int m = strlen(s);
    //    int n = strlen(p);
    //    while (m > 0 && n > 0 && *(s+m-1) == *(p+n-1)) {
    //        m--;
    //        n--;
    //    }
    //    if (m == 0 || n == 0)
    //        return m == n;
    //    //vector <vector <bool> > flag(m+1, vector<bool>(n+1, false));
    //    bool flag[m+1][n+1];
    //    flag[m][n] = true;
    //    for (int i=m-1, j=n-1; i >= 0 && j >= 0; i--,j--) {
    //        if (s[i] == '*') {
    //            for (int k = j; k >= 0; k--) {
    //                flag[i][k] = flag[i+1][j+1];
    //            }
    //        } else if (p[j] == '*') {
    //            for (int k = i; k >= 0; k--) {
    //                flag[k][j] = flag[i+1][j+1];
    //            }
    //        } else if (s[i] == '?' || p[j] == '?') {
    //            flag[i][j] = flag[i+1][j+1];
    //        } else {
    //            flag[i][j] = (s[i] == s[j]) && flag[i+1][j+1];
    //        }
    //    }
    //    return flag[0][0];
    //}

    // recursive version: tle
    // bool isMatch(const char *s, const char *p) {
    //     // Note: The Solution object is instantiated only once and is reused by each test case.
    //     if (s == NULL || p == NULL) {
    //         return s == p;
    //     }
    //     if (*s == '\0' || *p == '\0') {
    //         return *s == *p;
    //     }
    //     if (*s == '*') {
    //         while (*p != '\0') {
    //             if (isMatch(s+1, p))
    //                 return true;
    //             p = p+1;
    //         }
    //         return isMatch(s+1, p);
    //     } else if (*p == '*') {
    //         while (*s != '\0') {
    //             if (isMatch(s, p+1)) {
    //                 return true;
    //             }
    //             s = s+1;
    //         }
    //         return isMatch(s, p+1);
    //     } else if (*s == '?' || *p == '?') {
    //         return isMatch(s+1, p+1);
    //     } else {
    //         return (*s == *p) && isMatch(s+1, p+1);
    //     }
    // }
};
int main() {
    Solution s;
    cout << s.isMatch("aa", "a") << ",0" << endl;
    cout << s.isMatch("aa", "aa") << ",1" << endl;
    cout << s.isMatch("aaa", "aa") << ",0" << endl;
    cout << s.isMatch("aa", "*") << ",1" << endl;
    cout << s.isMatch("aa", "a*") << ",1" << endl;
    cout << s.isMatch("ab", "?*") << ",1" << endl;
    cout << s.isMatch("aab", "c*a*b") << ",0" << endl;
    cout << s.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b") << endl;
    return 0;
}
