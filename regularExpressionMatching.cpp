#include "leetcode.h"
//  If the next character of p is NOT ‘*’, then it must match the current character of s. Continue pattern matching with the next character of both s and p.
//  If the next character of p is ‘*’, then we do a brute force exhaustive matching of 0, 1, or more repeats of current character of p… Until we could not match any more characters.
class Solution {
public:
    bool isMatch(const char *s, const char *p) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if (*p == '\0')
            return *s == '\0';
        // next char is not '*': must match current character
        if (*(p+1) != '*') {
            return ((*p == *s) || (*p == '.' && *s != '\0')) && isMatch(s+1, p+1);
        }
        // next char is '*'
        while ((*p == *s) || (*p == '.' && *s != '\0')) {
            if (isMatch(s, p+2)) 
                return true;
            s++;
        }
        return isMatch(s, p+2);
    }
};
int main() {
    Solution s;
    cout << s.isMatch("aa", "a") << ",0" << endl;
    cout << s.isMatch("aa", "aa") << ",1" << endl;
    cout << s.isMatch("aaa", "aa") << ",0" << endl;
    cout << s.isMatch("aa", "a*") << ",1" << endl;
    cout << s.isMatch("aa", ".*") << ",1" << endl;
    cout << s.isMatch("ab", ".*") << ",1" << endl;
    cout << s.isMatch("aab", "c*a*b") << ",1" << endl;
    //cout << s.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b") << endl;
    return 0;
}

