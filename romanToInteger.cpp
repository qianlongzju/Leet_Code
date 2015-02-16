#include "leetcode.h"
class Solution {
public:
    int romanToInt(string s) {
        int result = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == 'M') {
                if (i-1 >= 0 && s[i-1] == 'C') {
                    result -= 100;
                    result += 900;
                } else {
                    result += 1000;
                }
            } else if (s[i] == 'D') {
                if (i-1 >= 0 && s[i-1] == 'C') {
                    result -= 100;
                    result += 400;
                } else {
                    result += 500;
                }
            } else if (s[i] == 'C') {
                if (i-1 >= 0 && s[i-1] == 'X') {
                    result -= 10;
                    result += 90;
                } else {
                    result += 100;
                }
            } else if (s[i] == 'L') {
                if (i-1 >= 0 && s[i-1] == 'X') {
                    result -= 10;
                    result += 40;
                } else {
                    result += 50;
                }
            } else if (s[i] == 'X') {
                if (i-1 >= 0 && s[i-1] == 'I') {
                    result -= 1;
                    result += 9;
                } else {
                    result += 10;
                }
            } else if (s[i] == 'V') {
                if (i-1 >= 0 && s[i-1] == 'I') {
                    result -= 1;
                    result += 4;
                } else {
                    result += 5;
                }
            } else {
                result ++;
            }
        }
        return result;
    }
};
int main() {
    Solution s;
    cout << s.romanToInt("MCMLIV") << " :1954" << endl;
    cout << s.romanToInt("MCMXC") << " :1990" << endl;
    cout << s.romanToInt("MMVIII") << " :2008" << endl;
    return 0;
}

