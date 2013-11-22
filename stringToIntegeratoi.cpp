#include "leetcode.h"
class Solution {
public:
    int atoi(const char *str) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int len = strlen(str);
        int i = 0;
        bool positive = true;
        long long result = 0;
        while (i < len && isspace(str[i])) 
            i ++;
        if (i < len && str[i] == '+') 
            i ++;
        else if (i < len && str[i] == '-') {
            positive = false;
            i ++;
        }
        while (i < len) {
            if (isdigit(str[i])) {
                result = 10*result + (str[i] - '0');
            } else {
                break;
            }
            i ++;
        }
        if (positive && result > 2147483647L) 
            return 2147483647;
        else if (!positive && result > 2147483648L)
            return -2147483648;
        if (positive)
            return result;
        else 
            return -result;
    }
};
int main() {
    Solution s;
    cout << s.atoi(" 1.3") << endl;
    return 0;
}

